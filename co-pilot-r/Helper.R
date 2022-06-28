# hint: during docker built renv will find these dependencies on its own (via `renv::init()`)
# for parsing JSON
library(jsonlite)
# for http communication
library(httr)
# for loading move CSV files
library(move)

readInput <- function(sourceFile) {
  input <- NULL
  if(!is.null(sourceFile) && sourceFile != "") {
    if (file.info(sourceFile)$size == 0) {
        # handle the special `null`-input
        logger.warn("The App has received invalid input! It cannot process NULL-input. Aborting..")
        # codes for exception handling
        # 10: abort consuming null-input
        stop("The App has received invalid input! It cannot process NULL-input. Check the output of the preceding App or adjust the datasource configuration. [code 10]")
    }
    logger.debug("Loading file from %s", sourceFile)
    input <- tryCatch({
        # 1: try to read input as move RDS file
        readRDS(file = sourceFile)
      },
      error = function(readRdsError) {
        tryCatch({
          # 2 (fallback): try to read input as move CSV file
          move(sourceFile, removeDuplicatedTimestamps=TRUE)
        },
        error = function(readCsvError) {
          # collect errors for report and throw custom error
          stop(paste(sourceFile, " -> readRDS(sourceFile): ", readRdsError, "move(sourceFile): ", readCsvError, sep = ""))
        })
      })
  } else {
    logger.debug("Skip loading: no source File")
  }

  input
}

storeResult <- function(result, outputFile) {
    if(!is.null(outputFile) && outputFile != "" && !is.null(result)) {
        logger.debug("Storing RDS to file %s", outputFile)
        saveRDS(result, file = outputFile)
    } else {
        logger.debug("Storing the null-result to file %s", outputFile)
        file.create(outputFile) # write an empty file (for post-processing etc.)
    }
}

storeToFile <- function(result, outputFile) {
    if(!is.null(outputFile) && outputFile != "" && !is.null(result)) {
        logger.debug("Writing to file %s", outputFile)
        write(paste(result), file = outputFile)
    } else {
        logger.debug("Skip writing to file: no output File or result is missing")
    }
}

configuration <- function() {
    configurationString <- Sys.getenv(x = "CONFIGURATION", "{}")

    result <- if(configurationString != "") {
        fromJSON(txt=configurationString)
    } else {
        NULL
    }

    if (Sys.getenv(x = "PRINT_CONFIGURATION", "no") == "yes") {
        logger.debug("parse stored configuration: \'%s\'", configurationString)
        logger.info("app will be started with configuration:\n%s", toJSON(result, auto_unbox = TRUE, pretty = TRUE))
    }
    result
}

sourceFile <- function() {
    result <- Sys.getenv(x = "SOURCE_FILE", "")
    logger.debug("sourceFile: %s", result)
    result
}

outputFile <- function() {
    result <- Sys.getenv(x = "OUTPUT_FILE", "")
    logger.debug("outputFile: %s", result)
    result
}

errorFile <- function() {
  result <- Sys.getenv(x = "ERROR_FILE", "")
  logger.debug("errorFile: %s", result)
  result
}

pilotEndpoint <- function() {
  Sys.getenv(x = "PILOT_ENDPOINT", "http://localhost:8100")
}

httpClientLogging <- function() {
  httpClientLogging <- Sys.getenv(x = "PILOT_CLIENT_LOG_LEVEL", "NULL") # real NULL not possible (?!)
  httpClientLogging != "NULL"
}

notifyDone <- function(executionType) {
  logger.debug("notify done with success")
  response <- POST(
    paste(pilotEndpoint(), "/pilot/api/v1/copilot/done", sep = ""),
    body = jsonlite::toJSON(list("success" = TRUE, "executionType" = executionType), auto_unbox = TRUE),
    encode = "json",
    content_type_json(),
    if (httpClientLogging()) verbose(info = TRUE, data_out = TRUE, data_in = TRUE)
  )
}

storeConfiguration <- function(configuration) {
  logger.debug("Storing configuration in pilot: %s", configuration)

  response <- POST(
    paste(pilotEndpoint(), "/pilot/api/v1/copilot/configuration", sep = ""),
    body = jsonlite::toJSON(list("configuration" = configuration), auto_unbox = TRUE),
    encode = "json",
    content_type_json(),
    if (httpClientLogging()) verbose(info = TRUE, data_out = TRUE, data_in = TRUE)
  )

  parsedResponse <- content(response, "parsed")

  if (parsedResponse["success"] == TRUE) {
    newConfiguration = toJSON(parsedResponse[["configuration"]], auto_unbox = TRUE)
    Sys.setenv(CONFIGURATION = newConfiguration)
    logger.debug("Set new configuration environment: %s", newConfiguration)
  } else {
    logger.info("Couldn't store Configuration")
  }
}


##### LOGGER

FATAL <- 1L
names(FATAL) <- "FATAL"
ERROR <- 2L
names(ERROR) <- "ERROR"
WARN <- 4L
names(WARN) <- "WARN"
INFO <- 6L
names(INFO) <- "INFO"
DEBUG <- 8L
names(DEBUG) <- "DEBUG"
TRACE <- 9L
names(TRACE) <- "TRACE"

logger.layout <- function(level, msg, id='', ...) {
  the.time <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
  if (length(list(...)) > 0) {
    parsed <- lapply(list(...), function(x) if(is.null(x)) 'NULL' else x )
    msg <- do.call(sprintf, c(msg, parsed))
  }
  sprintf("[%s] %s\n", names(level), msg)
}

logger.log_level <- function(msg, ..., level)
{
  if (level <= logger.threshold)  {
    message <- logger.layout(level, msg, name, ...)
    cat(message)
  }
}

logger.trace <- function(msg, ...) {
  logger.log_level(msg, ..., level=TRACE)
}

logger.debug <- function(msg, ...) {
  logger.log_level(msg, ..., level=DEBUG)
}

logger.info <- function(msg, ...) {
  logger.log_level(msg, ..., level=INFO)
}

logger.warn <- function(msg, ...) {
  logger.log_level(msg, ..., level=WARN)
}

logger.error <- function(msg, ...) {
  logger.log_level(msg, ..., level = ERROR)
}

logger.fatal <- function(msg, ...) {
  logger.log_level(msg, ..., level = FATAL)
}

logger.threshold = Sys.getenv(x = "LOG_LEVEL_SDK", TRACE)

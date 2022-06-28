# this file is in the root dir of the builder app (docker)
source("Helper.R")
# this file comes from the app developer and is also located in the root dir
source("RFunction.R")

tryCatch(
{
  setwd("/root/app/")
  Sys.setenv(tz="UTC")

  args <- configuration()
  data <- readInput(sourceFile())
  if (!is.null(data)) {
    args[["data"]] <- data
  }

  result <- do.call(rFunction, args)

  storeResult(result, outputFile())

},
error = function(e)
{
  # error handler picks up where error was generated
  print(paste("ERROR: ", e))
  storeToFile(e, errorFile())
  stop(e) # re-throw the exception
})
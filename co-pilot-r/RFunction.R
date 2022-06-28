########################################################################################################################
# RFunction.R
# This file is provided by the app developer. 
# It gets the configuration (reference_time) and the input-data (data)
# It must return its computed data
########################################################################################################################

rFunction <- function(reference_time, data) {
  print(paste("Hello from co-pilot-r base-image. This file should be overwritten by the concrete MoveApps app.", reference_time))
  return(data)
}
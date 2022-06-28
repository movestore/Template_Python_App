########################################################################################################################
# RFunction.R
# This file is provided by the app developer. 
# It gets the configuration (reference_time) and the input-data (data)
# It must return its computed data
########################################################################################################################

library('move')
library('lubridate')

# Select year example
# The last parameter with the name data is the result of the previous app
rFunction = function(year, data) {
  print(paste("Will filter by given year", year))
  result <- data[year(data@timestamps) == year]
  
  pdf("/tmp/hello_world.pdf")
  plot(data,main="Hello World!")
  
  return(result)
}
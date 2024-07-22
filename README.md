# Name of App *(Give your app a short and informative title. Please adhere to our convention of Title Case without hyphens (e.g. My New App))*

MoveApps

Github repository: *github.com/yourAccount/Name-of-App* *(provide the link to the repository where the code of the App can be found)*

## Description
*Enter here the short description of the App that might also be used when filling out the description during App submission to MoveApps. This text is directly presented to Users that look through the list of Apps when compiling Workflows.*

## Documentation
*Enter here a detailed description of your App. What is it intended to be used for. Which steps of analyses are performed and how. Please be explicit about any detail that is important for use and understanding of the App and its outcomes. You might also refer to the sections below.*

### Application scope
#### Generality of App usability
*State here if the App was developed for a specific species, taxon or taxonomic group, or to answer a specific question. How might it influence the scope and utility of the App. This information will help the user to understand why the App might be producing no or odd results.*

*Examples:*

This App was developed using data of birds. 

This App was developed using data of red deer. 

This App was developed for any taxonomic group. 

This App was developed to identify kill sites, but can probably be used to identify any kind of location clusters like nests, dens or drinking holes.

#### Required data properties
*State here the required and/or optimal data properties for this App to perform properly.*

*Examples:*

This App is only applicable to data that reflect range resident behavior. 

The data should have a fix rate of at least 1 location per 30 minutes. 

The App should work for any kind of (location) data.

### Input type
*Indicate which type of input data the App requires.*

*Example*: `MovingPandas.TrajectoryCollection`

### Output type
*Indicate which type of output data the App produces to be passed on to subsequent Apps.*

*Example:* `MovingPandas.TrajectoryCollection`

### Artefacts
*If the App creates artefacts (e.g. csv, pdf, jpeg, shapefiles, etc), please list them here and describe each.*

*Example:* `rest_overview.csv`: csv-file with Table of all rest site properties

### Settings 
*Please list and define all settings/parameters that the App requires to be set by the App user, if necessary including their unit. Please first state the Setting name the user encounters in the Settings menu defined in the appspecs.json, and between brackets the argument used in the Python code to be able to identify it quickly in the code if needed.*

*Example:* `Radius of resting site` (radius): Defined radius the animal has to stay in for a given duration of time for it to be considered resting site. Unit: `metres`.

### Changes in output data
*Specify here how and if the App modifies the input data. Describe clearly what e.g. each additional column means.*

*Examples:*

The App adds to the input data the columns `Max_dist` and `Avg_dist`. They contain the maximum distance to the provided focal location and the average distance to it over all locations. 

The App filterers the input data as selected by the user. 

The output data is the outcome of the model applied to the input data. 

The input data remains unchanged.

### Most common errors
*Please describe shortly what most common errors of the App can be, how they occur and best ways of solving them.*

### Null or error handling
*Please indicate for each setting as well as the input data which behaviour the App is supposed to show in case of errors or NULL values/input. Please also add notes of possible errors that can happen if settings/parameters are improperly set and any other important information that you find the user should be aware of.*

*Example:* **Setting `radius`:** If no radius AND no duration are given, the input data set is returned with a warning. If no radius is given (NULL), but a duration is defined then a default radius of 1000m = 1km is set. 

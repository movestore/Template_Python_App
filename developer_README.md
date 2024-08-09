# MoveApps Python Software Development Kit (SDK)

This documentation provides a short introduction to the [MoveApps](https://www.moveapps.org) **Python SDK**.

As a first step, and before your read this, you should have used this GitHub template to create a copy of it in your personal space and named the repository as your App will be named in MoveApps.

# Overview

This template is designed according to a file structure that is necessary for your App to run in your local development environment similar to the way it will run in the MoveApps environment later. Please contain the structure and only change/add files as necessary for your App's functionality. See below which files can be changed and which should remain as is for simulation of the behaviour on MoveApps on your local system. A stepwise explanation below indicates the function and some background of each file and folder.

## File descriptions

1. `./app/app.py`: This is the entrypoint for your App logic. MoveApps will call this class during a workflow execution which includes your App.
**The class must be named `App` and the file must be named `./app/app.py`, do not alter it!**
1. `./appspec.json`: This file defines the settings and metadata of your App, for details refer to the [MoveApps User Manual](https://docs.moveapps.org/#/appspec)
1. `./environment.yml`: Definition of the dependencies of your App. We use `conda` as library manager.
1. `./resources/**`: Resources of the SDK
   1. `auxiliary/**`: Simulates the usage of [*auxiliary App files*](https://docs.moveapps.org/#/auxiliary). You can put files into this folder to simulate an App run with provided/user-uploaded files. 
   1. `output/**`: If your App produces [*artefacts*](https://docs.moveapps.org/#/copilot-r-sdk?id=artefacts) they will be stored here.
   1. `samples/**`: Collection of sample App input data. You can use these samples to simulate an App run with real input.
1. `./sdk/**`: The (internal) MoveApps Python SDK logic.
   1. `moveapps_execution.py`: The logic for simulating an App run.
   1. `moveapps_io.py`: Helper functions to use IO features of MoveApps.
   1. `moveapps_spec.py`: The python App specification each MoveApps Python App must implement
1. `./sdk.py`: The main entry point of the SDK. Use it to execute your App in your IDE
1. `./tests/**`: Location for **Unit Tests**

## SDK Runtime environment

Critical parts of the SDK can be adjusted by `environment variables`. 
Keep in mind that these variables are only changeable during App development and not during an App run on MoveApps.
They are predefined with sensible defaults - they should work for you as they are.

- `SOURCE_FILE`: path to input file for your App
- `CONFIGURATION_FILE`: configuration of your App (json - must correspondent with the `settings` of your `appspec.json`)
- `PRINT_CONFIGURATION`: prints the configuration your App receives
- `USER_APP_FILE_HOME_DIR`: home aka base directory of your local user App files (*auxiliary*)
- ~~`LOCAL_APP_FILES_DIR`~~: Deprecated! base directory of your local App files (*auxiliary*)
- `OUTPUT_FILE`: path to output file of your App
- `APP_ARTIFACTS_DIR`: base directory for writing App artifacts

You can adjust these environment variables by adjusting the file `./.env`.

## MoveApps App Bundle

Which files will be bundled into the final App running on MoveApps?

- everything in `./app/**`
- your conda environment definition `./environment.yml`
- all directories defined in your `appspec.json` at `providedAppFiles` 

Nothing else.


## Synchronization of your App repository with this template

This template includes a _GitHub action_ to keep your copy synchronized with the original template. Take a look at the [documentation](https://docs.moveapps.org/#/manage_Pyapp_github?id=keep-your-repositories-up-to-date-sync-with-templates) and make sure to keep your repository up-to-date.

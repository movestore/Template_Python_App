# MoveApps Python Software Development Kit (SDK)

This should give you a short introduction to the [MoveApps](https://www.moveapps.org) **Python SDK**.

At this point you should have forked this GitHub template to your personal space and named the repository as your app will be named in MoveApps.

# Overview

## File structure

```
.
├── app
│   └── app.py
├── appspec.json
├── environment.yml
├── resources
│   ├── local_app_files
│   ├── output
│   └── samples
│       └── input1.pickle
├── sdk
│   ├── moveapps_execution.py
│   ├── moveapps_io.py
│   └── moveapps_spec.py
├── sdk.py
├── tests
│   ├── app
│   │   └── test_app.py
│   └── resources
│       ├── app
│       │   └── input2.pickle
│       └── output
```

1. `./app/app.py`: This is the entrypoint for your app logic. MoveApps will call this class during a workflow execution which includes your app.
**The class must be named `App` and the file must be named `./app/app.py`**, do not alter it!
1. `./appspec.json`: This file defines metadata of your app, for details refer to the [MoveApps User Manual](https://docs.moveapps.org/#/appspec)
1. `./environment.yml`: Definition of the dependencies of your app. We use `conda` as library manager.
1. `./resources/**`: Resources of the SDK
   1. `local_app_files/**`: Simulates the usage of [*app files*](https://docs.moveapps.org/#/auxiliary). You can put files into this folder to simulate app run with provided/user-uploaded files. 
   1. `output/**`: If your app produces [*artefacts*](https://docs.moveapps.org/#/artefacts_appspec) they will be stored here.
   1. `samples/**`: Collection of sample app input data. You can use these samples to simulate a app run with real input
1. `./sdk/**`: The (internal) MoveApps Python SDK logic.
   1. `moveapps_execution.py`: The logic for simulating a app run
   1. `moveapps_io.py`: Helper functions to use IO features of MoveApps apps
   1. `moveapps_spec.py`: The python app specification each MoveApps Python App must implement
1. `./sdk.py`: The main entry point of the SDK. Use it to execute your app in your IDE
1. `./tests/**`: Location for **Unit Tests**

## SDK Runtime environment

Critical parts of the SDK can be adjusted by `environment variables`. 
Keep in mind that these variables are only changeable during app development and not during an app run on MoveApps.
They are predefined with sensible defaults - they should just work for you.

- `SOURCE_FILE`: path to input file for your app
- `CONFIGURATION_FILE`: configuration of your app (json - must correspondent with the `settings` of your `appspec.json`)
- `PRINT_CONFIGURATION`: prints the configuration your app receives
- `LOCAL_APP_FILES_DIR`: base directory of your local app files (*auxiliary*)
- `OUTPUT_FILE`: path to output file of your app
- `APP_ARTIFACTS_DIR`: base directory to for writing app artifacts

You can adjust these environment variables by adjusting the file `./.env`.

## MoveApps App Bundle

What will be bundled into the final app running on MoveApps?

- everything in `./app/**`
- your conda environment definition `./environment.yml`
- all directories defined in your `appspec.json` at `providedAppFiles` 

Nothing else.

## App development

1. create the conda environment by `conda env create -n APP_NAME --file environment.yml`
1. execute `python sdk.py`
1. ensure the sdk executes the vanilla template app code. Everything is set up correctly if no error occurs and you see something like _Welcome to the MoveApps Python SDK._
1. begin with your app development in `./app/app.py`

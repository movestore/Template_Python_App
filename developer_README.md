# MoveApps Python Software Development Kit (SDK)

This documentation provides a short introduction to the [MoveApps](https://www.moveapps.org ':ignore') **Python SDK**.

As a first step, and before your read this, you should have used this GitHub template to create a copy of it in your personal space and named the repository as your App will be named in MoveApps (please adhere to our convention of Title Case, e.g. My New App).

**The [MoveApps User Manual](https://docs.moveapps.org/#/create_py_app) provides a step-by-step explanation of how to create an App.** Please carefully follow these steps when creating a MoveApps App.


## Files in the SDK/template

This template is designed according to a file structure that is necessary for your App to run in your local development environment similar to the way it will run in the MoveApps environment later. Please contain the structure and only change/add files as necessary for your App's functionality. Take a look at the [overview image in the User Manual](https://docs.moveapps.org/#/create_py_app ':ignore') to see which files can be changed and which should remain as is for simulation of the behaviour on MoveApps on your local system.

Here you find an overview of the files and their function in the SDK.

1. `./app/app.py`: This is the entrypoint for your App logic. MoveApps will call this class during a Workflow execution which includes your App. The class must be named `App` and the file must be named `./app/app.py`, do not alter it. See [Step 4](https://docs.moveapps.org/#/create_py_app#step-4-develop-the-app-code-locally-within-the-template ':ignore') in the User Manual.
1. `./appspec.json`: This file defines the settings and metadata of your App. See [Step 6](https://docs.moveapps.org/#/create_py_app?id=step-6-write-app-specifications ':ignore') in the User Manual.
1. `./environment.yml`: Definition of the dependencies of your App. We use `conda` as library manager. See [Step 7](https://docs.moveapps.org/#/create_py_app?id=step-7-store-environment-dependencies ':ignore') in the User Manual.
1. `./resources/**`: Resources of the SDK
   1. `auxiliary/**`: Simulates the usage of [*auxiliary files*](https://docs.moveapps.org/#/auxiliary ':ignore'). You can put files into this folder to simulate an App run with provided/user-uploaded files. 
   1. `output/**`: If your App produces output files (artifacts) they will be stored here. See [*producing artifacts*](https://docs.moveapps.org/#/copilot-python-sdk?id=producing-app-artifacts ':ignore') for more information.
   1. `samples/**`: Collection of sample App input data. You can use these samples to simulate an App run with real input.
1. `./sdk/**`: The (internal) MoveApps Python SDK logic.
   1. `moveapps_execution.py`: The logic for simulating an App run.
   1. `moveapps_io.py`: Helper functions to use IO features of MoveApps.
   1. `moveapps_spec.py`: The Python App specification each MoveApps Python App must implement
1. `./sdk.py`: The main entry point of the SDK. Use it to execute your App in your compiler.
1. `./tests/**`: Location for *Unit Tests*. See [Step 5](https://docs.moveapps.org/#/create_py_app#=step-5-test-your-app-locally ':ignore') of the User Manual.


## SDK Runtime environment

Critical parts of the SDK can be adjusted by `environment variables`. Keep in mind that these variables are only changeable during App development and not during an App run on MoveApps. They are predefined with sensible defaults - they should work for you as they are.

- `SOURCE_FILE`: path to the input file for your App.
- `CONFIGURATION_FILE`: path to the configuration/settings file of your App (in [JSON](https://www.w3schools.com/js/js_json_intro.asp) format - must correspondent with the `settings` of your `appspec.json`, see [MoveApps parameters](https://docs.moveapps.org/#/copilot-python-sdk.md#moveapps-parameters ':ignore') for an example of the `app-configuration.json` file).

You can adjust these environment variables by adjusting the file `./.env`.


## MoveApps App Bundle

Which files will be bundled into the final App running on MoveApps?

- everything in `./app/**`
- your conda environment definition `./environment.yml`
- all directories defined in your `appspec.json` at `providedAppFiles` 

Nothing else.


## Synchronization of your App repository with this template

This template includes a _GitHub action_ to keep your copy synchronized with the original template. Take a look at the [documentation](https://docs.moveapps.org/#/manage_Pyapp_github#keep-your-repositories-up-to-date-sync-with-templates) and make sure to keep your repository up-to-date.

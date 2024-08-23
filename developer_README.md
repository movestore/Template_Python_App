# MoveApps Python Software Development Kit (SDK)

This documentation provides a short introduction to the [MoveApps](https://www.moveapps.org) **Python SDK**.

As a first step, and before your read this, you should have used this GitHub template to create a copy of it in your personal space and named the repository as your App will be named in MoveApps (please adhere to our convention of Title Case, e.g. My New App).

**The [MoveApps User Manual](https://docs.moveapps.org/#/create_py_app) provides a step-by-step explanation of how to create an App.** Please carefully follow these steps when creating a MoveApps App.


## Files in the SDK/template

This template is designed according to a file structure that is necessary for your App to run in your local development environment similar to the way it will run in the MoveApps environment later. Please contain the structure and only change/add files as necessary for your App's functionality. Take a look at the [overview image in the User Manual](https://docs.moveapps.org/#/create_py_app) to see which files can be changed and which should remain as is for simulation of the behaviour on MoveApps on your local system.

Here you find an overview of the files and their function in the SDK:

1. `./app/app.py`: must be modified by the developer. This is the entrypoint for your App logic. MoveApps will call this class during a Workflow execution which includes your App. The class must be named `App` and the file must be named `./app/app.py`, do not alter it. See [Step 4](https://docs.moveapps.org/#/create_py_app#step-4-develop-the-app-code-locally-within-the-template) in the User Manual.
1. `./appspec.json`: must be modified by the developer. This file defines the settings and metadata of your App. See [Step 6](https://docs.moveapps.org/#/create_py_app?id=step-6-write-app-specifications) in the User Manual.
1. `./environment.yml`: must be modified by the developer. Definition of the dependencies of your App. We use `conda` as library manager. See [Step 7](https://docs.moveapps.org/#/create_py_app?id=step-7-store-environment-dependencies) in the User Manual.
1. `./README.md`: must be modified by the developer. Provided template for the documentation of the App (see [Step 8](https://docs.moveapps.org/#/create_py_app?id=step-8-write-a-documentation-file) in the User Manual).
1. `./tests/**`: must be modified by the developer. Location for *Unit Tests*. See [Step 5](https://docs.moveapps.org/#/create_py_app#=step-5-test-your-app-locally) of the User Manual.
1. `./sdk.py`: use for App testing. The main entrypoint of the SDK. Use it to execute your App in your compiler (e.g. PyCharm).
1. `./app-configuration.json`: adjust for App testing. The configuration/settings file of your App (in [JSON](https://www.w3schools.com/js/js_json_intro.asp) format - must correspondent with the `settings` of your `appspec.json`, see [MoveApps parameters](https://docs.moveapps.org/#/copilot-python-sdk.md#moveapps-parameters) for an example).
1. `.env`: adjust for App testing. defining the SDK Runtime environment, see below.
1. `./resources/**`: use for App testing. Resources of the SDK
   1. `auxiliary/**`: Simulates the usage of [*auxiliary files*](https://docs.moveapps.org/#/auxiliary). You can put files into this folder to simulate an App run with provided/user-uploaded files. 
   1. `output/**`: The output data (`output.pickle`) that will be passed on to the next App in a Workflow and other output files (artifacts) that your App may produce will be stored here. See [*producing artifacts*](https://docs.moveapps.org/#/copilot-python-sdk?id=producing-artifacts) for more information.
   1. `samples/**`: Collection of sample App input data. You can use these data to test an App run with real input.


## SDK runtime environment

Critical parts of the SDK can be adjusted by `environment variables`. Keep in mind that these variables are only changeable during App development and not during an App run on MoveApps. They are predefined with sensible defaults - they should work for you as they are.  While testing your App you will want to modify the SOURCE_FILE variable to either call the different example data sets provided in the template or other data sets that you want to use to test your App.

- `SOURCE_FILE`: path to the input file for your App.
- `CONFIGURATION_FILE`: path to the configuration/settings file of your App (in [JSON](https://www.w3schools.com/js/js_json_intro.asp) format - must correspondent with the `settings` of your `appspec.json`, see [MoveApps parameters](https://docs.moveapps.org/#/copilot-python-sdk.md#moveapps-parameters) for an example of the `app-configuration.json` file).

You can adjust these environment variables by adjusting the file `./.env`.


## MoveApps App Bundle

Which files will be bundled into the final App running on MoveApps?

- everything in `./app/**`
- your conda environment definition `./environment.yml`
- all directories defined in your `appspec.json` at `providedAppFiles` 
- the file ./appspec.json will be used to build and create the metadata of your App
- the file ./README.md will be reference to for the documentation of your App

Nothing else.


## Synchronization of your App repository with this template

This template includes a _GitHub action_ to keep your copy synchronized with the original template. Take a look at the [documentation](https://docs.moveapps.org/#/manage_Pyapp_github#keep-your-repositories-up-to-date-sync-with-templates) and make sure to keep your repository up-to-date.

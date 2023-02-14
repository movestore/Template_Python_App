# MoveApps Python Software Development Kit (SDK)

This documentation provides a short introduction to the [MoveApps](https://www.moveapps.org) **Python SDK**.

As a first step, and before your read this, you should have forked this GitHub template to your personal space and named the repository as your App will be named in MoveApps.

# Overview

This template is designed according to a file structure that is necessary for your App to run in your local development environment similar to the way it will run in the MoveApps environment later. Please contain the structure and only change/add files as necessary for your App's functionality. See below which files can be changed and which should remain as is for simulation of the behaviour on MoveApps on your local system. A stepwise explanation below indicates the function and some of its background of each file and folder.

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

1. `./app/app.py`: This is the entrypoint for your App logic. MoveApps will call this class during a workflow execution which includes your app.
**The class must be named `App` and the file must be named `./app/app.py`**, do not alter it!
1. `./appspec.json`: This file defines the settings and metadata of your App, for details refer to the [MoveApps User Manual](https://docs.moveapps.org/#/appspec)
1. `./environment.yml`: Definition of the dependencies of your App. We use `conda` as library manager.
1. `./resources/**`: Resources of the SDK
   1. `local_app_files/**`: Simulates the usage of [*app files*](https://docs.moveapps.org/#/auxiliary). You can put files into this folder to simulate an App run with provided/user-uploaded files. 
   1. `output/**`: If your App produces [*artefacts*](https://docs.moveapps.org/#/copilot-r-sdk?id=artefacts) they will be stored here.
   1. `samples/**`: Collection of sample App input data. You can use these samples to simulate a App run with real input.
1. `./sdk/**`: The (internal) MoveApps Python SDK logic.
   1. `moveapps_execution.py`: The logic for simulating an App run.
   1. `moveapps_io.py`: Helper functions to use IO features of MoveApps Apps.
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
- `LOCAL_APP_FILES_DIR`: base directory of your local App files (*auxiliary*)
- `OUTPUT_FILE`: path to output file of your App
- `APP_ARTIFACTS_DIR`: base directory for writing App artifacts

You can adjust these environment variables by adjusting the file `./.env`.

## MoveApps App Bundle

Which files will be bundled into the final App running on MoveApps?

- everything in `./app/**`
- your conda environment definition `./environment.yml`
- all directories defined in your `appspec.json` at `providedAppFiles` 

Nothing else.

## App development

1. Create the conda environment by `conda env create -n APP_NAME --file environment.yml`
1. Execute `python sdk.py`
1. Ensure the sdk executes the vanilla template app code. Everything is set up correctly if no error occurs and you see something like _Welcome to the MoveApps Python SDK._
1. Begin with your app development in `./app/app.py`

## Examples

### Request App configuration from your users

`./appspec.json`: define the settings UI on MoveApps. Users of your App can enter their configuration values.

```
"settings": [
 {
   "id": "line_width",
   "name": "Line width",
   "description": "The width of the lines in the plot.",
   "defaultValue": 2,
   "type": "INTEGER"
 },
 {
   "id": "legend",
   "name": "Include legend?",
   "description": "Should the plot contain a legend?",
   "defaultValue": false,
   "type": "CHECKBOX"
 }
],
```

`./app-configuration.json`: this is only needed during the app development to simulate an App run

```
{
  "line_width": 2,
  "legend": true
}
```

`./app/app.py`: your App will be called with the user's App configuration

```
@dataclass
class AppConfig:
    line_width: int
    with_legend: bool

class App(object):
   @staticmethod
    def map_config(config: dict):
        return AppConfig(
            line_width=config['line_width'] if 'line_width' in config else 5,
            with_legend=config['legend'] if 'legend' in config else False
        )
   
    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        app_config = self.map_config(config=config)
        # [..]
```

`./tests/app/test_app.py`: do not forget to test your App

```
def test_app_config_mapping_defaults(self):
   # prepare
   config = {}

   # execute
   actual = self.sut.map_config(config=config)

   # verify
   self.assertEqual(5, actual.line_width)
   self.assertFalse(actual.with_legend)
```

### Produce an App artefact

Your App can write files which the user can download after it has run.

`./appspec.json`

```
  "createsArtifacts": true,
```

`./app/app.py`

```
plot = data.plot(
   column="speed",
   linewidth=app_config.line_width,
   capstyle='round',
   legend=app_config.with_legend
)
plot.figure.savefig(self.moveapps_io.create_artifacts_file('plot.png'))
```

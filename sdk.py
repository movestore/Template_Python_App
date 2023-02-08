import pluggy
import pandas as pd
import json
import os
import logging
from co_pilot.co_pilot_spec import CoPilotSpec, HOOK_NAMESPACE
from co_pilot.moveapps_io import MoveAppsIo

PROJECT_NAME = "co-pilot-python"


class CoPilotPythonSdk:

    def __init__(self, active_hooks=None) -> None:
        """
        Setup the plugin manager and register all the hooks.
        """
        self._pm = pluggy.PluginManager(HOOK_NAMESPACE)
        self._pm.add_hookspecs(CoPilotSpec)
        self.hooks = active_hooks
        if self.hooks:
            for hook in self.hooks:
                self._pm.register(hook)

    def sdk_run(self):
        self.configure_logging()
        config = self.load_config()
        data = self.load_input()
        output = self.moveapps_run(data, config)
        self.store_output(output)

    @staticmethod
    def configure_logging():
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    @staticmethod
    def load_input():
        return pd.read_pickle(os.environ.get('SOURCE_FILE', 'resources/samples/input1.pickle'))

    @staticmethod
    def load_config():
        config = os.environ.get('CONFIGURATION', '{}')
        parsed = json.loads(config)
        if os.environ.get("PRINT_CONFIGURATION", "no") == "yes":
            logging.info(f'app will be started with configuration: {parsed}')
        return parsed

    @staticmethod
    def store_output(data):
        logging.info(f'storing output: {data}')
        pd.to_pickle(data, os.environ.get('OUTPUT_FILE', 'resources/output/output.pickle'))

    def moveapps_run(self, data, config):
        outputs = self._pm.hook.execute(data=data, config=config)
        return outputs[0]


if __name__ == "__main__":
    from app.app import App
    # LIFO
    hooks = [App(moveapps_io=MoveAppsIo())]
    sdk = CoPilotPythonSdk(active_hooks=hooks)
    sdk.sdk_run()

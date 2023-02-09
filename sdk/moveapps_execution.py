import pandas as pd
import json
import os
import logging
import pluggy
from dotenv import load_dotenv


class MoveAppsExecutor:

    def __init__(self, plugin_manager: pluggy.PluginManager):
        load_dotenv()
        self._pm = plugin_manager

    def execute(self):
        self.configure_logging()
        config = self.load_config()
        data = self.load_input()
        output = self.call_app(data, config)
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
        if os.environ['CONFIGURATION_FILE']:
            with open(os.environ['CONFIGURATION_FILE']) as config_file:
                parsed = json.load(config_file)
        else:
            config = os.environ.get('CONFIGURATION', '{}')
            parsed = json.loads(config)
        if os.environ.get("PRINT_CONFIGURATION", "no") == "yes":
            logging.info(f'app will be started with configuration: {parsed}')
        return parsed

    @staticmethod
    def store_output(data):
        logging.info(f'storing output: {data}')
        pd.to_pickle(data, os.environ.get('OUTPUT_FILE', 'resources/output/output.pickle'))

    def call_app(self, data, config):
        outputs = self._pm.hook.execute(data=data, config=config)
        return outputs[0]

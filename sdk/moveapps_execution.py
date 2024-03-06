import pandas as pd
import json
import os
import logging
import pluggy
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Environment:
    source_file: str
    output_file: str
    error_file: str
    app_configuration: dict


class MoveAppsExecutor:

    def __init__(self, plugin_manager: pluggy.PluginManager):
        load_dotenv()
        self._pm = plugin_manager

    def execute(self):
        try:
            self.__configure_logging()
            self.__load_environment()
            data = self.__load_input()
            output = self.__call_app(data)
            self.__store_output(output)
        except Exception as exception:
            self.__store_error(exception)
            raise exception

    def __load_environment(self):
        self.env = Environment(
            source_file=os.environ.get('SOURCE_FILE'),
            output_file=os.environ.get('OUTPUT_FILE', 'resources/output/output.pickle'),
            error_file=os.environ.get('ERROR_FILE', 'resources/output/error.txt'),
            app_configuration=self.__load_config()
        )

    @staticmethod
    def __configure_logging():
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def __load_input(self):
        return pd.read_pickle(self.env.source_file)

    @staticmethod
    def __load_config():
        if 'CONFIGURATION_FILE' in os.environ:
            with open(os.environ['CONFIGURATION_FILE']) as config_file:
                parsed = json.load(config_file)
        else:
            config = os.environ.get('CONFIGURATION', '{}')
            parsed = json.loads(config)
        if os.environ.get("PRINT_CONFIGURATION", "no") == "yes":
            logging.info(f'app will be started with configuration: {parsed}')
        return parsed

    def __store_output(self, data):
        logging.info(f'storing output: {data}')
        pd.to_pickle(data, self.env.output_file)

    def __store_error(self, error: Exception):
        logging.info(f'storing error to {self.env.error_file}')
        with open(self.env.error_file, 'w') as error_file:
            error_file.write(error.__str__())

    def __call_app(self, data):
        outputs = self._pm.hook.execute(data=data, config=self.env.app_configuration)
        return outputs[0]

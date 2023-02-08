from sdk.moveapps_spec import hook_impl
from movingpandas import TrajectoryCollection
import logging


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        logging.debug('your app code goes here')
        # return some useful data for next apps in the workflow
        return data

import unittest
import os
from tests.config.definitions import ROOT_DIR
from app.app import App
from sdk.moveapps_io import MoveAppsIo
import pandas as pd
import movingpandas as mpd


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        os.environ['APP_ARTIFACTS_DIR'] = os.path.join(ROOT_DIR, 'tests/resources/output')
        self.sut = App(moveapps_io=MoveAppsIo())

    def test_app_runs(self):
        # prepare
        data: mpd.TrajectoryCollection = pd.read_pickle(os.path.join(ROOT_DIR, 'tests/resources/app/input4_LatLon.pickle'))
        config: dict = {
            "year": 2014
        }

        # execute
        self.sut.execute(data=data, config=config)

    def test_app_config(self):
        # prepare
        config = {
            "year": 2014
        }

        # execute
        actual = config

        # verify
        self.assertEqual(2014, actual["year"])

    def test_year_present(self):
        # prepare input data
        df = pd.DataFrame([
            {'timestamp_utc': "2001-06-11 09:00:00", 'coords_x': 1, 'coords_y': 5, 'track_id': 'ID_1'},
            {'timestamp_utc': "2001-07-12 09:00:00", 'coords_x': 2, 'coords_y': 4, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-08-13 09:00:00", 'coords_x': 3, 'coords_y': 3, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-09-14 09:00:00", 'coords_x': 4, 'coords_y': 2, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-10-15 09:00:00", 'coords_x': 5, 'coords_y': 1, 'track_id': 'ID_1'},
            {'timestamp_utc': "2000-06-11 09:00:00", 'coords_x': 1, 'coords_y': 5, 'track_id': 'ID_2'},
            {'timestamp_utc': "2000-07-12 09:00:00", 'coords_x': 2, 'coords_y': 4, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-08-13 09:00:00", 'coords_x': 3, 'coords_y': 3, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-09-14 09:00:00", 'coords_x': 4, 'coords_y': 2, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-10-15 09:00:00", 'coords_x': 5, 'coords_y': 1, 'track_id': 'ID_2'}
        ])
        input = mpd.TrajectoryCollection(
            df,
            traj_id_col='track_id',
            t='timestamp_utc',
            crs='epsg:4326',
            x='coords_x', y='coords_y'
        )

        # prepare configuration
        config = {
            "year": 2001
        }

        # prepare expected data
        df_e = pd.DataFrame([
            {'timestamp_utc': "2001-06-11 09:00:00", 'coords_x': 1, 'coords_y': 5, 'track_id': 'ID_1'},
            {'timestamp_utc': "2001-07-12 09:00:00", 'coords_x': 2, 'coords_y': 4, 'track_id': 'ID_1'},
            {'timestamp_utc': "2001-08-13 09:00:00", 'coords_x': 3, 'coords_y': 3, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-09-14 09:00:00", 'coords_x': 4, 'coords_y': 2, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-10-15 09:00:00", 'coords_x': 5, 'coords_y': 1, 'track_id': 'ID_2'}
        ])
        expected = mpd.TrajectoryCollection(
            df_e,
            traj_id_col='track_id',
            t='timestamp_utc',
            crs='epsg:4326',
            x='coords_x', y='coords_y'
        )

        # execute
        actual = self.sut.execute(data=input, config=config)

        # verify timestamps
        self.assertEqual(actual.to_point_gdf().index.strftime("%Y-%m-%d %H:%M:%S").tolist(),expected.to_point_gdf().index.strftime("%Y-%m-%d %H:%M:%S").tolist())

        # verify track ids
        self.assertEqual(actual.to_point_gdf()[actual.get_traj_id_col()].unique().tolist(), expected.to_point_gdf()[expected.get_traj_id_col()].unique().tolist())

    def test_year_not_present(self):
        # prepare input data
        df = pd.DataFrame([
            {'timestamp_utc': "2001-06-11 09:00:00", 'coords_x': 1, 'coords_y': 5, 'track_id': 'ID_1'},
            {'timestamp_utc': "2001-07-12 09:00:00", 'coords_x': 2, 'coords_y': 4, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-08-13 09:00:00", 'coords_x': 3, 'coords_y': 3, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-09-14 09:00:00", 'coords_x': 4, 'coords_y': 2, 'track_id': 'ID_1'},
            {'timestamp_utc': "2002-10-15 09:00:00", 'coords_x': 5, 'coords_y': 1, 'track_id': 'ID_1'},
            {'timestamp_utc': "2000-06-11 09:00:00", 'coords_x': 1, 'coords_y': 5, 'track_id': 'ID_2'},
            {'timestamp_utc': "2000-07-12 09:00:00", 'coords_x': 2, 'coords_y': 4, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-08-13 09:00:00", 'coords_x': 3, 'coords_y': 3, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-09-14 09:00:00", 'coords_x': 4, 'coords_y': 2, 'track_id': 'ID_2'},
            {'timestamp_utc': "2001-10-15 09:00:00", 'coords_x': 5, 'coords_y': 1, 'track_id': 'ID_2'}
        ])
        input = mpd.TrajectoryCollection(
            df,
            traj_id_col='track_id',
            t='timestamp_utc',
            crs='epsg:4326',
            x='coords_x', y='coords_y'
        )

        # prepare configuration
        config = {
            "year": 2100
        }

        # execute
        actual = self.sut.execute(data=input, config=config)

        # verify
        self.assertIsNone(actual)

    """
    # Use this test if the App should return the input data
    def test_app_returns_input(self):
        # prepare
        expected: mpd.TrajectoryCollection = pd.read_pickle(os.path.join(ROOT_DIR, 'tests/resources/app/input2_LatLon.pickle'))
        config: dict = {}

        # execute
        actual = self.sut.execute(data=expected, config=config)

        # verif
        self.assertEqual(expected, actual)
    """

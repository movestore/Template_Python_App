import os
from unittest import TestCase
from tests.config.definitions import ROOT_DIR
from sdk.moveapps_io import MoveAppsIo


class TestMoveAppsIo(TestCase):

    def setUp(self) -> None:
        self.sut = MoveAppsIo()

    def test_create_artifacts_file(self):
        # execute
        actual = self.sut.create_artifacts_file('artifact-file.xyz')

        # verify
        self.assertEqual(os.path.join(ROOT_DIR, 'tests/resources/output/artifact-file.xyz'), actual)

    def test_get_app_file_path_provided_only(self):
        # prepare
        os.environ['LOCAL_APP_FILES_DIR'] = os.path.join(ROOT_DIR, 'tests/resources/local_app_files/provided_only')

        # execute
        actual = self.sut.get_app_file_path('config-id')

        # verify
        expected_file = os.listdir(actual)[0]
        self.assertEqual('expected', expected_file)

    def test_get_app_file_path_uploaded_only(self):
        # prepare
        os.environ['LOCAL_APP_FILES_DIR'] = os.path.join(ROOT_DIR, 'tests/resources/local_app_files/uploaded_only')

        # execute
        actual = self.sut.get_app_file_path('config-id')

        # verify
        expected_file = os.listdir(actual)[0]
        self.assertEqual('expected', expected_file)

    def test_get_app_file_path_provided_and_uploaded(self):
        # prepare
        os.environ['LOCAL_APP_FILES_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/local_app_files/provided_and_uploaded')

        # execute
        actual = self.sut.get_app_file_path('config-id')

        # verify
        expected_file = os.listdir(actual)[0]
        self.assertEqual('expected', expected_file)

    def test_get_app_file_path_nothing(self):
        # prepare
        os.environ['LOCAL_APP_FILES_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/local_app_files/nothing')

        # execute
        actual = self.sut.get_app_file_path('any')

        # verify
        self.assertIsNone(actual)

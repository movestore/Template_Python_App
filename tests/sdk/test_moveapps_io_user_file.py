import os
from unittest import TestCase
from tests.config.definitions import ROOT_DIR
from sdk.moveapps_io import MoveAppsIo


class TestMoveAppsIo(TestCase):

    def setUp(self) -> None:
        self.sut = MoveAppsIo()

    def test_get_user_app_file_path_provided_only(self):
        # prepare
        os.environ['USER_APP_FILE_HOME_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/auxiliary/local-app-files/provided_only')

        # execute
        actual = self.sut.get_auxiliary_file_path('config-id')

        # verify
        self.assertEqual(
            os.path.join(
                ROOT_DIR,
                'tests/resources/auxiliary/local-app-files/provided_only',
                'provided-app-files',
                'config-id',
                'expected'
            ),
            actual
        )

    def test_get_user_app_file_path_uploaded_only(self):
        # prepare
        os.environ['USER_APP_FILE_HOME_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/auxiliary/local-app-files/uploaded_only')

        # execute
        actual = self.sut.get_auxiliary_file_path('config-id')

        # verify
        self.assertEqual(
            os.path.join(
                ROOT_DIR,
                'tests/resources/auxiliary/local-app-files/uploaded_only',
                'uploaded-app-files',
                'config-id',
                'expected'
            ),
            actual
        )

    def test_get_user_app_file_path_provided_and_uploaded(self):
        # prepare
        os.environ['USER_APP_FILE_HOME_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/auxiliary/local-app-files/provided_and_uploaded')

        # execute
        actual = self.sut.get_auxiliary_file_path('config-id')

        # verify
        self.assertEqual(
            os.path.join(
                ROOT_DIR,
                'tests/resources/auxiliary/local-app-files/provided_and_uploaded',
                'uploaded-app-files',
                'config-id',
                'expected'
            ),
            actual
        )

    def test_get_user_app_file_path_nothing(self):
        # prepare
        os.environ['USER_APP_FILE_HOME_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/auxiliary/local-app-files/nothing')

        # execute
        actual = self.sut.get_auxiliary_file_path('any')

        # verify
        self.assertIsNone(actual)

    def test_get_user_app_file_path_unexpected_number_of_files(self):
        # prepare
        os.environ['USER_APP_FILE_HOME_DIR'] = \
            os.path.join(ROOT_DIR, 'tests/resources/auxiliary/user-files/unexpected-number')

        # execute
        actual = self.sut.get_auxiliary_file_path('config-id')

        # verify
        self.assertIsNone(actual)

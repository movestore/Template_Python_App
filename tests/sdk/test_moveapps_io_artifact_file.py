import os
from unittest import TestCase
from tests.config.definitions import ROOT_DIR
from sdk.moveapps_io import MoveAppsIo


class TestMoveAppsIo(TestCase):

    def setUp(self) -> None:
        os.environ['APP_ARTIFACTS_DIR'] = os.path.join(ROOT_DIR, 'tests/resources/output')
        self.sut = MoveAppsIo()

    def test_create_artifacts_file(self):
        # execute
        actual = self.sut.create_artifacts_file('artifact-file.xyz')

        # verify
        self.assertEqual(
            os.path.join(
                ROOT_DIR,
                'tests/resources/output',
                'artifact-file.xyz'
            ),
            actual
        )

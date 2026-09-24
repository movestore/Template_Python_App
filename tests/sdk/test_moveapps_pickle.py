import os
import tempfile
from unittest import TestCase

import pandas as pd

from sdk.moveapps_pickle import MoveAppsPickle
from tests.config.definitions import ROOT_DIR


class TestMoveAppsPickle(TestCase):
    """
    MoveApps hands the App its input and output paths without a file extension, so none of these
    cases may rely on the file name to tell compressed from uncompressed data.
    """

    def setUp(self) -> None:
        self.sut = MoveAppsPickle()
        self.tmp = tempfile.TemporaryDirectory()
        self.data = pd.DataFrame({'id': range(5_000), 'note': ['a note about this record'] * 5_000})

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def path(self, file_name: str) -> str:
        return os.path.join(self.tmp.name, file_name)

    def test_writes_compressed_although_the_file_name_has_no_extension(self):
        # prepare
        target = self.path('output_file')

        # execute
        self.sut.write(data=self.data, path=target)

        # verify
        with open(target, 'rb') as written:
            actual = written.read(2)
        self.assertEqual(b'\x1f\x8b', actual)

    def test_written_output_is_substantially_smaller_than_uncompressed(self):
        # prepare
        compressed = self.path('compressed')
        uncompressed = self.path('uncompressed')
        pd.to_pickle(self.data, uncompressed, compression=None)

        # execute
        self.sut.write(data=self.data, path=compressed)

        # verify
        actual = os.path.getsize(compressed)
        self.assertLess(actual, os.path.getsize(uncompressed) / 2)

    def test_reads_back_what_it_wrote(self):
        # prepare
        target = self.path('output_file')
        self.sut.write(data=self.data, path=target)

        # execute
        actual = self.sut.read(path=target)

        # verify
        pd.testing.assert_frame_equal(self.data, actual)

    def test_reads_an_uncompressed_pickle_written_by_an_older_sdk(self):
        # prepare: Apps built against an SDK before v3 wrote uncompressed pickles, and such output
        # can still reach a current App as its input.
        legacy = self.path('output_file')
        pd.to_pickle(self.data, legacy, compression=None)

        # execute
        actual = self.sut.read(path=legacy)

        # verify
        pd.testing.assert_frame_equal(self.data, actual)

    def test_reads_a_sample_file_carrying_a_gz_extension(self):
        # prepare: during App development the SDK is pointed at the shipped samples via `SOURCE_FILE`
        sample = os.path.join(ROOT_DIR, 'tests/resources/app/input4_LatLon.pickle.gz')

        # execute
        actual = self.sut.read(path=sample)

        # verify
        self.assertIsNotNone(actual)

    def test_detects_gzip_by_content(self):
        # prepare
        compressed = self.path('compressed')
        pd.to_pickle(self.data, compressed, compression='gzip')

        # execute
        actual = self.sut.detect_compression(path=compressed)

        # verify
        self.assertEqual('gzip', actual)

    def test_detects_absence_of_compression_by_content(self):
        # prepare
        uncompressed = self.path('uncompressed')
        pd.to_pickle(self.data, uncompressed, compression=None)

        # execute
        actual = self.sut.detect_compression(path=uncompressed)

        # verify: `None` is what pandas expects for "do not decompress"
        self.assertIsNone(actual)

import logging

import pandas as pd

GZIP_MAGIC = b'\x1f\x8b'


class MoveAppsPickle:
    """
    Reads and writes the pickle files that carry the data from one App to the next.

    MoveApps dictates the input and output paths and they carry no file extension, so pandas cannot
    infer the compression from the file name. Writing therefore states the compression explicitly,
    and reading determines it from the file content.
    """

    @staticmethod
    def read(path: str):
        """
        Reads a pickle, compressed or not.

        Apps built against an SDK before `v3` write uncompressed pickles, and such output can still
        reach a current App as its input. Both flavours therefore have to stay readable.

        :param path: path to the pickle to read
        :return: the unpickled data
        """
        compression = MoveAppsPickle.detect_compression(path=path)
        logging.info(f'reading pickle \'{path}\' (compression: {compression})')
        return pd.read_pickle(path, compression=compression)

    @staticmethod
    def write(data, path: str) -> None:
        """
        Writes a gzip-compressed pickle, whatever the file is named.

        :param data: the data to pickle
        :param path: path to write the pickle to
        """
        pd.to_pickle(data, path, compression='gzip')

    @staticmethod
    def detect_compression(path: str) -> str | None:
        """
        Determines the compression of a pickle from its first bytes instead of from its name.

        :param path: path to the pickle to inspect
        :return: `'gzip'` for a gzip-compressed file, otherwise `None`, which is how pandas is told
            not to decompress at all
        """
        with open(path, 'rb') as probe:
            return 'gzip' if probe.read(len(GZIP_MAGIC)) == GZIP_MAGIC else None

import os
import pandas as pd
import movingpandas as mpd
from tests.config.definitions import ROOT_DIR


class InputConverter:

    def csv_to_pickle(self, csv_path, result_file_name):
        print(os.getcwd())

        pandas = self.read_data_csv(file_path=f'{csv_path}/link.csv')
        timezone = self.read_timezone(file_path=f'{csv_path}/meta.csv')
        projection = self.read_projection(file_path=f'{csv_path}/meta.csv')

        self.adjust_timestamps(data=pandas, timezone=timezone)
        movingpandas = self.create_moving_pandas(data=pandas, projection=projection)
        self.write_result(file_name=result_file_name, data=movingpandas)

    def read_data_csv(self, file_path):
        csv = pd.read_csv(
            file_path,
            parse_dates=['timestamps'],
        )
        print(csv.info())
        return csv

    def read_timezone(self, file_path):
        meta_csv = pd.read_csv(file_path)
        tzone = meta_csv['tzone'][0]
        return tzone

    def read_projection(self, file_path):
        meta_csv = pd.read_csv(file_path)
        projection = meta_csv['crs'][0]
        return projection

    def adjust_timestamps(self, data, timezone):
        data['timestamp_tz'] = data['timestamps'].apply(lambda x: x.tz_localize(timezone))
        print('applied timezone', timezone)
        print(data.head())

    def create_moving_pandas(self, data, projection):
        move = mpd.TrajectoryCollection(
            data,
            traj_id_col='trackId',
            crs=projection,
            t='timestamp_tz',  # use our converted timezone column
            x='location.long',
            y='location.lat'
        )
        print(move)
        return move

    def write_result(self, file_name, data):
        print(type(data))
        pd.to_pickle(data, file_name)


if __name__ == '__main__':
    converter = InputConverter()
    for i in range(1,5):
        file = f'input{i}'
        converter.csv_to_pickle(
            csv_path=f'./resources/input/{file}',
            result_file_name=f'{ROOT_DIR}/resources/samples/{file}.pickle'
        )

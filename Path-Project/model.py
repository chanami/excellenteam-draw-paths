import pandas as pd


class Model:

    def __init__(self, file_name):
        self.df = self.load_pickle(file_name)

    # def load_csv(self, csv_file):
    #     # TODO - load csv file
    #     self.convert_csv_to_pickle(csv_file)
    #
    # def convert_csv_to_pickle(self, csv_file):
    #     # TODO - convert
    #     self.load_pickle(csv_file)

    def load_pickle(self, pickle_file):
        print('WORK!!!')
        return pd.read_pickle(pickle_file)

    def get_df(self):
        return self.df

    def draw(self):
        pass

    def filter_by_hours(self, from_hour, to_hour):
        pass

    def filter_by_date_and_hour(self, from_hour, to_hour, date):
        pass

    def filter_by_area(self, point1, point2):
        pass

    def filter_by_areas(self, *squares):
        pass

    def apply_filters(self):
        pass


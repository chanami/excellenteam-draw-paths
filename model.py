import pandas as pd


class Model:
    def __init__(self):
        print("in model init")
        self.df = self.load_pickle('data/paths.pkl.xz')

    # def load_csv(self, csv_file):
    #     # T
    #     self.convert_csv_to_pickle(csv_file)
    #
    # def convert_csv_to_pickle(self, csv_file):
    #     self.load_pickle(csv_file)

    def load_pickle(self, pickle_file):
        return pd.read_pickle(pickle_file)

    def filter_by_hours(self, begin, end):
        objs = self.df.groupby(["filename", "obj"]).agg({'time': ['min', 'max']})

        begin_time = pd.to_datetime(begin).time()
        end_time = pd.to_datetime(end).time()
        min = objs.time['min'].dt.time  # objs[('time','min')]
        max = objs.time['max'].dt.time  # objs[('time','max')]
        # print(min, max)
        items = objs[(min.between(begin_time, end_time)) | ((min < begin_time) & (max > begin_time))]
        # print(items)
        return items

    def filter_by_date_and_hour(self, from_hour, to_hour, date):
        pass

    def filter_by_area(self, point1, point2):
        pass

    def filter_by_areas(self, *squares):
        pass

    def apply_filters(self):
        pass

    def filter_by_areas(self, *squares):
        pass

    def apply_filters(self):
        pass


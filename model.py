import pandas as pd
from pylab import imread
import csv


class Model:
    def set_file(self, file, pic):
        self.img = imread(pic)
        self.df = self.load_file(file)  # 'data/paths.pkl.xz' pd.read_pickle('data/paths.pkl.xz')  #
        self.index_file = self.df.set_index(['filename', 'obj']).sort_index()
        self.df = self.index_file
        self.last = self.index_file  # self.df

    def reset(self):
        self.last = self.df

    def load_file(self, file):
        if file[-4:] == ".csv":
            fixed_file = self.fix_csv(file)

            col_names = ["frame", "x", "y", "obj", "size", "seq", "tbd1", "tbd2", "tbd3", "filename", "time",
                         "path_time",
                         "delta_time", "tbd4"]
            use_cols = ["frame", "x", "y", "obj", "size", "seq", "filename", "time", "delta_time"]
            df = pd.read_csv(fixed_file, names=col_names, usecols=use_cols, parse_dates=['time'])
            df = self.initialize_areas(df)
            df['time'] = df['time'] + pd.to_timedelta(df['delta_time'])
            df = df.drop(['delta_time'], axis=1)

            df = self.optimize_csv(df)

            # df = self.convert_csv_to_pickle(df)
            file = 'data/paths.pkl.xz'
            df.to_pickle(file)

        return self.load_pickle(file)

    def fix_csv(self, csv_file):
        valid_lines = 0
        invalid_lines = 0
        lines = []
        with open(csv_file, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                valid_lines += 1
                if len(row) == 14:
                    for i in range(len(row)):
                        row[i] = row[i].strip()
                    lines.append(row)
                else:
                    # sys.stderr.write(f"warning {str(row)}\n")
                    invalid_lines += 1
                    continue

        fixed_file_path = 'data/fixed.csv'
        with open(fixed_file_path, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        readFile.close()
        writeFile.close()

        return fixed_file_path

    def initialize_areas(self, df):
        h, w = self.img.shape[:2]
        size = 10
        i = 0
        ab = range(size * size)
        w_delta, h_delta = w / size, h / size
        for y in range(size):
            for x in range(size):
                df.loc[(df.x.between(x * w_delta, x * w_delta + w_delta)) & (
                    df.y.between(y * h_delta, y * h_delta + h_delta)), 'areas'] = ab[i]
                i += 1

        return df

    def optimize_csv(self, df):
        df_int = df.select_dtypes(include=['int64'])
        converted_int = df_int.apply(pd.to_numeric, downcast='unsigned')
        df[converted_int.columns] = converted_int
        df_obj = df.select_dtypes(include=['object']).copy()
        converted_obj = pd.DataFrame()

        for col in df_obj.columns:
            num_unique_values = len(df_obj[col].unique())
            num_total_values = len(df_obj[col])
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[:, col] = df_obj[col].astype('category')
            else:
                converted_obj.loc[:, col] = df_obj[col]
        df[converted_obj.columns] = converted_obj
        return df

    def load_pickle(self, pickle):
        return pd.read_pickle(pickle)

    def filter_by_hours(self, begin, end):
        objs = self.last.groupby(["filename", "obj"]).agg({'time': ['min', 'max']})
        begin_time = pd.to_datetime(begin).time()
        end_time = pd.to_datetime(end).time()
        min = objs.time['min'].dt.time  # objs[('time','min')]
        max = objs.time['max'].dt.time  # objs[('time','max')]
        # print(min, max)
        items = objs[(min.between(begin_time, end_time)) | ((min < begin_time) & (max > begin_time))]
        # print(items)
        self.set_last_data(items)
        print(len(items))
        return self.to_arrays(items)

    def filter_by_date_and_hour(self, date, begin, end):
        objs = self.last.groupby(["filename", "obj"]).agg({'time': ['min', 'max']})
        # objs= self.index_file.agg({'time': ['min', 'max']})
        date = pd.to_datetime(date)
        begin_time = date + pd.to_timedelta(begin)
        end_time = date + pd.to_timedelta(end)
        # print(date,begin_time,end_time)
        #     print(objs)
        min = objs[('time', 'min')]
        max = objs[('time', 'max')]
        #     print(min.dt.date)
        items = objs[
            (min.between(begin_time, end_time)) | ((min.where(min < begin_time) & (max.where(max > begin_time))))]
        # print(items)
        self.set_last_data(items)
        print(len(items))
        arr = self.to_arrays(items)
        print(len(arr))
        return arr

    def filter_by_area(self, x0, x1, y0, y1):
        # df_by_obj =
        # current = self.last[self.last.index]
        data_a = self.last[(self.last.x.between(x0, x1)) & (self.last.y.between(y0, y1))]
        self.set_last_data(data_a)
        # print(data_a)
        return self.to_arrays(data_a)

    def filter_by_areas(self, areas):
        # df_by_obj = self.df.set_index(['filename', 'obj']).sort_index().head(8000)
        data_as = self.last[self.last.areas.isin(areas)]
        return self.to_arrays(data_as)

    def apply_filters(self):
        pass

    def no_filter(self):
        return self.last.groupby(["filename", "obj"]).size()

    def to_arrays(self, to_draw):
        points = []
        for t in to_draw.index:
            oo = self.index_file.loc[t]
            # imshow(self.img)
            points.append((oo.x, oo.y))
        return points

    def set_last_data(self, data_to_set):
        # df_by_obj = df.set_index(['filename', 'obj']).sort_index().head(8000)
        indexs = list(data_to_set.index.unique())
        last_data = self.index_file[self.index_file.index.isin(indexs)]
        self.last = last_data

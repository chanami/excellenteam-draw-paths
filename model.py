import pandas as pd


class Model:
    def set_file(self, file):
        self.df = self.load_pickle(file)  # 'data/paths.pkl.xz'
        self.index_file = self.df.set_index(['filename', 'obj']).sort_index()
        self.last = self.df

    def reset(self):
        self.last = self.df

    def load_pickle(self, pickle_file):
        return pd.read_pickle(pickle_file)

    def filter_by_hours(self, begin, end):
        objs = self.last.groupby(["filename", "obj"]).agg({'time': ['min', 'max']})
        begin_time = pd.to_datetime(begin).time()
        end_time = pd.to_datetime(end).time()
        min = objs.time['min'].dt.time  # objs[('time','min')]
        max = objs.time['max'].dt.time  # objs[('time','max')]
        # print(min, max)
        items = objs[(min.between(begin_time, end_time)) | ((min < begin_time) & (max > begin_time))]
        # print(items)
        self.last = items
        print(len(items))
        return self.to_arrays(items)

    def filter_by_date_and_hour(self, date, begin, end):
        objs = self.last.groupby(["filename", "obj"]).agg({'time': ['min', 'max']})
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
        self.last = items
        print(len(items))
        arr=self.to_arrays(items)
        print(len(arr))
        return arr

    def filter_by_area(self, x0, x1, y0, y1):
        # df_by_obj =
        data_a = self.index_file[(self.index_file.x.between(x0, x1)) & (self.index_file.y.between(y0, y1))]
        self.last = data_a
        print(data_a)
        return self.to_arrays(data_a)

    def filter_by_areas(self, areas):
        df_by_obj = self.df.set_index(['filename', 'obj']).sort_index().head(8000)
        data_as = df_by_obj[df_by_obj.areas.isin(areas)]
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

    def create_pickle(self,file):
        pass

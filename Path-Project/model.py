import pandas as pd

class Model:

    def __init__(self, file_name):
        self.file = self.load_file(file_name)


    def load_file(self, file_name):
        pass


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


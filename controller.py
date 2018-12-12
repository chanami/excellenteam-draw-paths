from model import Model
from view import View

class Controller:

    def __init__(self):
        self.model =Model()
        self.view=View()
        # self.run()

    def run(self):
        command = self.view.get_command()
        print("command: "+command)
        if command == '1':
            res=self.model.filter_by_hours("04:00:02", "09:03:02")
            self.view.draw_path(res)
        elif command=='2':
            Model.filter_by_date_and_hour("04:00:02", "09:03:02")

    def apply_filter(self,filter):
        res=self.model.filter_by_hours("04:00:02", "09:03:02")
        self.view.draw_path(res)
    # def load_file(self, file_name):
    #   pass
    #
    # def draw(self, ):
    #     pass


    # def filter_by_hours(self, from_hour, to_hour):
    #     pass
    #
    #
    # def filter_by_date_and_hour(self, from_hour, to_hour, date):
    #     pass
    #
    #
    # def filter_by_area(self, point1, point2):
    #     pass
    #
    #
    # def filter_by_areas(self, *squares):
    #     pass
    #
    #
    # def apply_filters(self, ):
    #     pass

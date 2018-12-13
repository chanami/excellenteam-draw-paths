from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.run()

    def run(self):
        while True:
            command = self.view.get_filter()
            while int(command) < 1 or int(command) > 6:
                print("invalid choice")
                command = self.view.get_filter()
            if command == '6':
                return
            file, pic = self.view.get_files()

            self.model.set_file(file,pic)
            self.view.set_attr(pic)
            # print("command: " + command)
            res = self.apply_filter(command)

    def edit(self, command):
        if command == '1':
            filter = self.view.get_filter()
            self.apply_filter(filter)
        elif command == '2':
            self.model.reset()
            filter = self.view.get_filter()
            self.apply_filter(filter)
        else:
            self.model.reset()
            return

    def apply_filter(self, command):
        if command == '1':
            t1 = input("enter first hour in hh:mm:ss format:\n")
            t2 = input("enter second hour in hh:mm:ss format:\n")
            res = self.model.filter_by_hours(t1, t2)  # ("04:00:02", "09:03:02")
        elif command == '2':
            t1 = input("enter first hour in hh:mm:ss format:\n")
            t2 = input("enter second hour in hh:mm:ss format:\n")
            date = input("enter date in yyyy-mm-dd format:\n")
            res = self.model.filter_by_date_and_hour(date, t1, t2)
        elif command == '3':
            x0, y0 = input("enter top corner as (x,y):\n").split(',')
            x1, y1 = input("enter bottom corner as (x,y):\n").split(',')
            res = self.model.filter_by_area(int(x0), int(x1), int(y0), int(y1))
        elif command == '4':
            self.view.draw_grid()
            areas = input("enter areas as in pic:\n").split(',')
            res = self.model.filter_by_areas(areas)
        elif command == '5':
            res = self.model.no_filter()
        elif command == '6':
            return
        else:
            return
        self.view.draw_path(res)
        command = self.view.edit()
        self.edit(command)

    # def apply_filter(self,filter):
    #     res=self.model.filter_by_hours("04:00:02", "09:03:02")
    #     self.view.draw_path(res)
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

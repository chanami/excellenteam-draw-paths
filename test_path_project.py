import unittest

class PathProjectTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def test_load_file(self):
        controller = controller.Controller("data/")
        self.file = controller.load_file("")


    def test_load_file(self, file_name):
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


if __name__ == '__main__':
    unittest.main()
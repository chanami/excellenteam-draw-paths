import unittest

class PathProjectTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def test_load_file(self):
        control = controller.Controller("../data/paths.pkl.xz")
        df = control.get_file()


    def test_draw(self):
        pass


    def test_filter_by_hours(self):
        pass


    def test_filter_by_date_and_hour(self):
        pass


    def test_filter_by_area(self):
        pass


    def test_filter_by_areas(self):
        pass


    def test_apply_filters(self):
        pass


if __name__ == '__main__':
    unittest.main()
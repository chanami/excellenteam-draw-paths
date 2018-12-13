import unittest
from controller import Controller
from model import Model


class PathProjectTestCase(unittest.TestCase):

    def setUp(self):
        # self.controller = Controller()
        self.model = Model()

    def test_load_pickle(self):
        df = self.model.load_pickle('data/paths.pkl.xz')

    def test_filter_by_hours(self):
        df = self.model.load_pickle('data/paths.pkl.xz')

    def test_reset_df(self):
        self.model.set_file('data/paths.pkl.xz')
        # top100 = df.sort_values('time').head(100)
        top100 = self.model.df.agg({'time': ['min', 'max']}).head(100)
        filtered = self.model.filter_by_hours("01:27:09", "01:28:18")
        print(filtered)
        # self.assertEqual(filtered, 8)


    def test_draw(self):
        # control = controller.Controller()
        # control.draw()
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
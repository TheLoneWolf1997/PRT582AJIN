import unittest
from rockpaper import start_Game


class RockpaperTests(unittest.TestCase):

    def test_get_rockpaper(self):
        self.assertEqual(start_Game(), 'paper')


if __name__ == '__main__':
    unittest.main()
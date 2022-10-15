import unittest
from rockpaper import start_Game


class RockpaperTests(unittest.TestCase):

    def test_get_rockpaper(self):
        self.assertEqual(start_Game(), 'scissors')


if __name__ == '__main__':
    unittest.main()

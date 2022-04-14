import unittest
# (for ubuntu users, change import for doggy)
# appending path to src/doggy.py
# code needed below
# import sys
# sys.path.append('../src')
# import doggy
import pandas as pd

import src.doggy as doggy


class MyTestCase(unittest.TestCase):
    def test_init_database(self):
        doggy.init_db()
        empty_dataframe = pd.DataFrame(columns=["name", "cuisine", "ingredients", "image"])
        self.assertEqual(doggy.print_database(), empty_dataframe.to_string())




    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

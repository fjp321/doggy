import unittest
# (for ubuntu users, change import for doggy)
# appending path to src/doggy.py
# code needed below
import sys
sys.path.append('../')
# import doggy
from src.doggy import init_db as test_init_db
import pandas as pd
import src.doggy as doggy
from os.path import exists


class MyTestCase(unittest.TestCase):
    def test_init_database(self):
        doggy.init_db()
        empty_dataframe = pd.DataFrame(columns=["name", "cuisine", "ingredients", "image"])
        self.assertEqual(doggy.get_database().to_string(), empty_dataframe.to_string())
        self.assertEqual(True, exists("database.json"))

    def test_add_recipe(self):
        doggy.init_db()
        doggy.init_cuisines()
        doggy.init_ingredients()

        doggy.add_cuisine("american")
        doggy.add_ingredient("cereal", "cup")
        doggy.add_ingredient("milk", "cup")
        doggy.add_recipe("american", "test recipe", "temp_location", [{"cereal", 0.5}, {"milk", 0.5}])
        test_dataframe = pd.DataFrame([["test_recipe", "american", [{"cereal" : 0.5}, {"milk" : 0.5}], "temp_location"]], columns=["name", "cuisine", "ingredients", "image"])
        self.assertEqual(doggy.print_database().to_string(), test_dataframe.to_string())

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

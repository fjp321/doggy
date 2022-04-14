import unittest
# (for ubuntu users, change import for doggy)
# appending path to src/doggy.py
# code needed below
import sys
sys.path.append('../')
# import doggy
import pandas as pd
import src.doggy as doggy
from os.path import exists


class MyTestCase(unittest.TestCase):
    def test_init_ingredients(self):
        doggy.init_ingredients()
        empty_ingredient = {}
        self.assertEqual(doggy.get_ingredients(), empty_ingredient)
        self.assertEqual(True, exists("cuisines.csv"))

    def test_add_cuisine(self):
        doggy.init_ingredients()
        doggy.add_ingredient("cereal", "cup")
        example_ingredient = {"cereal" : "cup"}
        self.assertEqual(doggy.get_ingredients(), example_ingredient)

    def test_add_multiple_cuisine(self):
        doggy.init_ingredients()
        doggy.add_ingredient("cereal", "cup")
        doggy.add_ingredient("milk", "cup")
        example_ingredient = {"cereal" : "cup", "milk" : "cup"}
        self.assertEqual(doggy.get_ingredients(), example_ingredient)

    def test_add_same_cuisine(self):
        doggy.init_ingredients()
        doggy.add_ingredient("cereal", "cup")
        doggy.add_ingredient("milk", "cup")
        doggy.add_ingredient("milk", "cup")
        example_ingredient = {"cereal" : "cup", "milk" : "cup"}
        self.assertEqual(doggy.get_ingredients(), example_ingredient)
   

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

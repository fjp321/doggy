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
    def test_init_cuisine(self):
        doggy.init_cuisines()
        empty_cuisines = []
        self.assertEqual(doggy.get_cuisines(), empty_cuisines)
        self.assertEqual(True, exists("cuisines.csv"))

    def test_add_cuisine(self):
        doggy.init_cuisines()
        doggy.add_cuisine("american")
        example_cuisine = ["american"]
        self.assertEqual(doggy.get_cuisines(), example_cuisine)

    def test_add_multiple_cuisine(self):
        doggy.init_cuisines()
        doggy.add_cuisine("american")
        doggy.add_cuisine("asian")
        example_cuisine = ["american", "asian"]
        self.assertEqual(doggy.get_cuisines(), example_cuisine)

    def test_add_same_cuisine(self):
        doggy.init_cuisines()
        doggy.add_cuisine("american")
        doggy.add_cuisine("asian")
        doggy.add_cuisine("asian")
        example_cuisine = ["american", "asian"]
        self.assertEqual(doggy.get_cuisines(), example_cuisine)
   
    def test_del_cuisine(self):
        doggy.init_cuisines()
        doggy.add_cuisine("american")
        doggy.add_cuisine("asian")
        doggy.del_cuisine("american")
        doggy.del_cuisine("american")
        doggy.del_cuisine("asian")
        example_cuisine = []
        self.assertEqual(doggy.get_cuisines(), example_cuisine)

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

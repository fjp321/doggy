import unittest
# (for ubuntu users, change import for doggy)
# appending path to src/doggy.py
# code needed below
# import sys
# sys.path.append("../src")
# import doggy.py as doggy

import src.doggy as doggy



class MyTestCase(unittest.TestCase):
    def init_database(self):
        doggy.init_db()



    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

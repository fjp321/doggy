import sys
import json
import csv
import pandas as pd

def init_db():
    # initialize dataframe with name, type, ingredients, and recipe
    df = pd.DataFrame(columns = ["name", "type", "ingredients", "recipe"])

    #write dataframe to database to data.json
    database = open("data/data.json", "w")
    database.write(df.to_json())
    database.close()

def init_types():
    types_list = []

    # touch empty file for types, save as csv
    types = open("data/types.csv")
    types.close()

def init_ingredients():
    ingredients_dict = []

    # touch empty file for ingredients, save as json
    ingredients = open("data/ingredients.json")i
    ingredients.write(json.dumps(ingredients_dict))
    ingredients.close()

def print_db():
    database = pd.read_json("data/data.json")
    print(database)
    
def print_types():
    types = open("data/types.csv")
    csv_reader = csv.reader(types, delimiter=' ')
    for row in csv_reader:
        print(row + ',')
  
def print_ingredients():
    print("placeholder")
  
def add_recipe():
    print("placeholder")

def add_type();
    print("placeholder")
  
def add_ingredient():
    print("placeholder")

def del_recipe():
    print("placeholder")

def del_type():
    print("placeholder")

def del_ingredient():
    print("placeholder")

def valid_ingredient():
    print("placeholder")
  
def valid_type():
    print("placeholder")
  
def __init__(self):
    init_db()
    init_types()
    init_ingredients()

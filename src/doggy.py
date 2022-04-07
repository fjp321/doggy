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
    typesonclose()

def init_ingredients():
    ingredients_dict = []

    # touch empty file for ingredients, save as json
    ingredients = open("data/ingredients.json")i
    ingrtedients.write(json.dumps(ingredients_dict))
    ingredients.close()

def print_db():
    database = pd.read_json("data/data.json")
    print(database)
    
def print_types():
    print("placeholder")
  
def print_ingredients():
    print("placeholder")
  
def update_db():
    print("placeholder")

def update_types();
    print("placeholder")
  
def update_ingredients():
    print("placeholder")
  
def valid_ingredient():
    print("placeholder")
  
def valid_type():
    print("placeholder")
  
def __init__(self):
    init_db()
    init_types()
    init_ingredients()

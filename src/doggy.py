import sys
import json
import pandas as pd

def init_db():
    # initialize dataframe with name, type, ingredients, and recipe
    df = pd.DataFrame(columns = ["name", "type", "ingredients", "recipe"])

    #write dataframe to database to data.json
    database = open("data.json", "w")
    database.write(df.to_json())
    database.close()

def init_types():
    print("placeholder")

def init_ingredients():
    print("placeholder")

def print_db():
    print("placeholder")

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

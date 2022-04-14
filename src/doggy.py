import sys
import json
import csv
import pandas as pd

no_error_code = 0
input_error_code = -1
already_exists_error_code = -2

recipes_location = "data/recipes.json"
ingredients_location = "data/ingredients.json"
types_location = "data/types.csv"


# creates pandas dataframe with needed columns and save dataframe to json
def init_db():
    # initialize dataframe with name, type, ingredients, and recipe
    recipes_df = pd.DataFrame(columns=["name", "type", "ingredients", "recipe"])

    # write dataframe to database to data.json
    recipes_file = open(recipes_location, 'w')
    recipes_file.write(recipes_df.to_json())
    recipes_file.close()


# saves files for types as csv
def init_types():
    # touch empty file for types, save as csv
    types_file = open(types_location, 'w')
    types_file.close()


# saves ingredients dictionary to json file
def init_ingredients():
    # touch empty file for ingredients, save as json
    ingredients_file = open(ingredients_location, 'w')
    ingredients_file.close()


# helper function to print recipes file
def print_recipes():
    recipes_df = pd.read_json(recipes_location)
    print(recipes_df)


# helper function to print types list
def print_types():
    types_file = open(types_location, 'r')
    csv_reader = csv.reader(types_file, delimiter=' ')
    for row in csv_reader:
        print(row + ',')
    types_file.close()


# helper function to print ingredients dictionary
def print_ingredients():
    ingredients_file = open(ingredients_location, 'r')
    print(json.load(ingredients_file))


# helper function to check if recipe is in recipe df
def contain_recipe(input_recipe):
    print("placeholder")


def contain_type(input_type):
    if not (isinstance(input_type, str)):
        print("input is not a string")
        return input_error_code
    types_file = open(types_location, 'r')
    csv_reader = csv.reader(types_file, delimiter=' ')


def contain_ingredient(input_ingredient):
    print("placeholder")


# opens json recipes file and reads into df, add recipe based on inputs string type, string dictionary ingredients, and string list steps, and saves df to json file
def add_recipe(type_input, ingredients_input, steps_input):
    print("placeholder")


# opens csv and reads into list, then appends input string type to list and saves as csv
# will raise exception if input is not string
def add_type(input_type):
    if not isinstance(input_type, str):
        print("input is not string")
        return input_error_code
    if (contain_type(input_type)):
        print("input already in types.csv")
        return already_exists_error_code
    types_file = open(types_location, 'a')
    types_file.write(input_type)
    types_file.close()
    return no_error_code


# open ingredients json and reads into dictionary, add elements based on inputs string ingredient, string measurement, then saves to json file
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

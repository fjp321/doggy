import sys
import json
import csv
import pandas as pd

no_error_code = 0
input_error_code = -1
already_exists_error_code = -2

database_location = "data/database.json"
ingredients_location = "data/ingredients.json"
cuisines_location = "data/cuisines.csv"


# creates pandas dataframe with needed columns and save dataframe to json
def init_db():
    # initialize dataframe with name, cuisine, ingredients, and recipe
    database_df = pd.DataFrame(columns=["name", "cuisine", "ingredients", "image"])

    # write dataframe to database to data.json
    database_file = open(database_location, 'w')
    database_file.write(database_df.to_json())
    database_file.close()


# saves files for cuisines as csv
def init_cuisines():
    # touch empty file for cuisines, save as csv
    cuisines_file = open(cuisines_location, 'w')
    cuisines_file.close()


# saves ingredients dictionary to json file
def init_ingredients():
    # touch empty file for ingredients, save as json
    ingredients_file = open(ingredients_location, 'w')
    ingredients_file.close()


# helper function to print recipes file
def print_database():
    return pd.read_json(database_location).to_string()


# helper function to print cuisines list
def print_cuisines():
    cuisines_file = open(cuisines_location, 'r')
    csv_reader = csv.reader(cuisines_file, delimiter=' ')
    for row in csv_reader:
        print(row + ',')
    cuisines_file.close()


# helper function to print ingredients dictionary
def print_ingredients():
    ingredients_file = open(ingredients_location, 'r')
    print(json.load(ingredients_file))


# helper function to check if recipe is in recipe df
def contain_name(input_name):
    print("placeholder")


def contain_cuisine(input_cuisine):
    if not (isinstance(input_cuisine, str)):
        print("input is not a string")
        return input_error_code
    cuisines_file = open(cuisines_location, 'r')
    csv_reader = csv.reader(cuisines_file, delimiter=' ')


def contain_ingredient(input_ingredient):
    print("placeholder")


# opens json recipes file and reads into df, add recipe based on inputs string cuisine, string dictionary ingredients, and string list steps, and saves df to json file
def add_recipe(input_cuisine, input_name, input_image, input_ingredients):
    print("placeholder")


# opens csv and reads into list, then appends input string cuisine to list and saves as csv
# will raise exception if input is not string
def add_cuisine(input_cuisine):
    if not isinstance(input_cuisine, str):
        print("input is not string")
        return input_error_code
    if (contain_cuisine(input_cuisine)):
        print("input already in cuisines.csv")
        return already_exists_error_code
    cuisines_file = open(cuisines_location, 'a')
    cuisines_file.write(input_cuisine)
    cuisines_file.close()
    return no_error_code


# open ingredients json and reads into dictionary, add elements based on inputs string ingredient, string measurement, then saves to json file
def add_ingredient():
    print("placeholder")


def del_recipe():
    print("placeholder")


def del_cuisine():
    print("placeholder")


def del_ingredient():
    print("placeholder")


def get_database():
    return pd.read_json(database_location)


def __init__(self):
    init_db()
    init_cuisines()
    init_ingredients()

import sys
import json
import csv
import pandas as pd

no_error_code = 0
input_error_code = -1
already_exists_error_code = -2

default_database_location = "database.json"
default_ingredients_location = "ingredients.json"
default_cuisines_location = "cuisines.csv"


# creates pandas dataframe with needed columns and save dataframe to json
def init_db(file_location=default_database_location):
    # initialize dataframe with name, cuisine, ingredients, and recipe
    database_df = pd.DataFrame(columns=["name", "cuisine", "ingredients", "image"])

    # write dataframe to database to data.json
    database_file = open(file_location, 'w')
    database_file.write(database_df.to_json())
    database_file.close()


# saves files for cuisines as csv
def init_cuisines(file_location=default_cuisines_location):
    # touch empty file for cuisines, save as csv
    cuisines_file = open(file_location, 'w')
    cuisines_file.close()


# saves ingredients dictionary to json file
def init_ingredients(file_location=default_ingredients_location):
    # touch empty file for ingredients, save as json
    ingredients_file = open(file_location, 'w')
    ingredients_file.close()


# helper function to print recipes file
def print_database(file_location=default_database_location):
    return pd.read_json(file_location).to_string()


# helper function to print cuisines list
def get_cuisines(file_location=default_cuisines_location):
    cuisines_file = open(file_location, 'r')
    csv_reader = csv.reader(cuisines_file, delimiter=',')
    cuisine_list = list(csv_reader)
    cuisines_file.close()
    if len(cuisine_list) != 0:
        cuisine_list = cuisine_list[0]
    return cuisine_list


# helper function to print ingredients dictionary
def get_ingredients(file_location=default_ingredients_location):
    ingredients_file = open(file_location, 'r')
    
    ingredients_file.close()


# helper function to check if recipe is in recipe df
def contain_name(input_name):
    print("placeholder")


def contain_cuisine(input_cuisine, file_location=default_cuisines_location):
    if not (isinstance(input_cuisine, str)):
        print("input is not a string")
        return input_error_code # maybe change to false for this function
    cuisine_list = get_cuisines()    
    return input_cuisine in cuisine_list

def contain_ingredient(input_ingredient):
    print("placeholder")


# opens json recipes file and reads into df, add recipe based on inputs string cuisine, string dictionary ingredients, and string list steps, and saves df to json file
def add_recipe(input_cuisine, input_name, input_image, input_ingredients):
    print("placeholder")


# opens csv and reads into list, then appends input string cuisine to list and saves as csv
# will raise exception if input is not string
def add_cuisine(input_cuisine,file_location=default_cuisines_location):
    if not isinstance(input_cuisine, str):
        print("input is not string")
        return input_error_code
    if contain_cuisine(input_cuisine):
        print("input already in cuisines.csv")
        return already_exists_error_code
    # adjust input string if non empty list
    input_string = input_cuisine
    if len(get_cuisines()) != 0:
        input_string = "," + input_string
    cuisines_file = open(file_location, 'a')
    cuisines_file.write(input_string)
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


def get_database(file_location=default_database_location):
    return pd.read_json(file_location)


def __init__(self):
    init_db()
    init_cuisines()
    init_ingredients()

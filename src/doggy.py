##
# @mainpage Doggy Wheel Project
# 
# @section descript_main Description
# Python wheel file for database interaction and initialization for the purpose for recipe management

## 
# @file doggy.py
#
# @brief Wheel file containing functions for database interaction
# 
# @section description_doggy Description
# Wheel file containing functions for database interaction
# 
# @section libraries_main Libraries/Modules
# - sys standard library
#   - for access to file io functions
# - json standard library
#   - for access to json conversion functions
# - csv standard library
#   - for csv reader functions
# - pandas dataframe functions
#   - for interaction for larger databases
#

# Imports
import sys
import json
import csv
import pandas as pd

# Global Variables
## return code for success
no_error_code = 0
## return code for invalid input variable types
input_error_code = -1
## error code for entries already existing in database
already_exists_error_code = -2
## error code for entries that do not exist in the database
does_not_exist_error_code = -3
## default file location for database
default_database_location = "database.json"
## default file location for ingredients database
default_ingredients_location = "ingredients.json"
## default file location for cuisines database
default_cuisines_location = "cuisines.csv"


# Functions
def init_db(file_location=default_database_location):
    """! creates pandas dataframe with needed columns to represent database of recipes and save dataframe to json
    @param file_location    the file location the database will be saved to
    """
    # initialize dataframe with name, cuisine, ingredients, and recipe
    database_df = pd.DataFrame(columns=["name", "cuisine", "ingredients", "image"])

    # write dataframe to database to data.json
    database_file = open(file_location, 'w')
    database_file.write(database_df.to_json())
    database_file.close()


def init_cuisines(file_location=default_cuisines_location):
    """! saves cuisines csv to initial location
    @param file_location    the file location the cuisines database will be saved to
    """
    cuisines_file = open(file_location, 'w')
    cuisines_file.close()


def init_ingredients(file_location=default_ingredients_location):
    """! saves ingredients dictionary to initial location
    @param file_location    the file location the ingredients database will be saved to
    """
    ingredients_file = open(file_location, 'w')
    ingredients_file.close()


def get_database(file_location=default_database_location):
    """! helper function to return recipes database as string
    @param file_location    the file location the function will access to read
    @return string database
    """
    return pd.read_json(file_location)


def get_cuisines(file_location=default_cuisines_location):
    """! Helper function to return cuisines list
    @param file_location    the file location the function will access to read
    @return list of strings representing all available cuisines
    """
    cuisines_file = open(file_location, 'r')
    csv_reader = csv.reader(cuisines_file, delimiter=',')
    cuisine_list = list(csv_reader)
    cuisines_file.close()
    if len(cuisine_list) != 0:
        cuisine_list = cuisine_list[0]
    return cuisine_list


def get_ingredients(file_location=default_ingredients_location):
    """! Helper function to return ingredients dictionary
    @param file_location    the file location the function will access to read
    @return dictionary of string keys and string values for ingredient name and measurement respectively
    """
    ingredients_file = open(file_location, 'r')
    # added try catch for error handling on empty json file
    try:
        ingredients_dict = json.load(ingredients_file)   
    except:
        ingredients_dict = {}
    ingredients_file.close()
    return ingredients_dict


def contain_name(input_name):
    """! Helper function that will check if a recipe name already exists in the database. 
    @param input_name   string name that will be checked for
    @param file_location    the file location that will be accessed for read
    @return will return 0 on success
    """
    print("placeholder")


def contain_cuisine(input_cuisine, file_location=default_cuisines_location):
    """! Helper function that checks if cuisine is already saved in cuisine list
    @param input_cuisine    string that will be checked for in the ingredient database
    @param file_location    the file location that will be accessed for read
    @return true if input_cuisine is in list false otherwise 
    """
    if not (isinstance(input_cuisine, str)):
        print("input is not a string")
        return input_error_code # maybe change to false for this function
    cuisine_list = get_cuisines(file_location=file_location)    
    return input_cuisine in cuisine_list


def contain_ingredient(input_ingredient, file_location=default_ingredients_location):
    """! Helper function that checks if ingredient is in ingredients dictionary keys list
    @param input_ingredient string that will be checked for in ingredients dictionary key value
    @return true if input_ingredient is in dictionary otherwise false
    """
    ingredients_dict = get_ingredients(file_location=file_location)
    return input_ingredient in ingredients_dict.keys()


def add_recipe(input_cuisine, input_name, input_image, input_ingredient_list, file_location=default_database_location):
    """! Opens json recipes file and reads into df, add recipe based on inputs string cuisine, string dictionary ingredients, and string list steps, and saves df to json file
    @param input_cuisine    string representing cuisine of the recipe
    @param input_name   string name representing the name of the recipe
    @param input_image  file location for the image of the recipe
    @param input_ingredients    dictionary of string keys and float values, representing 
    @param file_location file location that will be opened and read
    @return will return 0 on success
    """
    if not isinstance(input_cuisine, str) or not isinstance(input_name, str) or not isinstance(input_ingredient_list, list) or not isinstance(input_name, str):
        print("input is incorrect data type")
        return input_error_code
    if not contain_cuisine(input_cuisine, file_location=file_location):
        print("cuisine is not in cuisine list")
        return does_not_exist_error_code
    for ingredient in input_ingredient_list:
        if not contain_ingredient(input_ingredient, file_location=file_location):
            print(ingredient + " does not exist in ingredient databse")
            return does_not_exist_error_code
    if contain_recipe(input_name, file_location):
        print("recipe name already exists")
        return already_exists_error_code
    # add recipe image check exists




def add_cuisine(input_cuisine,file_location=default_cuisines_location):
    """! Opens csv and reads into list, then appends input string cuisine to list and saves as csv
    @param input_cuisine    string representing the input cuisine to be added to the database
    @param file_location    file location of the database that the changes will be written to
    @return will return 0 on success
    """
    if not isinstance(input_cuisine, str):
        print("input is not string")
        return input_error_code
    if contain_cuisine(input_cuisine, file_location=file_location):
        print("input already in cuisines.csv")
        return already_exists_error_code
    # adjust input string if non empty list
    cuisines_file = open(file_location, 'a')
    if len(get_cuisines(file_location=file_location)) != 0:
        cuisines_file.write("," + input_cuisine)
    else:
        cuisines_file.write(input_cuisine)
    cuisines_file.close()
    return no_error_code


def add_ingredient(input_ingredient, input_measurement, file_location=default_ingredients_location):
    """! Open ingredients json and reads into dictionary, add elements based on inputs string ingredient, string measurement, then saves to json file
    @param input_ingredient string representing the ingredient 
    @param input_measurement    string representing the unit of measurement for the ingredient
    @param file_location    file location of the database that the changes will be written to
    @return will return 0 on success
    """
    if not isinstance(input_ingredient,str) or not isinstance(input_measurement,str):
        print("input is not string")
        return input_error_code
    if contain_ingredient(input_ingredient, file_location=file_location):
        print("input_ingredient already exists, try update_measurement(input_ingredient, input_measurement) if you want to update measurement tied to ingredient")
        return already_exists_error_code
    # open file and load into local dictionary
    ingredients_dict = get_ingredients(file_location=file_location)
    ingredients_dict[input_ingredient] = input_measurement
    ingredients_file = open(file_location, "w")
    ingredients_file.write(json.dumps(ingredients_dict))
    ingredients_file.close()
    return no_error_code
    


def del_recipe(input_recipe, file_location=default_database_location):
    """! Open recipes database, and removes recipe entry based on recipe input string
    @param input_recipe string representing the recipe to be removed
    @param file_location    file location of the database where changes will be written to
    @returns will return 0 on success
    """
    print("placeholder")


def del_cuisine(input_cuisine, file_location=default_cuisines_location):
    """! Opens cuisine list, checks if input is in list, then removes it and rewrites list to csv
    @param input_cuisine string representing the cusine to be removed from the database
    @param file_location file location of the database where changes will be written to
    @return will return 0 on success
    """
    if not isinstance(input_cuisine,str):
        print("input is not string")
        return input_error_code
    if not contain_cuisine(input_cuisine, file_location=file_location):
        print("input is not in list, no deletion needed")
        return does_not_exist_error_code
    cuisine_list = get_cuisines(file_location=file_location)
    cuisine_list.remove(input_cuisine)
    cuisine_file = open(file_location, "w")
    if len(cuisine_list) != 0: 
        cuisine_file.write(cuisine_list[0])
        cuisine_list.pop(0)
        for cuisine in cuisine_list:
            cuisine_file.write("," + cuisine)
    cuisine_file.close()
    return no_error_code


def del_ingredient(input_ingredient, file_location=default_ingredients_location):
    """! Opens ingredients dictionary, checks if input is in dictionary, then removes it and rewrites json
    @param input_ingredient string that represents teh input ingredient to be deleted
    @param file_location    file location that represents the database that will be updated
    @return will return 0 on success
    """
    if not isinstance(input_ingredient,str):
        print("input is not string")
        return input_error_code
    if not contain_ingredient(input_ingredient, file_location=file_location):
        print("ingredient not found, no deletion needed")
        return does_not_exist_error_code
    ingredient_dict = get_ingredients(file_location=file_location)
    ingredient_dict.pop(input_ingredient)
    ingredient_file = open(file_location, 'w')
    if not ingredient_dict:
        ingredient_file.write(json.dumps(ingredient_dict))
    ingredient_file.close()
    return no_error_code

def update_ingredient(input_ingredient, input_measurement, file_location=default_ingredients_location):
    """! Helper function to update input ingredient with new measurement, or add new ingredient with specified measurement if ingredient does not exist
    @param input_ingredient string representing ingredient that will updated
    @param input_measurement    string representing measurement associated with ingredient
    @param file_location    file representing the database that will be updated
    @return will return 0 on success
    """
    if not isinstance(input_ingredient,str):
        print("input is not string")
        return input_error_code
    if not contain_ingredient(input_ingredient, file_location=file_location):
        print("ingredient not found, adding instead")
        return add_ingredient(input_ingredient, input_measurement, file_location=file_location)
    ingredient_dict = get_ingredients(file_location=file_location)
    ingredient_dict[input_ingredient] = input_measurement
    ingredient_file = open(file_location, 'w')
    ingredient_file.write(json.dumps(ingredient_dict))
    ingredient_file.close()
    return no_error_code


def get_database(file_location=default_database_location):
    """! Helper function that will return the database as a dataframe
    @param file_location location of the database that will be accessed and returned
    @return dataframe that represents the recipe database
    """
    return pd.read_json(file_location)


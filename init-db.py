import sys
import json
import pandas as pd

# initialize hash table of usable ingredients, size 5000

# write hash table to usable_ingredients as binary

# initialize list of strings of acceptable types

# write list of strings into acceptable_types as binary

# initialize dataframe with name, type, ingredients, and recipe
df = pd.DataFrame(columns = ["name", "type", "ingredients", "recipe"])

#write dataframe to database to data.json
database = open("data.json", "w")
database.write(df.to_json())
database.close()

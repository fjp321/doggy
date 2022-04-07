import sys
import json
import pandas as pd

# initialize dataframe with name, type, ingredients, and recipe
df = pd.DataFrame(columns = ["name", "type", "ingredients", "recipe"])

#write dataframe to database to data.json
database = open("data.json", "w")
database.write(df.to_json())
database.close()

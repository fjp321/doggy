import sys
import json
import pandas as pd

ingredient_arg=sys.argv[1]
recipe_arg=sys.argv[2]

df1 = pd.read_json("data.json")
print(df1)
df2 = pd.DataFrame({
        "name":["cereal"], 
        "type":["american"],
        "ingredients":["ingredients1.txt"],
        "recipe":["recipe1.txt"]
    })

df1 = pd.concat([df1,df2],ignore_index=True)
print(df1)

database = open("data.json","w")
database.write(df1.to_json())
database.close()

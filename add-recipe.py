import sys
import numpy as np
import scipy as sp
import pandas as pd
from lxml import etree as et

ingredient_arg=sys.argv[1]
recipe_arg=sys.argv[2]

tree = et.parse('recipes.xml')
root = tree.getroot()
file_recipe=open(recipe_arg)
name_arg=file_recipe.readline().rstrip('\n')
new_recipe=et.SubElement(root,"recipe", name=name_arg)

theme_arg=file_recipe.readline().rstrip('\n')
current_line=file_recipe.readline().rstrip('\n')
directions=et.SubElement(new_recipe, "directions")
index=0
while len(current_line) != 0:
    current_recipe=et.SubElement(directions, "step", step_num=(str)(index))
    index = index + 1
    current_recipe.text=current_line
    current_line=file_recipe.readline().rstrip('\n')
file_recipe.close()

file_ingredients=open(ingredient_arg)
current_line=file_ingredients.readline().rstrip('\n')
ingredients=et.SubElement(new_recipe, "ingredients")
while len(current_line) != 0:
    formatted = current_line.split(' ')
    current_ingredient=et.SubElement(ingredients, "ingredient", quantity=formatted[0])
    current_ingredient.text=formatted[1]
    current_line=file_ingredients.readline().rstrip('\n')
file_ingredients.close()

theme=et.SubElement(new_recipe, "theme")
theme.text=theme_arg
db=open('recipes.xml','w')
db.write(et.tostring(new_recipe, pretty_print=True, encoding='utf-8').decode('utf-8'))
db.close()
rm recipes.xml
python3 init-db.py
for i in $(seq 1 $1)
do
    python3 add-recipe.py ingredients.txt recipe.txt
done
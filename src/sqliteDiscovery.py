import sqlite3
from sqlite3 import Error


# This creates a table and identifies the columns and constraints
# CREATE TABLE IF NOT EXISTS recipes (
#     id integer PRIMARY KEY, (alias for rowid)
#     cuisine text UNIQUE, (Unique means no duplicate or update)
#     ingredients text NOT NULL,
#     link text,
# );


# Creates a database connection to a database that resides in db_file

# these are helper functions
def string_to_array(in_str):
    ret_arr = in_str.split("\n")
    return ret_arr


def array_to_string(in_arr):
    ret_str = '\n'.join(in_arr)
    return ret_str


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)  # returns a connection object
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


# creates a table in conn from create_table_sql1
def create_table(conn, create_table_sql):
    try:
        curs = conn.cursor()  # returns a cursor that allows you to traverse the database
        curs.execute(create_table_sql)  # inserts a table
    except Error as e:
        print(e)


# Inserts a row into the table provided, returns the rowid for the row added
def insert_recipe(conn, row_add):
    row_add_syn = "INSERT INTO recipes(cuisine, ingredients, steps)" \
                  "VALUES(?,?,?)"
    curs = conn.cursor()
    curs.execute(row_add_syn, row_add)  # execute, this executes the sql statement provided by row_add_sy
    conn.commit()  # This saves the changes
    return curs.lastrowid


# Updates data in the recipe table
def update_recipe(conn, row_update, row_syn):
    curs = conn.cursor()
    if row_update is not None:
        row_up_syn = "UPDATE recipes SET cuisine=?, ingredients=?, steps=? WHERE id=?"
        curs.execute(row_up_syn, row_update)
    elif row_syn is not None:
        curs.execute(row_syn)
    else:
        raise Exception('Invalid Parameter')
    conn.commit()


# returns an iterator rows for all of the rows
def select_all_rows(conn):
    curs = conn.cursor()
    curs.execute("SELECT * FROM recipes")
    rows = curs.fetchall()
    return rows


# returns an iterator for rows, that match input
def select_row_priority(conn, cuisine, ingredient, step):
    curs = conn.cursor()
    if cuisine is not None:
        curs.execute("SELECT * FROM recipes WHERE cuisine=?", (cuisine,))
    elif ingredient is not None:
        curs.execute("SELECT * FROM recipes WHERE ingredients=?", (ingredient,))
    elif step is not None:
        curs.execute("SELECT * FROM recipes WHERE steps=?", (step,))
    else:
        raise Exception('Invalid parameters')

    return curs.fetchall()


# deletes a row that matches the given parameters
def delete_row_priority(conn, rowid, cuisine, ingredient, step):
    curs = conn.cursor()
    if rowid is not None:
        curs.execute("DELETE FROM recipes WHERE id=?", (rowid,))
    elif cuisine is not None:
        curs.execute("DELETE FROM recipes WHERE cuisine=?", (cuisine,))
    elif ingredient is not None:
        curs.execute("DELETE FROM recipes WHERE ingredients=?", (ingredient,))
    elif step is not None:
        curs.execute("DELETE FROM recipes WHERE steps=?", (step,))
    else:
        raise Exception('Invalid parameters')

    return curs.fetchall()


def main():
    table_one = "CREATE TABLE IF NOT EXISTS recipes " \
                "(id integer PRIMARY KEY, cuisine text, ingredients text NOT NULL, steps text UNIQUE);"
    database_path = r"C:\Users\potte\PycharmProjects\pythonProject1\sqliteDiscover.db"
    conn = create_connection(database_path)

    if conn is not None:
        create_table(conn, table_one)
    else:
        print("Error!")

    row_to_add = ("american", "milk, cheese, pasta", "1. cook pasta\n2. combine milk and cheese")
    try:
        row_id = insert_recipe(conn, row_to_add)
    except Error as e:
        print(e)

    row_to_add_two = ("american", "egg, cheese", "1. scramble eggs\n2. combine eggs and cheese")
    try:
        row_id = insert_recipe(conn, row_to_add_two)
    except Error as e:
        print(e)

    update_recipe(conn, None, "UPDATE recipes SET cuisine='italian' WHERE id=1")
    # delete_row_priority(conn, 1, None, None, None)  # comment out and in to check for deletion
    rows_all = select_all_rows(conn)
    rows_cuisine = select_row_priority(conn, "american", None, None)

    for i in rows_all:
        (rowid, cuisine, ingredient, step) = i
        print("row: ", i)

    for i in rows_cuisine:
        print("row: ", i)
    conn.close()


if __name__ == '__main__':
    main()

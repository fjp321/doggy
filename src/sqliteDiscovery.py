# Imports
import sqlite3
from sqlite3 import Error

# Global Variables
file_path_global = "./sqliteDiscover.db"  # path for the file that stored database


# Functions
def string_to_array(in_str):
    """! takes in a string and splits it on the newlines, returning an array of strings
    @param in_str   the string that is being split
    @return returns an array
    """
    ret_arr = in_str.split("\n")
    return ret_arr


def array_to_string(in_arr):
    """! takes in an array and converts it into a string, concatenating the elements with
    newlines
    @param in_arr   the array that is being converted into a string"""
    ret_str = '\n'.join(in_arr)
    return ret_str


def create_connection(db_file):
    """! creates a file at the filepath and creates a connection object that allows you to
    update the database
    @param db_file  the filepath where the database should be created
    @return connection object, allows you to update the database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)  # returns a connection object
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


# creates a table in conn from create_table_sql1
def create_table(conn, create_table_sql):
    """! executes the command provided and commits the changes to the database, the command
    should create a new table in the database. The table is defined by the input string
    @param conn    a connection object that represents the current database
    @param create_table_sql    a string that is formatted to execute a command that creates a table
    """
    try:
        curs = conn.cursor()  # returns a cursor that allows you to traverse the database
        curs.execute(create_table_sql)  # inserts a table
        conn.commit()
    except Error as e:
        print(e)


# Inserts a row into the table provided, returns the rowid for the row added
def insert_row(conn, table, columns, row_add, row_syn):
    """! either executes the command provided, row_syn, or formats a proper command with the
    provided inputs, table, column, and row_add. The command will insert a row into the table
    provided.
    @param conn     a connection object that represents the current database
    @param table    a string that represents the name of the table to change
    @param columns  a string that represents all of the columns, split by commas
    @param row_add  a tuple with values for all of the necessary columns
    @param row_syn  a string that represents the proper command to correctly execute an insertion
    @return the id of the row that was added (integer)
    """
    curs = conn.cursor()
    if row_add is not None:
        column_arr = columns.split(',')
        column_arr_mapped = map(lambda x: "?", column_arr)
        values_str = ','.join(column_arr_mapped)
        row_add_syn = "INSERT INTO " + table + " (" + columns + ") VALUES(" + values_str + ")"
        curs.execute(row_add_syn, row_add)  # execute, this executes the sql statement provided by row_add_sy
    elif row_syn is not None:
        curs.execute(row_syn)
    conn.commit()  # This saves the changes
    return curs.lastrowid


# insert row but also checks that the ingredients are valid
def insert_row_valid(conn, table, columns, row_add, row_syn):
    """! This function performs a check to make sure the ingredients of a recipe
    are valid ingredients.
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to change
    @param columns  a string that represents all of the columns, split by commas
    @param row_add  a tuple with values for all of the necessary columns
    @param row_syn  a string that represents the proper command to correctly execute an insertion
    @return returns true if it was correctly inserted, false otherwise"""
    curs = conn.cursor()
    (cuisine, ingredients, steps) = row_add
    if check_valid_ingredient(conn, "ingredients_val", ingredients.split(',')):
        insert_row(conn, table, columns, row_add, row_syn)
        return True
    else:
        return False


# Updates data in the recipe table
def update_table(conn, table, columns_update, row_identify, row_update, row_syn):
    """! either executes the command given by row_syn or formats the proper command using
    the provided, table, columns_update, check_row, row_update. The command will update
    the columns in the rows specified
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to change
    @param columns_update  an array that stores all of the columns to update
    @param row_identify    this is a string that contains the identifier to specify which rows to update
    @param row_update  a tuple with values for all of the necessary columns and the row_identifier
    @param row_syn  a string that represents the proper command to correctly execute an update
    """
    curs = conn.cursor()
    if row_update is not None:
        col_str = map(lambda x: x + "=?", columns_update)
        columns_change = ','.join(col_str)
        identifier = row_identify + "=?"
        row_up_syn = "UPDATE " + table + " SET " + columns_change + " WHERE " + identifier
        curs.execute(row_up_syn, row_update)
    elif row_syn is not None:
        curs.execute(row_syn)
    else:
        raise Exception('Invalid Parameter')
    conn.commit()


# returns an iterator rows for all of the rows
def select_all_rows(conn, table):
    """ This selects all of the rows in the provided table and returns them
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to get the rows
    @return an iterable for all rows
    """
    curs = conn.cursor()
    curs.execute("SELECT * FROM " + table)
    rows = curs.fetchall()
    return rows


# returns an iterator for rows, that match input
def select_row_priority(conn, table, column, value):
    """ This selects all of the rows in the provided table that match the specified value in
    the specified column.
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to get the rows
    @param column   a string that represents the column that is being checked
    @param value    the value that is being looked for in the table
    @return an iterable for all rows that match the column and value
    """
    curs = conn.cursor()
    if column is not None:
        try:
            curs.execute("SELECT * FROM " + table + " WHERE " + column + "=?", (value,))
        except Error as e:
            print(e)
    else:
        raise Exception('Invalid parameters')

    return curs.fetchall()


# deletes a row that matches the given parameters
def delete_row_priority(conn, table, column, value):
    """! deletes a row from the provided table that matches the specified value, looking for
    that value in the provided column.
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to get the rows
    @param column   a string that represents the column that is being checked
    @param value    the value that is being looked for in the table
    """
    curs = conn.cursor()
    if column is not None:
        try:
            curs.execute("DELETE FROM " + table + " WHERE " + column + "=?", (value,))
            conn.commit()
        except Error as e:
            print(e)
    else:
        raise Exception('Invalid parameters')


# Checks for valid ingredients
def check_valid_ingredient(conn, table, ingredients):
    """! iterates through the ingredients provided, checks if it exists in the table,
    then returns false if any ingredients did not exist.
    @param conn    a connection object that represents the current database
    @param table    a string that represents the name of the table to get the rows
    @param ingredients  an iterable, preferably array, that contains all ingredients that need to be checked
    @return true if ALL ingredients are valid, otherwise returns false"""
    curs = conn.cursor()
    for i in ingredients:
        i = i.strip()
        subquery = "SELECT 1 FROM " + table + " WHERE valid_ingredients=" + "\'" + i + "\'"
        comm_ex = "SELECT EXISTS(" + subquery + ")"
        curs.execute(comm_ex)
        tuple_exist = curs.fetchall().pop()
        fnd_row = tuple_exist[0]
        if fnd_row == 0:
            return False

    return True


def main():
    table_one = "CREATE TABLE IF NOT EXISTS recipes " \
                "(id integer PRIMARY KEY, cuisine text, ingredients text NOT NULL, steps text UNIQUE);"
    table_two = "CREATE TABLE IF NOT EXISTS ingredients_val " \
                "(id integer PRIMARY KEY, valid_ingredients text UNIQUE, quantity text);"

    database_path = file_path_global
    conn = create_connection(database_path)

    if conn is not None:
        create_table(conn, table_one)
        create_table(conn, table_two)
    else:
        print("Error!")

    ingredients = [("soda", "cups"), ("cheese", "cups"), ("pasta", "cups"), ("crack", "cups")]
    for i in ingredients:
        try:
            row_id = insert_row(conn, "ingredients_val", "valid_ingredients, quantity", i, None)
        except Error as e:
            print(e)

    row_to_add = ("american", "milk, cheese, pasta", "1. cook pasta\n2. combine milk and cheese")
    try:
        row_id = insert_row(conn, "recipes", "cuisine, ingredients, steps", row_to_add, None)
    except Error as e:
        print(e)

    row_to_add_two = ("american", "cheese, egg", "1. scramble eggs\n2. combine eggs and cheese")
    # try:
    #     row_id = insert_row(conn, "recipes", "cuisine, ingredients, steps", row_to_add_two, None)
    # except Error as e:
    #     print(e)

    try:
        truth = insert_row_valid(conn, "recipes", "cuisine, ingredients, steps", row_to_add_two, None)
    except Error as e:
        print(e)

    update_table(conn, "recipes", ["cuisine"], "id", ("italian", 1), None)
    update_table(conn, "ingredients_val", ["valid_ingredients"], "id", ("milk", 1), None)
    delete_row_priority(conn, "ingredients_val", "id", 4)
    # delete_row_priority(conn, "recipes", 1, None, None, None)  # comment out and in to check for deletion
    rows_all = select_all_rows(conn, "recipes")
    rows_cuisine = select_row_priority(conn, "recipes", "cuisine", "american")
    valid_ingredients = select_all_rows(conn, "ingredients_val")

    for i in rows_all:
        print("row: ", i)

    for i in rows_cuisine:
        print("row: ", i)

    for i in valid_ingredients:
        print("row: ", i)
    conn.close()


if __name__ == '__main__':
    main()

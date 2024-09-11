'''Script containing common functionality for interacting with the SQLite database.

The tasks required of the database are:
    1. To extract lists of recipe names; ingredient names; tag names.
    2. To extract an entire recipe: name, ingredients, tags and instructions.
    3. To create meals and insert all information into the db correctly.

Task 1 can be done simply with "SELECT <var> FROM <table>;" querys.
Task 2 can be completed via SELECT statements with the appropriate JOIN clauses.
Task 3 can be done by first attempting to insert the new name into the recipes TABLE. If this is succesful (i.e. unique recipe name) then the id of the recipe can be obtained and new ingredients/tags can be inserted in similar fashion. The relation tables can then be populated to link the information.

This script assumes that the database adheres to the schema in mealplanner.schema
'''

import sqlite3 as sql

type Cursor = sql.Cursor

def get_all_names_from_table(cur: Cursor, table: str) -> list[str]:
    '''Function that extracts all of the "name" entries in the provided table, and returns them as a list.'''
    res = cur.execute(f"SELECT name FROM {table}") # this is explicitly suggested against, but table names cannot be passed in as ? or :arg syntax
    names = res.fetchall()
    names = [tup[0] for tup in names]
    return names


def get_all_recipe_names(cur: Cursor):
    return get_all_names_from_table(cur, "recipes")


def get_all_ingredient_names(cur: Cursor):
    return get_all_names_from_table(cur, "ingredients")


def get_all_tags_names(cur: Cursor):
    return get_all_names_from_table(cur, "tags")


def extract_recipe(cur: Cursor, recipe_name: str):
    recipe_ids = cur.execute("SELECT id FROM recipes WHERE name=:name", {'name':recipe_name}).fetchall()
    if recipe_ids is None:
        return None

    if len(recipe_ids) > 1:
        raise ValueError(f"Should only be 1 recipe with name {recipe_name}, but received {len(recipe_ids)} ids: {recipe_ids}")

    recipe_id = recipe_ids[0][0]
    instructions = {
        ordering: instruction
        for (ordering, instruction) in cur.execute("""
            SELECT ordering, content FROM instructions
            INNER JOIN recipes ON instructions.recipe_id=:recipe_id
            """, {'recipe_id':recipe_id}
        ).fetchall()
    }
    ingredients = [
        ing_tup[0] for ing_tup in cur.execute("""
        SELECT ingredients.name FROM ingredients_in_recipe
        INNER JOIN ingredients ON ingredients.id=ingredients_in_recipe.ingredient_id
        WHERE ingredients_in_recipe.recipe_id=:recipe_id
        """, {'recipe_id': recipe_id}
        ).fetchall()
    ]
    tags = [
        tag_tup[0] for tag_tup in cur.execute("""
        SELECT tags.name FROM tags
        INNER JOIN tags_for_recipe ON tags_for_recipe.tag_id=tags.id
        WHERE tags_for_recipe.recipe_id=:recipe_id
        """, {'recipe_id': recipe_id}
        ).fetchall()
    ]
    return (recipe_name, ingredients, instructions, tags)



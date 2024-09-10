# `MealPlanner` - Python edition

This is the python edition of MealPlanner. 

## Usage

To run the meal planner, the steps required are:

1) Clone the repository to your local machine where you intend to use `MealPlanner`.
2) Create a new python environment to install the MealPlanner package into.
3) From within this directory, run `python -m pip install -e .` to create a local install of the package.
4) Run `python MealPlanner.py`!


## SQLite

### Schema

The SQLite schema is described in [SQLITE_SCHEMA.md](./SQLITE_SCHEMA.md).

The database can be initialised using the command
```bash
sqlite3 mealplanner.db < mealplanner.schema
```

The `sqlite3` utility can then be used to insert entries into the database.

### Test initialisation

The file [db_init.sql](./tests/db_init.sql) contains instructions to initialise values within the schema.

A test database can be insitialised through the following command:
```
sqlite3 test.db < mealplanner.schema && sqlite3 test.db < tests/db_init.sql
```

From this state, the database can be opened and editted as so:
```
> sqlite3 test.db < mealplanner.schema && sqlite3 test.db < tests/db_init.sql
> sqlite3 test.db

SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.

sqlite> SELECT ingredients.name
   ...> FROM ingredients_in_recipe INNER JOIN ingredients ON ingredients.id=ingredients_in_recipe.ingredient_id
   ...> INNER JOIN recipes ON recipes.id=ingredients_in_recipe.recipe_id
   ...> WHERE recipes.id=1;
tinned tomatoes
onions
garlic
olives
capers
tuna
sundried tomatoes
lemon juice
herbs
pasta
tomato puree

sqlite> SELECT tags.name
   ...> FROM tags_for_recipe
   ...> INNER JOIN tags ON tags.id=tags_for_recipe.tag_id
   ...> INNER JOIN recipes ON recipes.id=tags_for_recipe.recipe_id
   ...> WHERE recipes.id=2;
veggie
comfort
easy
one pot

sqlite> SELECT tags.name
   ...> FROM tags_for_recipe
   ...> INNER JOIN tags ON tags.id=tags_for_recipe.tag_id
   ...> INNER JOIN recipes ON recipes.id=tags_for_recipe.recipe_id
   ...> WHERE recipes.id=3;
veggie
spicy
comfort

sqlite> .quit
```

# SQLite schema

In this document, I will attempt to create an SQLite schema for the project that contains all of the required functionality. I will also attempt to explain why each design choice has been made.

The tables included will be:

 + recipes: names of the recipes saved, with unique id's
 + ingredients: names and associated unique id's of ingredients
 + tags: tags for the recipes, and associated unique id's
 + instructions: an ordering (integer), content (string) and associated recipe id (foreign key) so that instruction lists can be retreived.
 + ingredients\_in\_recipe: a recipe id, and an ingredient id, linking the two tables
 + tags\_in\_recipe: a recipe id, and a tag id, linking the two tables.

 ## `recipes`

 ```SQL
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY ASC,
    name TEXT UNIQUE ON CONFLICT ABORT
    time_prep INTEGER NOT NULL,
    time_cook INTEGER NOT NULL
)
 ```

 ## `ingredients`

 ```SQL
CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY ASC,
    name TEXT UNIQUE ON CONFLICT ABORT
)
 ```

 ## `Tags`

 ```SQL
CREATE TABLE tags (
    id INTEGER PRIMARY KEY ASC,
    name TEXT UNIQUE ON CONFLICT ABORT
)
 ```

 ## `instructions`

 ```SQL
CREATE TABLE instructions (
    recipe_id INTEGER REFERENCES recipes (id),
    ordering INTEGER NOT NULL,
    content TEXT NOT NULL
)
 ```

 ## `ingredients_in_recipe`

 ```SQL
CREATE TABLE ingredients_in_recipe (
    recipe_id INTEGER REFERENCES recipes (id),
    ingredient_id INTEGER REFERENCES ingredients (id)
)
 ```

 ## `tags_for_recipe`

 ```SQL
CREATE TABLE tags_for_recipe (
    recipe_id INTEGER REFERENCES recipes (id),
    tag_id INTEGER REFERENCES tags (id)
)
 ```

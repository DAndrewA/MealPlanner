# `MealPlanner` - Python edition

This is the python edition of MealPlanner. 

## Usage

To run the meal planner, the steps required are:

1) Clone the repository to your local machine where you intend to use `MealPlanner`.
2) Create a new python environment to install the MealPlanner package into.
3) From within this directory, run `python -m pip install -e .` to create a local install of the package.
4) Run `python MealPlanner.py`!


## SQLite

The SQLite schema is described in [SQLITE_SCHEMA.md](~/SQLITE_SCHEMA.md).

The database can be initialised using the command
```bash
sqlite3 mealplanner.db < mealplanner.schema
```

The `sqlite3` utility can then be used to insert entries into the database.

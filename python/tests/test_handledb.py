import sqlite3 as sql
from meal_planner import handledb as hdb

def format_recipe(name, ingredients, instructions, tags):
    print("="*30 + "\n")
    print(f"{name.upper():^30}")
    print("\n"*2)
    print(" "*5 + f"{'INGREDIENTS':<25}\n")
    for i in ingredients:
        print(" "*8 + f"{i:<23}")
    print("\n")
    for k, v in instructions.items():
        print(" "*5 + f"{k:>2}:{v}")
    print("\n")
    for t in tags:
        print(f"{t}, ",end='')
    print("")

db = sql.connect("./test.sqlite")
cur = db.cursor()
for r in ("fishy pasta", "tuscan chickpeas", "sweet potato curry"):
    n,i,inst,t = hdb.extract_recipe(cur, r)
    format_recipe(n,i,inst,t) 

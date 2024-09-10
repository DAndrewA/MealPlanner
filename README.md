# MealPlanner
Have you ever thought to yourself one Tuesday evening _what the hell is in the fridge and what do I have to eat for the rest of thew week? :(_ I have semi-regularly found myself in this situation, and then fall back on the same 3 easy-to-cook meals for weeks on end.

No more.

With `MealPlanner` it will be easy to plan ahead at the start of the week - meals for the following days, matching the requirements of your schedule. Need a quick meal on Monday? Sorted. Adhearing to veggie-wedensday? Sorted.

## The plan

My plan is to create 2 versions of the application, one in Python (in which I have some experience), and the second in Rust which I have been recently learning. Doing the project twice, in seperate languages, will give me a chance to get to grips with the problems posed by the project in a language I am comfortable with initially, and in the second run I can focus more on practicing my skills in the new language rather than worrying about the specific implememntation. 

## Aims

 - [ ] Have robust error handling throughout the program for user input, file handling, etc.
 - [ ] Create a local SQLite database to store information about recipes.
 - [ ] Have an insterface to make recipe entries into the database, including a title, ingredients and steps required.
 - [ ] Have an interface for listing and reading recipes from the SQLite database. 
 - [ ] Have an interface for creating a list of meals for a week.
 - [ ] Have each seperate function be available from the command line, or through a TUI interface.
 - [ ] In the meal planning, implement features to customise what meals are used in certain slots (i.e. vegetarian meals, quick meals; through a tagging system)
 - [ ] In the recipe listing, implement a basic fuzzy matching algorithm to allow users to better search for specific recipes, by title, ingredients, tags.

## Python

The first part coded will be in Python, to hash out the idea and gain familiarity with the sqlite database handling.



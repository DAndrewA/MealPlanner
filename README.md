# MealPlanner
Have you ever thought to yourself one Tuesday evening _what the hell is in the fridge and what do I have to eat for the rest of thew week? :(_ I have semi-regularly found myself in this situation, and then fall back on the same 3 easy-to-cook meals for weeks on end.

No more.

With `MealPlanner` it will be easy to plan ahead at the start of the week - meals for the following days, matching the requirements of your schedule. Need a quick meal on Monday? Sorted. Adhearing to veggie-wedensday? Sorted.

## The plan

My plan is to create 2 versions of the application, one in Python (in which I have some experience), and the second in Rust which I have been recently learning. Doing the project twice, in seperate languages, will give me a chance to get to grips with the problems posed by the project in a language I am comfortable with initially, and in the second run I can focus more on practicing my skills in the new language rather than worrying about the specific implememntation. 

## Aims

+ create a CL app with robust input error handling
+ Store, retrieve data using a sqlite database
+ Have 4 modes of functionality for the "binary"
    1. Write a new recipe to the database
    2. List recipes in the database
    3. Produce a list of meals for the week, with a provided shopping list
    4. If no prior option is specified when calling the binary, load an interface that allows for all of the above options (extension)

## Python

The first part coded will be in Python, to hash out the idea and gain familiarity with the sqlite database handling.

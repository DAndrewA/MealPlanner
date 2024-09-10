INSERT INTO recipes (id, name, time_prep, time_cook) VALUES 
    (1,"fishy pasta", 3, 10),
    (2,"tuscan chickpeas", 10, 25),
    (3,"sweet potato curry", 15, 30);

INSERT INTO ingredients (name) VALUES 
    ("tinned tomatoes"),
    ("onions"),
    ("garlic"),
    ("olives"),
    ("capers"),
    ("tuna"),
    ("sundried tomatoes"),
    ("chickpeas"),
    ("mustard"),
    ("coconut milk"),
    ("lemon juice"),
    ("herbs"),
    ("pasta"),
    ("tomato puree"),
    ("sweet potato"),
    ("spinach"),
    ("aubergine"),
    ("tumeric"),
    ("pepper");

INSERT INTO tags (name) VALUES
    ("quick"),
    ("veggie"),
    ("spicy"),
    ("comfort"),
    ("easy"),
    ("one pot");

INSERT INTO instructions (recipe_id, ordering, content) VALUES
    (1, 1, "Chop the onions and garlic. Put the kettle on to boil."),
    (1, 2, "Set the pasta boiling for 10 minutes."),
    (1, 3, "Start frying the onions and garlic."),
    (1, 4, "Chop up the olives and sundried tomatoes, and add them to the onions and garlic."),
    (1, 5, "Add the capers, tuna, and some tomatoe puree, and mix."),
    (1, 6, "Add the tinned tomatoes, bring to the boil, and add salt, pepper and herbs to taste."),
    (1, 7, "Once drained, mix the pasta into the sauce and serve."),
    (2, 1, "Chop the onions and garlic, and place in a large pot to begin frying."),
    (2, 2, "Drain the chickpeas. Once the onions have softened, add the chickpeas to the pot."),
    (2, 3, "Pour the coconut milk and vegetable stock into the pot and bring to a low simmer."),
    (2, 4, "Add the dijon mustard, enough to taste. Add the herbs and lemon juice too."),
    (2, 5, "Put the orzo into the sauce, bring to a simmer and leave to cook for 7-8 minutes."),
    (2, 6, "Optionally, wilt some spinach in the pot. Serve once the orzo is cooked."),
    (3, 1, "Preheat the oven to 180 degrees C."),
    (3, 2, "Cube the sweet potato and aubergine. Apply spices, oil, and cook in the oven, mixing occasionaly."),
    (3, 3, "Chop some onions and garlic, and start frying in a pan with some cumin seeds."),
    (3, 4, "Chop a pepper and add to the pan."),
    (3, 5, "Add tinned tomatoes or coconut milk to the pan. Add spices to taste."),
    (3, 6, "Cook some rice for 10 minutes. Once cooked, serve with the curry sauce and roasted sweet potato and aubergine.");

INSERT INTO ingredients_in_recipe (recipe_id, ingredients_id) VALUES
    (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,11), (1,12), (1,13), (1,14),
    (2,2), (2,3), (2,7), (2,8), (2,9), (2,10), (2,11), (2,12), (2,13), (2,14), (2,16),
    (3,1), (3,2), (3,3), (3,8), (3,10), (3,11), (3,14), (3,15), (3,16), (3,17), (3,18), (3,19);  

INSERT INTO tags_for_recipes (recipe_id, tag_id) VALUES
    (1,1), (1,4), (1,5),
    (2,2), (2,4), (2,5), (2,6),
    (3,2), (3,3), (3,4);


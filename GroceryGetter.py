import os
import json

INSTACART_URL = "https://www.instacart.com/store/partner_recipe?recipe_url=https%3A%2F%2Fwww.yummly.com%2F%23recipe%2FTurkey-Meatloaf-2250020&partner_name=www.yummly.com"
INGREDIENT_CODE = "&ingredients%5B%5D="
MEALS_PATH = "/Users/kyle/python/GroceryGetter/meals"
INGREDIENTS_PATH = "/Users/kyle/python/GroceryGetter/Ingredients.json"

def read_meals(directory):
    meals = {}
    for dir in os.walk(directory):
        for file in dir[2]:
            fileSplit = file.split(".")
            meals[fileSplit[0]] = file
    return meals

def read_json(json_file):
    jsonString = ""
    for line in open(json_file, 'r'):
        jsonString += line
    return json.loads(jsonString)

def urlify(ingredient):
    return "+".join(ingredient.split(" "))

# get all meals from meals file
meals = read_meals(MEALS_PATH)

# get ingredients list
ingredients = read_json(INGREDIENTS_PATH)

# print meals out for user to select from
for meal in meals:
    print ("{0}".format(meal))

# get selected meals from user
selectedMeals = input("Enter a comma separated list of meals: \n")

# add all items to the grocery list
groceryList = {}
for meal in selectedMeals.split(","):
    meal = meal.strip(" ")
    mealIngredients = read_json("{0}/{1}".format(MEALS_PATH, meals[meal]))

    for k,v in mealIngredients.items():
        if k in groceryList:
            groceryList[k] += v
        else:
            groceryList[k] = v

# print out all items in the grocery list
for k,v in groceryList.items():
    unit = ingredients[k]
    print ("{0}: {1} {2}".format(k,v,unit))

# create a instacart url
instacartURL = ""
instacartURL += INSTACART_URL
#for k,v in groceryList.items():
#   instacartURL += INGREDIENT_CODE
#   instacartURL += urlify(k)

#print instacartURL

import csv
import random

# Define the recipe data file name
RECIPE_FILE = "recipes.csv"

def main():
    # Load existing recipes from the file
    recipes = load_recipes()

    while True:
        print("Recipe Organizer")
        print("1. Add Recipe")
        print("2. Search Recipes")
        print("3. Generate Meal Plan")
        print("4. Generate Shopping List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            search_recipes(recipes)
        elif choice == "3":
            generate_meal_plan(recipes)
        elif choice == "4":
            generate_shopping_list(recipes)
        elif choice == "5":
            save_recipes(recipes)
            print("Exiting Recipe Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

def load_recipes():
    """Load recipes from the recipe file and return a list of dictionaries."""
    try:
        with open(RECIPE_FILE, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    """Save the recipes to the recipe file."""
    with open(RECIPE_FILE, "w", newline="") as file:
        fieldnames = ["Name", "Ingredients", "Instructions"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(recipes)

def add_recipe(recipes):
    """Add a new recipe to the recipe list."""
    print("Add a New Recipe")
    name = input("Enter the recipe name: ").capitalize()
    ingredients = input("Enter the ingredients (separated by commas): ")
    instructions = input("Enter the instructions: ")

    recipe = {"Name": name, "Ingredients": ingredients, "Instructions": instructions}
    recipes.append(recipe)
    print("Recipe added successfully!\n")

def search_recipes(recipes):
    """Search recipes based on user input."""
    keyword = input("Enter a keyword to search for in recipe names or ingredients: ")
    matching_recipes = []

    for recipe in recipes:
        if keyword.lower() in recipe["Name"].lower() or keyword.lower() in recipe["Ingredients"].lower():
            matching_recipes.append(recipe)

    if matching_recipes:
        print(f"Found {len(matching_recipes)} matching recipes:")
        for recipe in matching_recipes:
            print_recipe(recipe)
    else:
        print("No recipes found.\n")

def generate_meal_plan(recipes):
    """Generate a meal plan for a specified number of days."""
    num_days = int(input("Enter the number of days for the meal plan: "))
    meal_plan = []

    for _ in range(num_days):
        random_recipe = random.choice(recipes)
        meal_plan.append(random_recipe)

    print("Generated Meal Plan:")
    for i, recipe in enumerate(meal_plan, start=1):
        print(f"Day {i}:")
        print_recipe(recipe)

def generate_shopping_list(recipes):
    """Generate a shopping list based on selected recipes."""
    selected_recipes = []

    print("Select Recipes for Shopping List (Enter 'done' to finish selection)")
    while True:
        recipe_name = input("Enter recipe name: ")
        if recipe_name.lower() == "done":
            break

        for recipe in recipes:
            if recipe["Name"].lower() == recipe_name.lower():
                selected_recipes.append(recipe)
                break
        else:
            print("Recipe not found. Please try again.\n")

    shopping_list = []
    for recipe in selected_recipes:
        ingredients = recipe["Ingredients"].split(",")
        shopping_list.extend(ingredients)

    print("Generated Shopping List:")
    for item in shopping_list:
        print(item.strip())

def print_recipe(recipe):
    """Print the details of a recipe."""
    print(f"Name: {recipe['Name']}")
    print("Ingredients:")
    ingredients = recipe["Ingredients"].split(",")
    for ingredient in ingredients:
        print("- " + ingredient.strip())
    print("Instructions:")
    print(recipe["Instructions"])
    print()

if __name__ == "__main__":
    main()

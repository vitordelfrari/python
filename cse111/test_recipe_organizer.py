import pytest
from unittest.mock import patch
from io import StringIO
import recipe_organizer

@pytest.fixture
def recipes():
    return [
        {"Name": "Pasta", "Ingredients": "Pasta, Tomato Sauce, Cheese", "Instructions": "Cook pasta, mix with sauce, and top with cheese."},
        {"Name": "Salad", "Ingredients": "Lettuce, Tomatoes, Cucumbers", "Instructions": "Wash and chop vegetables, then toss together."},
        {"Name": "Pizza", "Ingredients": "Dough, Tomato Sauce, Cheese, Toppings", "Instructions": "Roll out dough, spread sauce, add cheese and toppings, then bake."}
    ]

@patch('builtins.input', side_effect=["Pizza", "Dough, Tomato Sauce, Cheese, Toppings", "Roll out dough, spread sauce, add cheese and toppings, then bake."])
def test_add_recipe(mock_input, recipes):
    recipe_organizer.add_recipe(recipes)
    assert len(recipes) == 4

@patch('builtins.input', return_value="Pasta")
def test_search_recipes_matching(mock_input, recipes, capsys):
    recipe_organizer.search_recipes(recipes)
    captured = capsys.readouterr()
    assert "1 matching recipes" in captured.out

@patch('builtins.input', return_value="Chicken")
def test_search_recipes_not_matching(mock_input, recipes, capsys):
    recipe_organizer.search_recipes(recipes)
    captured = capsys.readouterr()
    assert "No recipes found" in captured.out

@patch('builtins.input', return_value="3")
def test_generate_meal_plan(mock_input, recipes, capsys):
    recipe_organizer.generate_meal_plan(recipes)
    captured = capsys.readouterr()
    assert captured.out.count("Day") == 3

@patch('builtins.input', side_effect=["Pizza", "done"])
def test_generate_shopping_list(mock_input, recipes, capsys):
    recipe_organizer.generate_shopping_list(recipes)
    captured = capsys.readouterr()
    assert "Dough" in captured.out
    assert "Cheese" in captured.out
    assert "Toppings" in captured.out

pytest.main(["-v", "--tb=line", "-rN", __file__])
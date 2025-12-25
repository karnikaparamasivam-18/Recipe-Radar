import requests

def find_meal_options(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    data = requests.get(url).json()
    return data.get("meals", [])

def fetch_full_recipe(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    data = requests.get(url).json()
    return data.get("meals", [None])[0]
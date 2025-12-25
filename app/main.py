import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
# Make sure your .env has GEMINI_API_KEY=AIza...
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"), http_options=types.HttpOptions(api_version='v1'))

def get_best_model():
    """Automatically finds the best available Flash model to avoid 404 errors."""
    for m in client.models.list():
        if 'generateContent' in m.supported_actions and 'flash' in m.name:
            return m.name
    return "gemini-2.0-flash" # Fallback

def start_recipe_project(image_path):
    model_name = get_best_model()
    print(f"Using model: {model_name}")
    
    img = Image.open(image_path)
    
    # We ask for BOTH ingredients and the recipe in one go to save requests
    prompt = """
    1. List all food ingredients you see in this image.
    2. Suggest list of existing recipes that I can make with them with only names of the recipes fetch the recipes present in mealdb api.
    """
    
    print("AI is thinking...")
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt, img]
    )
    return response.text

if __name__ == "__main__":
    result = start_recipe_project("test2.jpg")
    print(result)
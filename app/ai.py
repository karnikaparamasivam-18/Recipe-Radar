import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version='v1')
)

def get_ingredients_from_image(image_path):
    try:
        img = Image.open(image_path)
        
        # FIX: Added '-preview' to the model name
        # Alternatively, use 'gemini-2.5-flash' which is the stable version
        model_name = "gemini-3-flash-preview" 
        
        prompt = "Identify all food ingredients in this image. Return them as a comma-separated list."
        
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt, img]
        )
        
        return [i.strip().lower() for i in response.text.split(",")]
    except Exception as e:
        print(f"Gemini Error: {e}")
        return []
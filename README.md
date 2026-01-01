Recipe-Radar
Overview
  Recipe-Radar is a Python-based backend application that uses artificial intelligence to analyze images of food ingredients and suggest matching recipes. By integrating Google's Gemini AI for image processing and the MealDB API for recipe data, it helps users discover meal ideas based on available ingredients.

Features
  AI-Powered Ingredient Detection: Upload an image, and Gemini AI identifies all visible food ingredients.
  Recipe Suggestions: Automatically queries the MealDB API to find recipes that can be made with the detected ingredients.
  Modular Architecture: Clean separation of concerns with dedicated modules for AI processing, API interactions, and main logic.
  Error Handling: Graceful handling of API errors and missing data.

Project Structure

  main.py: Main entry point that orchestrates image analysis and recipe suggestions.
  ai.py: Handles AI-based ingredient extraction from images using Gemini.
  recipes.py: Manages API calls to MealDB for searching and fetching recipes.
  __pycache__: Auto-generated Python bytecode (ignore).

Dependencies

  google-genai: For interacting with Google's Gemini AI.
  Pillow: For image processing.
  python-dotenv: For loading environment variables.
  requests: For HTTP requests to external APIs.
  
API Integrations
  Gemini AI: Used for image analysis and content generation.
  MealDB API: Provides recipe data and search functionality.

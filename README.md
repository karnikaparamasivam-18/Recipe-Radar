#  Recipe-Radar

##  Overview
Recipe-Radar is a Python-based backend application that uses artificial intelligence to analyze images of food ingredients and suggest matching recipes. By integrating Google’s Gemini Vision AI for image processing and TheMealDB API for recipe data, it helps users discover meal ideas based on available ingredients.

---

##  Features

- **AI-Powered Ingredient Detection**  
  Upload an image of food ingredients and automatically identify all visible items using Gemini Vision models.

- **Recipe Suggestions**  
  Automatically queries TheMealDB API to find recipes that can be prepared using the detected ingredients.

- **Modular Architecture**  
  Clean separation of concerns with dedicated modules for AI processing, recipe retrieval, and application logic.

- **Robust Error Handling**  
  Graceful handling of API failures, empty responses, and rate-limit issues.

- **Scalable Backend Design**  
  Designed to support UI frameworks such as Gradio, Streamlit, or FastAPI.

---

## How It Works

1. The user uploads an image containing food ingredients.
2. Gemini Vision AI analyzes the image and extracts visible ingredients.
3. Extracted ingredients are sent to TheMealDB API.
4. Matching recipes are fetched and returned to the user.
5. Errors and edge cases are handled gracefully to ensure application stability.

---

## API Integrations

### Google Gemini AI
- Used for image analysis and ingredient extraction
- Supports multimodal input (text + image)

### TheMealDB API
- Provides recipe names, instructions, images, and video links
- Free public REST API

---

## Dependencies

- `google-genai` – Interaction with Google Gemini AI  
- `Pillow` – Image processing  
- `python-dotenv` – Environment variable management  
- `requests` – HTTP requests to external APIs  

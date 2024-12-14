import os
from dotenv import load_dotenv
import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from app.exceptions.custom_exceptions import CustomException

load_dotenv()

def load_model():
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise CustomException("Missing API key", "Environment variable GOOGLE_API_KEY is not set")
        
        genai.configure(api_key=api_key)
        return Gemini(model="models/gemini-pro", api_key=api_key)
    except Exception as e:
        raise CustomException("Failed to load model", e)



import os
from dotenv import load_dotenv
from google import genai

# Load the key from your local .env file
load_dotenv(override=True)

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

print("Testing API key...")

if not API_KEY:
    print("FAILED: GEMINI_API_KEY was not found in .env")
else:
    print("API key found in .env. Testing Gemini connection...")

    try:
        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="Say hello in one short sentence.",
        )

        print("SUCCESS! Gemini API is working.")
        print(response.text)

    except Exception as e:
        print("FAILED. Error details:")
        print(type(e).__name__)
        print(str(e))

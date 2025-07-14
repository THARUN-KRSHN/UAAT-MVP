import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_response(text, mode, retries=3, wait_seconds=10):
    prompt = f"Explain: {text}" if mode == "standard" else f"Explain in detail: {text}"
    
    for attempt in range(1, retries + 1):
        try:
            response = model.generate_content(
                prompt,
                generation_config={"max_output_tokens": 200}
            )
            return response.text
        
        except ResourceExhausted as e:
            print(f"[Retry {attempt}] Quota exceeded. Waiting {wait_seconds} seconds...")
            time.sleep(wait_seconds)
        
        except Exception as e:
            return f"[Unexpected Error] {str(e)}"
    
    return "[Error] Request failed after retries. Try again later."

# 🔍 Test
if __name__ == "__main__":
    print(generate_response("What is AI?", "deep"))

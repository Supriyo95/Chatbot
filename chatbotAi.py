
import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyD9s8zMyc4cqjmjvuOrCIN3fCTNEoqyt3Q")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

def handle_user_query(query: str):
    response = model.generate_content(query)
    output = re.sub(r'[*_]', '', response.text)
    print(f"Here's your answer (BOT): {output}")

    try:
         with open("google-res.txt", 'w', encoding='utf-8') as file:
            file.write(output)
    except Exception as e:
        print(f"Error: {e}")
        return None
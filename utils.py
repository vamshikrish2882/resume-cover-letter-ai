import os
from dotenv import load_dotenv
import together

load_dotenv()
together.api_key = os.getenv("TOGETHER_API_KEY")

def generate_text(prompt):
    try:
        response = together.Complete.create(
            prompt=prompt,
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            max_tokens=500,
            temperature=0.7,
            top_k=50,
            top_p=0.7,
            repetition_penalty=1.1,
        )

        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['text'].strip()
        else:
            return " No output received. Check prompt or model response format."

    except Exception as e:
        return f" Error: {str(e)}"

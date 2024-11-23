from django.conf import settings
import requests
import re

def rephrase_text(text: str):
    url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct"
    headers = {
        "Authorization": f"Bearer {settings.HUGGING_FACE_API_KEY}"
    }
    payload = {
        "inputs": f"Convert this to a professional email: {text}",
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 1024,
            "top_p": 0.95
        }
    }


    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:

        generated_text = response.json()[0]['generated_text']

        formatted_text = generated_text.replace('[Recipient\'s Name],', '[Recipient\'s Name],\n') 
        formatted_text = formatted_text.replace('[Subject]', '\n[Subject]\n')
        formatted_text = formatted_text.replace('[Body]', '\n[Body]\n')
        formatted_text = formatted_text.replace('[Closing]', '\n[Closing]\n')

        
        formatted_text = re.sub(r'(?<!\w)\[ | \](?!\w)', '', formatted_text)    # Remove unmatched `[` or `]`

        return formatted_text

    else:
        return "There was an error rephrasing the text."
        
    


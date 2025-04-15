import requests
import uuid
import os

HUGGINGFACE_API_KEY = "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"  

def generate_image(prompt: str) -> str:
    api_url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        filename = f"generated_images/{uuid.uuid4().hex}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        print(f"Image generation failed: {response.status_code}, {response.text}")
        return ""

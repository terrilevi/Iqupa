from flask import Flask, request
import base64
import os
import requests
import json


image_path = "/home/moises/Documents/TestCamera/images/photo.jpg"
if os.path.isfile(image_path):
    print("File exists.")
else:
    print("File does not exist.")


# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

prompt_text = (
    "Examine the image provided and categorize the visible waste item(s). Use these guidelines: "
    "1 for Organic Waste, 2 for Non-Recyclable Waste, and 3 for Recyclable Waste. "
    "If multiple different items are visible, categorize as Non-Recyclable (2). "
    "If all items are of the same type, categorize them into their appropriate bin. "
    "In cases of uncertainty or non-identifiable items, also categorize as Non-Recyclable (2).\n\n"
    "Respond ONLY with the number of the bin where the items should be placed, without any additional text. "
    "For example, respond with '1', '2', or '3' based on the categorization.\n\n"
    "This format is critical for the automation process in the waste sorting system."
)

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_text},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

response_data = response.json()
content = response_data["choices"][0]["message"]["content"]
print(content)
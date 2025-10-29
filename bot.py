import requests

HF_API_KEY = "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"  # <--- wklej swój pełny token Hugging Face

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

data = {
    "inputs": "Napisz krótki motywacyjny cytat o biznesie po polsku.",
}

response = requests.post(API_URL, headers=headers, json=data)

print("STATUS:", response.status_code)
print("RAW:", response.text)

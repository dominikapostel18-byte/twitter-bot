import requests

# 🔑 Wklej tutaj swój prawidłowy token Hugging Face:
HF_API_KEY = "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"

# 🌐 Adres API Zephyra
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "inputs": "Napisz krótki motywacyjny cytat o biznesie po polsku."
}

response = requests.post(API_URL, headers=headers, json=data)

print("STATUS:", response.status_code)
print("RAW:", response.text)

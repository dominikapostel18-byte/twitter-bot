import os
import random
import json
import requests
import subprocess

# === KONFIG ===
TWEET_URL = "https://api.twitter.com/2/tweets"
TOKENS_FILE = "tokens.json"

# 🔥 ścieżka do folderu stylów
STYLES_DIR = "."


def load_tokens():
    with open(TOKENS_FILE, "r") as f:
        return json.load(f)


def choose_random_style_file():
    """Losuje plik stylu z folderu styles"""
    files = [f for f in os.listdir(STYLES_DIR) if f.endswith(".txt")]
    chosen = random.choice(files)
    return os.path.join(STYLES_DIR, chosen)


def generate_tweet_from_style():
    """Wybiera styl i tworzy prompt dla Ollamy"""
    style_file = choose_random_style_file()
    with open(style_file, "r", encoding="utf-8") as f:
        style_examples = f.read().strip()

    prompt = f"""
You are an AI that writes short, powerful motivational tweets in the style of the examples below.
Never use quotes (" ") or hashtags (#). Never end with a period. 
Stay under 200 characters. Keep it raw, simple, and punchy.

Examples:
{style_examples}

Now generate one new line in the same style:
"""
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    tweet = result.stdout.strip()

    # usuń ewentualne cudzysłowy i kropki na końcu
    tweet = tweet.replace('"', '').replace("'", "")
    if tweet.endswith('.'):
        tweet = tweet[:-1]

    return tweet


def post_tweet(access_token, text):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {"text": text}
    response = requests.post(TWEET_URL, headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ Tweet opublikowany!")
    else:
        print("❌ Błąd:", response.text)


def main():
    tokens = load_tokens()
    access_token = tokens["access_token"]

    tweet_text = generate_tweet_from_style()
    print("🧠 Wygenerowany tweet:", tweet_text)

    post_tweet(access_token, tweet_text)


if __name__ == "__main__":
    main()

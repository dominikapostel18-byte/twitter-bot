# Użyj obrazu Python
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki z repo do kontenera
COPY . .

# Zainstaluj wymagane biblioteki
RUN pip install --no-cache-dir -r requirements.txt

# Uruchom bota
CMD ["python", "bot.py"]

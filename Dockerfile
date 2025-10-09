# Używamy oficjalnego obrazu Ollama + Pythona
FROM ollama/ollama:latest

# Instalacja Pythona
RUN apt-get update && apt-get install -y python3 python3-pip

# Skopiuj pliki bota do kontenera
WORKDIR /app
COPY . /app

# Zainstaluj wymagania
RUN pip3 install -r requirements.txt

# Załaduj model (np. llama3)
RUN ollama pull llama3

# Uruchom Ollamę w tle i potem bota
CMD ollama serve & sleep 5 && python3 bot.py

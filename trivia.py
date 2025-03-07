import requests
from deep_translator import GoogleTranslator

def trivia_fetch(num):
    url = f"http://numbersapi.com/{num}/trivia?json"
    r = requests.get(url).json()
    texto_en = r.get("text", "No disponible")
    texto_es = GoogleTranslator(source="en", target="es").translate(texto_en)
    return {"number": num, "text": texto_es}

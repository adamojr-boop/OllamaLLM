##Esercizio 4
#
# Traccia: Trasforma un set di dati strutturati (come un dizionario Python) in una descrizione testuale completa.
# 
# Obiettivo: Convertire dati strutturati in una descrizione leggibile.

from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("--- GENERATORE DI DESCRIZIONI INTERATTIVO (OLLAMA) ---")
print("Inserisci i dati del prodotto sotto forma di testo (o compila i campi):")

prodotto = input("Nome del prodotto: ")
prezzo = input("Prezzo (€): ")
materiale = input("Materiale: ")
colori = input("Colori disponibili (separati da virgola): ")
stock = input("Pezzi in magazzino (stock): ")

data = {
    "product": prodotto,
    "price": float(prezzo) if prezzo.replace('.', '', 1).isdigit() else prezzo,
    "material": materiale,
    "colors": [c.strip() for c in colori.split(',')],
    "stock": int(stock) if stock.isdigit() else stock
}

print("\n...elaborazione della descrizione in corso...")

completion = client.chat.completions.create(
    model="llama3.1",
    temperature=0.6,
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente copywriter in grado di analizzare un set di dati strutturati e trasformarli in una descrizione testuale chiara, fluida e accattivante, mantenendo tutti i dettagli tecnici inalterati.",
        },
        {"role": "user", "content": str(data)},
    ],
)

print("\n--- DESCRIZIONE COMMERCIALE GENERATA ---")
print(completion.choices[0].message.content)
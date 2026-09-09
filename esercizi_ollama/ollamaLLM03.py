##Esercizio 3
#
# Traccia: Crea un prompt che riassuma un articolo di notizie in un singolo paragrafo di al massimo 255 caratteri.
# 
# Obiettivo: Prendere un testo lungo e condensarlo nei punti essenziali.

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("--- SINTETIZZATORE DI NOTIZIE (OLLAMA) ---")

input_text = input("Inserisci l'articolo o il testo da riassumere: ")

completion = client.chat.completions.create(
    model="llama3.1",
    temperature=0.0,
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente in grado di analizzare testi e fornire sintesi chiare e concise. Riassumi l'articolo fornito dall'utente in un singolo paragrafo di al massimo 255 caratteri, condensandolo nei punti essenziali. Rispondi ESCLUSIVAMENTE con il riassunto, massimo 255 caratteri, senza aggiungere frasi di cortesia o commenti.",
        },
        {"role": "user", "content": input_text},
    ],
)

print("\n--- SINTESI ---")
print(completion.choices[0].message.content)
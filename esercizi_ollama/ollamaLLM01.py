##Esercizio 1:
# 
# Traccia: Scrivi un prompt che traduca un testo dall'italiano all'inglese e viceversa. Usa il prompt per tradurre una breve descrizione di un prodotto.
# 
# Obiettivo: Sviluppare un prompt che sia adatto alla traduzione fluida tra italiano e inglese.

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("--- TRADUTTORE INTERATTIVO ---")

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model="llama3.1",
    temperature=0.0,
    messages=[
        {
            "role": "system",
            "content": "Sei un traduttore professionista. Traduci il testo inserito dall'utente: se è in italiano, traducilo in inglese; se è in inglese, traducilo in italiano. Restituisci ESCLUSIVAMENTE la traduzione, senza aggiungere commenti, introduzioni o frasi di cortesia.",
        },
        {"role": "user", "content": input_text},
    ],
)

print("\n--- RISULTATO TRADOTTO ---")
print(completion.choices[0].message.content)
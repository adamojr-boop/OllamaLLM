from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("--- ESTRATTORE DI INFORMAZIONI ---")

input_text = input("Inserisci il testo descrittivo: ")

completion = client.chat.completions.create(
    model="llama3.1",
    messages=[
        {
            "role": "system",
            "content": "Sei un tool di estrazione dati. Estrai nome, età e professione dal testo fornito dall'utente. Rispondi ESCLUSIVAMENTE con i dati richiesti, in modo chiaro e conciso, senza aggiungere frasi di introduzione o commenti.",
        },
        {"role": "user", "content": input_text},
    ],
)

print("\n--- RISULTATO ESTRATTO ---")
print(completion.choices[0].message.content)
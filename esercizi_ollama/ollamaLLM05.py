##Esercizio 5
# 
# Traccia: Scrivi un prompt che generi domande di comprensione su un breve testo.
# 
#Obiettivo: Sviluppare un prompt per creare domande educative basate su un contenuto.

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

print("--- GENERATORE DI DOMANDE DI COMPRENSIONE ---")

input_text = input("Inserisci il testo di riferimento per generare le domande: ")

print("\n...generazione delle domande in corso...")

completion = client.chat.completions.create(
    model="llama3.1",
    temperature=0.2,
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente didattico specializzato nella creazione di test di verifica. Analizza il testo fornito dall'utente e genera domande educative chiare e pertinenti (un mix di risposta multipla e risposta aperta) per testare la comprensione del testo.",
        },
        {"role": "user", "content": input_text},
    ],
)

print("\n--- DOMANDE GENERATE ---")
print(completion.choices[0].message.content)
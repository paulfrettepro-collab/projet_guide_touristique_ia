"""
Assistant Parisien - Guide touristique IA
Un assistant virtuel qui répond aux questions sur les monuments de Paris
"""

import os
from openai import OpenAI

# Configuration du modèle GPT à utiliser
# J'ai choisi gpt-4o-mini pour un bon équilibre performance/coût
model = "gpt-4o-mini"

# Initialisation du client OpenAI
# La clé API est récupérée automatiquement depuis la variable d'environnement OPENAI_API_KEY
client = OpenAI()

# Historique de la conversation avec l'IA
# J'ai pré-configuré quelques échanges pour donner du contexte au modèle
conversation = [
    {
        "role": "system",
        "content": "You are a travel guide designed to provide information about landmarks that tourists should explore in Paris. You speak in a concise manner."
    },
    {
        "role": "user",
        "content": "What is the most famous landmark in Paris?"
    },
    {
        "role": "assistant",
        "content": "The most famous landmark in Paris is the Eiffel Tower."
    },
]

# Questions prédéfinies pour tester l'assistant
questions = [
    "How far away is the Louvre from the Eiffel Tower (in driving miles)?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

def main():
    """
    Fonction principale qui gère l'interaction avec l'API OpenAI
    """
    print("=== Assistant Parisien - Guide Touristique IA ===\n")
    
    # Traitement de chaque question
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        
        # Ajout de la question à l'historique
        conversation.append({"role": "user", "content": question})
        
        try:
            # Appel à l'API OpenAI
            response = client.chat.completions.create(
                model=model,
                messages=conversation,
                temperature=0.0,  # Température à 0 pour des réponses plus précises
                max_tokens=100
            )
            
            # Extraction et affichage de la réponse
            answer = response.choices[0].message.content
            print(f"Réponse: {answer}\n")
            
            # Sauvegarde de la réponse dans l'historique pour maintenir le contexte
            conversation.append({"role": "assistant", "content": answer})
            
        except Exception as e:
            print(f"Erreur lors de l'appel API: {e}\n")
            continue

if __name__ == "__main__":
    main()
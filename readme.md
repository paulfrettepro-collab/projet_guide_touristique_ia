# 🗼 Assistant Parisien

Un assistant virtuel qui répond aux questions sur Paris en utilisant l'API OpenAI.

## 📋 À propos

J'ai développé ce projet pour pratiquer l'intégration de l'API OpenAI dans une application Python. L'idée était de créer un guide touristique simple qui utilise GPT-4 pour répondre à des questions sur les monuments parisiens.

Ce projet m'a permis de comprendre :
- Comment structurer des appels à l'API Chat Completions
- La gestion du contexte conversationnel (historique des messages)
- L'importance du prompt système pour définir le comportement de l'IA

## �️ Technologies

- **Python 3.11+**
- **OpenAI API** (modèle gpt-4o-mini)

## 🚀 Installation et utilisation

1. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

2. **Configurer la clé API**
```bash
export OPENAI_API_KEY='votre-clé-api'
```

3. **Lancer le script**
```bash
python assistant_parisien.py
```

## 💡 Pistes d'amélioration

Quelques idées pour faire évoluer le projet :
- Permettre à l'utilisateur de saisir ses propres questions en temps réel
- Ajouter une interface web avec Flask ou Streamlit
- Intégrer un système de streaming pour afficher les réponses progressivement

---

Projet réalisé dans le cadre de ma formation au développement d'applications IA.
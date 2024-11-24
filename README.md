# Plan F


## Use case
A user writes his business idea in the form, and the AI will generate a business plan with the following sections:
- What can brings the collaborators of _Plan de Fuite_ as support
- What video formations can help from the video.csv

## TODO - TypeScript
- [ ] 🚸 Form with business idea connected to gpt with acess to video.csv
- [ ] 💄PDF download button
- [ ] 📡 Implement streaming
- [ ] 🚀 Deploy to Oracle Cloud always free
- [ ] 📝 Save pdf files with relevant name
## TODO - Python
- [x] 🚸 Form with business idea connected to gpt with acess to video.csv
- [x] 💄PDF download button
- [x] 🚀 Deploy to [streamlit](https://plan-fuite.streamlit.app)
- [ ] 📡 Implement streaming
- [ ] 📝 Save pdf files with relevant name

## TypScript - Deno application

Run tests
`deno test --allow-read --allow-env --allow-net`
## Python - Streamlit application


1. Fill secrets_example.toml with your[OpenAI API key](https://platform.openai.com/api-keys) and rename it to secrets.toml
2. Install [poetry](https://python-poetry.org/docs/#installation)
3. Create a virutal environement and install the dependencies
```bash
poetry shell
poetry install
```
4. Run the app
```bash
poetry run streamlit run app.py
```

## Exemple

### Business idea

Créer une plateforme e-commerce basée sur l'intelligence artificielle pour les petites entreprises locales. Cette plateforme utiliserait l'IA pour personnaliser les recommandations produits pour chaque client en fonction de ses préférences et de son historique de navigation. En parallèle, des outils d'automatisation marketing seraient intégrés pour simplifier la gestion des campagnes publicitaires, par exemple avec des suggestions d'annonces ciblées et l'optimisation des budgets. Enfin, un module de fidélisation client proposerait des récompenses ou des promotions personnalisées, renforçant la relation client à long terme.

### LLM output

**Résumé Exécutif :**
Ce projet vise à créer une plateforme e-commerce innovante qui met l'accent sur l'intelligence artificielle pour aider les petites entreprises locales à se développer. La plateforme proposera des recommandations de produits personnalisées, des outils d'automatisation marketing, et un module de fidélisation client. Ce business plan présente les formations disponibles dans le domaine pour soutenir le développement et l'optimisation de la plateforme.

---

**1. Analyse du Marché :**
- **Cible :** Petites entreprises locales cherchant à se digitaliser et à optimiser leur vente en ligne.
- **Tendances :** Croissance continue du e-commerce et de l'utilisation de l'IA pour la personnalisation et l'automatisation.

---

**2. Proposition de Valeur :**
- **Personnalisation :** Recommandations de produits sur mesure pour chaque client grâce à l'IA.
- **Automatisation :** Simplification de la gestion des campagnes marketing pour les petites entreprises.
- **Fidélisation :** Module pour des récompenses personnalisées, renforçant la relation client à long terme.

---

**3. Formations Disponibles :**
Pour assurer le succès de la plateforme et des utilisateurs, plusieurs formations seront proposées, en lien avec les domaines identifiés dans la base de données.

| Domaine | Lien de Formation |
|---------|-------------------|
| E-commerce | [Formation E-commerce](https://www.youtube.com/watch?v=1A2B3C4D5E6) |
| Utilisation de l'IA | [Formation sur l'IA](https://www.youtube.com/watch?v=2B3C4D5E6F7) |
| Marketing digital | [Formation Marketing Digital](https://www.youtube.com/watch?v=3C4D5E6F7G8) |
| Optimisation des ventes | [Formation Optimisation des Ventes](https://www.youtube.com/watch?v=4D5E6F7G8H9) |
| Automatisation en e-commerce | [Formation Automatisation](https://www.youtube.com/watch?v=5E6F7G8H9I0) |
| IA pour l'analyse de données | [Formation Analyse de Données](https://www.youtube.com/watch?v=6F7G8H9I0J1) |
| Stratégies de fidélisation | [Formation Fidélisation Client](https://www.youtube.com/watch?v=7G8H9I0J1K2) |
| Logistique en e-commerce | [Formation Logistique](https://www.youtube.com/watch?v=8H9I0J1K2L3) |
| Publicité en ligne | [Formation Publicité en Ligne](https://www.youtube.com/watch?v=9I0J1K2L3M4) |
| IA pour personnalisation client | [Formation Personnalisation Client](https://www.youtube.com/watch?v=0J1K2L3M4N5) |

---

**4. Stratégie de Mise en Œuvre :**
- **Développement de la plateforme :** Créer une interface utilisateur intuitive et intégrée avec des algorithmes d'IA.
- **Partenariats :** Collaborer avec des petites entreprises pour le pilotage de la plateforme et le retour d'expérience.
- **Marketing :** Utiliser les outils d'automatisation pour lancer des campagnes ciblées afin d'attirer des utilisateurs.

---

**5. Conclusion :**
Cette plateforme e-commerce basée sur l'IA représente une solution innovante pour les petites entreprises locales. En intégrant des formations pertinentes, nous garantissons que les utilisateurs peuvent tirer le meilleur parti des outils offerts, favorisant ainsi leur croissance et leur succès à long terme.

---

Ce business plan met en avant non seulement l'idée de la plateforme, mais aussi les ressources éducatives disponibles pour former les utilisateurs et les aider à maximiser leurs résultats.
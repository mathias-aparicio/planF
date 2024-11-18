import os

import pandas as pd

from api import business_plan, exit_strategy_to_pdf

# Load video data
video_data = pd.read_csv("video.csv")


def test_business_plan():
    business_idea = "Créer une plateforme e-commerce basée sur l'intelligence artificielle pour les petites entreprises locales. Cette plateforme utiliserait l'IA pour personnaliser les recommandations produits pour chaque client en fonction de ses préférences et de son historique de navigation. En parallèle, des outils d'automatisation marketing seraient intégrés pour simplifier la gestion des campagnes publicitaires, par exemple avec des suggestions d'annonces ciblées et l'optimisation des budgets. Enfin, un module de fidélisation client proposerait des récompenses ou des promotions personnalisées, renforçant la relation client à long terme."
    plan = business_plan(business_idea)
    print(plan)


def test_exit_strategy_to_pdf():
    text = """
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
"""
    exit_strategy_to_pdf(text)
    assert os.path.exists("exit_strategy.pdf")

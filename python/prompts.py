main_prompt_old = """
		Étant donné l'idée de business {form}
		Identifie les éléments de de la base de données retrouvée dans l'idée de business.
		{video_data}
		Retourne uniquement les éléments pertinents de la base de données par rapport à l'idée de business.
		Retourne un business plan qui met en avant les formations disponibles dans la base de données.
		"""

main_prompt = """
    Analysez l'idée de business suivante : {form}

    À partir de la base de données de formations ci-dessous :
    {video_data}

    Instructions précises :
    1. Identifiez UNIQUEMENT les domaines de formation directement liés à l'idée de business
    2. Pour chaque domaine identifié, expliquez en une ligne pourquoi il est pertinent
    3. Structurez la réponse comme suit:

    DOMAINES PERTINENTS IDENTIFIÉS:
    - [Nom du domaine] : [Lien] - [Brève justification]

    BUSINESS PLAN CIBLÉ:
    1. Concept principal
    2. Applications spécifiques des formations identifiées
    3. Stratégie de mise en œuvre

    Ne listez pas les domaines non pertinents pour cette idée de business.
	Redigez la sortie au format markdown
    """

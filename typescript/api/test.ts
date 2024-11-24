import { assertEquals } from "jsr:@std/assert";
import { businessPlan } from "./main.ts";
Deno.test("businessPlan", async () => {
  const idea =
    "Créer une plateforme e-commerce basée sur l'intelligence artificielle pour les petites entreprises locales. Cette plateforme utiliserait l'IA pour personnaliser les recommandations produits pour chaque client en fonction de ses préférences et de son historique de navigation. En parallèle, des outils d'automatisation marketing seraient intégrés pour simplifier la gestion des campagnes publicitaires, par exemple avec des suggestions d'annonces ciblées et l'optimisation des budgets. Enfin, un module de fidélisation client proposerait des récompenses ou des promotions personnalisées, renforçant la relation client à long terme.";

  const result = await businessPlan(idea);
  console.log(result);
});

import { parse } from "@std/csv/parse";
import { ChatOpenAI } from "@langchain/openai";
import { PromptTemplate } from "@langchain/core/prompts"; // Configuration
import { StringOutputParser } from "@langchain/core/output_parsers";
const MODEL = "gpt-4o-mini";

// Helper function to read CSV data
async function readCsvData(filePath: string): Promise<string[][]> {
  const text = await Deno.readTextFile(filePath);

  const data = parse(text);
  return data;
}

/**Take a business idea and returns a business plan.*/
async function businessPlan(form: string) {
  // Load video data
  const videoData = await readCsvData("./video.csv");


  // Initialize the language model
  const llm = new ChatOpenAI({ model: MODEL, apiKey	: Deno.env.get("OPENAI_API_KEY")});

  // Define the prompt template with the video data
  const prompt = new PromptTemplate({
    inputVariables: ["form", "videoData"],
    template: template,
  });


  // Set output parser to return only the relevant string
  const parser = new StringOutputParser();

  // Create the chain
  //const chain = prompt.pipe(llm).pipe(parser);

  // Run the chain
  //const output = await chain.invoke({ form: form, videoData: videoData });
  const output = await parser.invoke(await llm.invoke(await prompt.invoke({ form: form, videoData: videoData })));
  return output;
}
const template = `
    Analysez l'idée de business suivante : {form}

    À partir de la base de données de formations ci-dessous :
    {videoData}

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
`;
// Export the main function
export { businessPlan };

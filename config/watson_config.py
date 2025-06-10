from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
import os
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "url": os.getenv("WATSONX_URL", "https://api.watsonx.ai"),
    "apikey": os.getenv("API_KEY"),
    "project_id" : os.getenv("PROJECT_ID", "default_project_id")
}


def get_llm():
    return WatsonxLLM(
    model_id= "ibm/granite-3-8b-instruct", 
    url=credentials.get("url"),
    apikey=credentials.get("apikey"),
    project_id=credentials.get("project_id"),
    params={
        GenParams.DECODING_METHOD: "greedy",
        GenParams.TEMPERATURE: 0,
        GenParams.MIN_NEW_TOKENS: 5,
        GenParams.MAX_NEW_TOKENS: 250,
        GenParams.STOP_SEQUENCES: ["Human:", "Observation"],
    },
)

def get_embeddings():
    return WatsonxEmbeddings(
    model_id=EmbeddingTypes.IBM_SLATE_30M_ENG.value,
    url=credentials["url"],
    apikey=credentials["apikey"],
    project_id=credentials["project_id"],
)

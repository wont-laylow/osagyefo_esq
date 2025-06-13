from langchain.vectorstores import Chroma
import os
from langchain_core.embeddings import Embeddings
from together import Together
from dotenv import load_dotenv
import openai
load_dotenv(override=True)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


class TogetherEmbeddings(Embeddings):
    def __init__(self, model="togethercomputer/m2-bert-80M-32k-retrieval", api_key=None):
        self.client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)

        self.model = model

    def embed_documents(self, texts):
        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )
        return [d.embedding for d in response.data]

    def embed_query(self, text):
        response = self.client.embeddings.create(
            model=self.model,
            input=[text]
        )
        return response.data[0].embedding

embedding_model = TogetherEmbeddings()



class PreRag:

    current_dir = os.path.dirname(__file__)
    chroma_path = os.path.join(current_dir, "..", "..", "chroma")
    chroma_path = os.path.abspath(chroma_path)
    

    vector_store = Chroma(
        embedding_function=embedding_model,
        persist_directory=chroma_path,
        collection_name="osagyefo_v1",
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",  
        search_kwargs={"k": 5, "lambda_mult": 0.5}
    )

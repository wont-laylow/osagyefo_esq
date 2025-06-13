from langchain.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os

class PreRag:

    current_dir = os.path.dirname(__file__)
    chroma_path = os.path.join(current_dir, "..", "..", "chroma")
    chroma_path = os.path.abspath(chroma_path)
    
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_store = Chroma(
        embedding_function=embedding_function,
        persist_directory=chroma_path,
        collection_name="osagyefo_v1",
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",  
        search_kwargs={"k": 5, "lambda_mult": 0.5}
    )

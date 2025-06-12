from langchain.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

class PreRag:
    
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_store = Chroma(
        embedding_function=embedding_function,
        persist_directory="../chroma",
        collection_name="osagyefo_v1",
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",  
        search_kwargs={"k": 5, "lambda_mult": 0.5}
    )

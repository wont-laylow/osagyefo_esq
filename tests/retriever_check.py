from langchain.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings


embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Chroma(
embedding_function=embedding_function,
persist_directory="C:\\Users\\DeLL\\Desktop\\anything_py\\osagyefo_ai\\chroma",
collection_name="osagyefo_v1",
)

retriever = vector_store.as_retriever(
search_type="mmr",  
search_kwargs={"k": 3, "lambda_mult": 0.5}
    )


print("vector store", vector_store)
print("Number of documents:", vector_store._collection.count())

print("****************************")
print("retriever", retriever)

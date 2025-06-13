from sentence_transformers import SentenceTransformer

print("downloading model....")
model = SentenceTransformer("all-MiniLM-L6-v2")
model.save("./local_models/all-MiniLM-L6-v2")
print("download complete")
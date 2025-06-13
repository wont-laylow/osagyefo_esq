from src.app.a_sub_model import rephrase_query
from src.app.load_models import ModelParameters
from src.app.load_embeddings import PreRag
import os


def chat_osagyefo(user_query):
    
    current_dir = os.path.dirname(__file__)
    prompt_path = os.path.join(current_dir, "..", "..", "prompts", "main_prompt_template.txt")
    prompt_path = os.path.abspath(prompt_path)

    rephrased_query = rephrase_query(user_query)
    relevant_docs = PreRag.retriever.get_relevant_documents(rephrased_query)

    print("RELEVANT DOCS: ", relevant_docs)
    context = ''
    for doc in relevant_docs:
        context += f"[Source: {doc.metadata['file_name']}, Chapter: {doc.metadata.get('chapter_title', 'N/A')}]\n{doc.page_content}\n\n"
    print("context", context)
    # loading the prompt
    with open(prompt_path, "r", encoding="utf-8") as f:
        osagyefo_system_prompt = f.read().strip()
    osagyefo_system_prompt += f"Use the following context to answer:\n{context}"

    print(osagyefo_system_prompt)

    msg_to_model = [{"role": "system", "content": osagyefo_system_prompt}, {"role": "user", "content": user_query}]

    model = ModelParameters.client2.chat.completions.create(
        model=ModelParameters.model_2,
        messages=msg_to_model,
    )

    osagyefo_response = model.choices[0].message.content
    

    
    return osagyefo_response
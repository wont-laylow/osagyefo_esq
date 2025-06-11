from a_sub_model import rephrase_query
from src.app.load_models import ModelParameters
from src.app.load_embeddings import PreRag


def chat_osagyefo(user_query, history):
    
    prompt_path = "../prompts/main_prompt_template.txt"

    rephrased_query = rephrase_query(user_query)
    relevant_docs = PreRag.retriever.get_relevant_documents(rephrased_query)

    print("RELEVANT DOCS: ", relevant_docs)
    context = ''
    for doc in relevant_docs:
        context += f"[Source: {doc.metadata['file_name']}, Chapter: {doc.metadata.get('chapter_title', 'N/A')}]\n{doc.page_content}\n\n"

    # loading the prompt
    with open(prompt_path, "r", encoding="utf-8") as f:
        osagyefo_system_prompt = f.read().strip()
    osagyefo_system_prompt += f"Use the following context to answer:\n{context}"


    history = [
        {'role': h['role'], 'content': h['content'] }
        for h in history
        if 'role' in h and 'content' in h
    ]

    msg_to_model = [{"role": "system", "content": osagyefo_system_prompt}] + history + [{"role": "user", "content": user_query}]

    model = ModelParameters.client2.chat.completions.create(
        model=ModelParameters.model_2,
        messages=msg_to_model,
    )

    osagyefo_response = model.choices[0].message.content
    

    history.append({"role": "user", "content": user_query})
    history.append({"role": "assistant", "content": osagyefo_response})

    # print('history', history)
    
    return osagyefo_response
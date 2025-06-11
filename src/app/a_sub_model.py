"""
Subordinate to support the primary model during inferencing.
Role: repharse the prompt
"""
import os
from src.app.load_models import ModelParameters

def rephrase_query(user_query):
    # pdf_path = ".../docs"
    prompt_path = "C:\\Users\\DeLL\\Desktop\\anything_py\\osagyefo_ai\\prompts\\rephaser_llm_template.txt"
    
    with open(prompt_path, "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()
        system_prompt += """Your knowledge is limited strictly to the content of the following files:
            Ghana’s 1992 Constitution,
            children’s act, 1998 (act 560),
            criminal offences act,
            data-protection-act-2012-act-843,
            domestic_violence_act,
            land-act-2020-act-1036,
            rent act, 1963 (act 220).
            
        """
        # for filename in os.listdir(pdf_path):
        #     system_prompt += filename + "\n"


    message = [{'role': "system", "content": system_prompt}, {'role': "system", "content": user_query}]
    rephrased_query = ModelParameters.client1.chat.completions.create(model=ModelParameters.model_1, messages=message)
    rephrased_query = rephrased_query.choices[0].message.content

    return rephrased_query
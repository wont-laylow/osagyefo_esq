import openai
from dotenv import load_dotenv
import os

class ModelParameters:

    load_dotenv(override=True)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

    model_1 = "gemma2-9b-it"
    client1 = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    model_2 = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
    client2 = openai.OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
    )

    # will add model_3 for eval

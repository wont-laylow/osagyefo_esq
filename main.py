import gradio as gr
from src.app.b_primary_model import chat_osagyefo

demo_chatbot = gr.ChatInterface(chat_osagyefo,
                                title="OSAGYEFO ESQ.",
                                description="Welcome! Put forth your legal challenges. ")

demo_chatbot.launch()
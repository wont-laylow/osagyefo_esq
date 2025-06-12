import gradio as gr
from src.app.b_primary_model import chat_osagyefo

demo_chatbot = gr.ChatInterface(chat_osagyefo,
                                title="OSAGYEFO ESQ.",
                                description="Welcome! Put forth your local legal challenges. ")



if __name__ == "__main__":
    demo_chatbot.launch(server_name="0.0.0.0", server_port=7860)
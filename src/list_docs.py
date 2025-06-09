import os

current_knowledge_base = ''
for root, dirs, files in os.walk("./docs"):
    for file in files:
        current_knowledge_base += file.lower() + "\n"

print(current_knowledge_base)

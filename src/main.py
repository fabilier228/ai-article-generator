import openai

openai.api_key = "YOUR_API_KEY"


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

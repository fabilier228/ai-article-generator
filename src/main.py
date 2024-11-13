from openai import OpenAI


def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def generate_html_content(article_content):
    prompt = f"""
    Na podstawie poniższego artykułu wygeneruj kod HTML do wstawienia między tagami <body> i </body>. 
    Zastosuj odpowiednie tagi HTML do strukturyzacji tekstu, a tam, gdzie zasadne, wstaw tagi <img> z 
    atrybutem src="image_placeholder.jpg" oraz szczegółowym opisem alt, który możemy użyć do generowania grafiki.
    Pod każdym obrazem dodaj podpis w odpowiednim tagu. Kod nie powinien zawierać CSS ani JavaScript.
    Oto artykuł: {article_content}
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )

    html_content = response.choices[0].message.content
    return html_content



article_content = read_article('../data/artykul.txt')
generate_html_content(article_content)

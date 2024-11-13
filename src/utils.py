def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_html(file_path, html_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
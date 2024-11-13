from src.utils import read_article, save_html
from src.article_processor import generate_html_content, generate_article_preview


def main():
    article_content = read_article('../data/artykul.txt')

    html_content = generate_html_content(article_content)
    html_preview = generate_article_preview(html_content, '../data/szablon.html')

    save_html('../output/podglad.html', html_preview)
    save_html('../output/artykul.html', html_content)
    print("HTML file has been saved.")


if __name__ == "__main__":
    main()

from openai import OpenAI

client = OpenAI(
    # Here write code from instruction in README.md)
)

def generate_html_content(article_content):
    prompt = f"""
    Based on the following article, generate the HTML code to be inserted between the <body> and </body> tags. 
    Use appropriate HTML tags for structuring the text, and where relevant, 
    insert <img> tags with the attribute src="image_placeholder.jpg" and 
    a detailed alt description that we can use for generating the image. Below each image, 
    add a caption in the appropriate tag. The code should not include any CSS or JavaScript."
    Article: {article_content}
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

def generate_article_preview(content, template):
    with open(template, "r") as file:
        html_template = file.read()

    params = {
        "title": "Article Preview",
        "content": content
    }

    html_output = html_template.replace("{{ title }}", params["title"]) \
                                .replace("{{ content }}", params["content"])

    return html_output
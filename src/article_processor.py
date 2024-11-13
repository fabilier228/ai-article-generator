from openai import OpenAI

client = OpenAI(
    api_key="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"
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
from openai import OpenAI
import json
import pandas as pd
from source.output_formats import CategoryList
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def define_categories(comments: list[str]) -> list[dict]:
    """
    Reads comments from the given CSV file, sends them to the OpenAI API along with a prompt
    to generate 5-7 mutually exclusive sentiment/theme categories, and returns the categories as a dictionary.

    Args:
        csv_file_path (str): Path to the CSV file containing comments.

    Returns:
        list[dict]: List of dictionaries containing the generated categories.
    """

    comment_list_str = "\n".join(f"- {comment}" for comment in comments)

    with open("prompts/1_define_categories_prompt.md", "r") as file:
        define_categories_prompt = file.read()

    define_categories_prompt = define_categories_prompt.format(comments=comment_list_str)

    completion = client.beta.chat.completions.parse(
        model="o3",
        messages=[
            {"role": "system", "content": define_categories_prompt},
            {"role": "user", "content": comment_list_str}
        ],
        response_format=CategoryList,
    )

    categories = json.loads(completion.choices[0].message.content)

    return categories["categories"]

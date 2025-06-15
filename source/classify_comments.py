from openai import OpenAI
import json
import pandas as pd
from output_formats import create_comment_list_class
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_comments(comments: list[str], categories: list[dict]) -> list[dict]:
    """
    Classify comments into categories.

    Args:
        comments: List of comments to classify.
        categories: List of dictionaries containing category names and descriptions.

    Returns:
        List of dictionaries containing the comment text and its assigned category.
    """
    category_names = [category['name'] for category in categories]
    CommentList = create_comment_list_class(category_names)

    comment_list_str = "\n".join(
        f"- {comment}" for comment in comments
    )

    with open("prompts/2_classify_comments_prompt.md", "r") as file:
        classify_comments_prompt = file.read()

    formatted_categories = "\n".join(
        f"- **{category['name']}**: {category['description']}" for category in categories
    )
    classify_comments_prompt = classify_comments_prompt.format(
        categories=formatted_categories
    )

    completion = client.beta.chat.completions.parse(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": classify_comments_prompt},
            {"role": "user", "content": comment_list_str}
        ],
        response_format=CommentList,
    )

    result = json.loads(completion.choices[0].message.content)

    return result["comments"]

if __name__ == "__main__":
    comments = pd.read_csv("data/ECLIPSE_ RISING.csv")["Comment"][:10]
    categories = [
        {
            "name": "Enthusiasm and Excitement",
            "description": "Comments expressing excitement, hype, or emotional reactions such as crying, screaming, or joy about the teaser or upcoming release."
        },
        {
            "name": "Casting and Character Predictions",
            "description": "Comments speculating about casting choices, favorite actors for roles, or expressing approval/disapproval of potential cast options."
        },
        {
            "name": "Budget and Quality Concerns",
            "description": "Comments voicing concerns or hopes related to budget, VFX quality, production values, or realism of the effects."
        },
        {
            "name": "Franchise Expectations and Nostalgia",
            "description": "Comments referring to the original books, previous adaptations, or expressing nostalgia and attachment to the source material."
        },
        {
            "name": "Criticism and Reboot Fatigue",
            "description": "Comments criticizing reboots, remakes, or expressing fatigue and frustration with continuous reboots or lack of originality."
        },
        {
            "name": "Plot and Scene Expectations",
            "description": "Comments about specific scenes, plot points, or elements fans hope to see, such as battle scenes, twists, or character arcs."
        },
        {
            "name": "Marketing and Release Info",
            "description": "Comments discussing trailer dates, release dates, promotional materials, or related marketing news."
        }
    ]
    classified_comments = classify_comments(comments, categories)
    print(json.dumps(classified_comments, indent=4))

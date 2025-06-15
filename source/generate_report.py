from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(
        comments: list[str],
        statistics: str
    ) -> str:
    """
    Generate a report based on the comments and statistics.

    Args:
        comments: List of comments to generate a report for.
        statistics: Statistics generated previously.

    Returns:
        Markdown formatted report as a string.
    """

    with open("prompts/3_generate_report_prompt.md", "r") as file:
        generate_report_prompt = file.read()

    generate_report_prompt = generate_report_prompt.format(
        comments="\n".join(
            f"- {comment}" for comment in comments
        ),
        statistics=statistics
    )

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": generate_report_prompt}
        ]
    )

    report = completion.choices[0].message.content

    return report

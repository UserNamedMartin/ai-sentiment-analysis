from source.define_categories import define_categories
from source.classify_comments import classify_comments
from source.generate_report import generate_report
import pandas as pd

def main(csv_file_path: str):

    comments = pd.read_csv(csv_file_path)["Comment"].tolist()
    print(f"Number of comments: {len(comments)}\n\n")

    categories = define_categories(comments)
    print("Categories:\n")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category['name']}: {category['description']}")
    print("\n\n")

    comments_per_category = {category["name"]: 0 for category in categories}
    comments_per_category["Outliers"] = 0
    print("Processing comments", end="", flush=True)
    for comments_batch in [comments[i:i+10] for i in range(0, len(comments), 10)]:
        classified_comments = classify_comments(comments_batch, categories)
        for comment in classified_comments:
            comments_per_category[comment["category"]] += 1
        print(".", end="", flush=True)
    print("\n\n")

    print("\nComments per category:\n")
    for i, (category, count) in enumerate(comments_per_category.items()):
        print(f"{i+1}. {category}: {count}")
    print("\n\n")

    statistics = "**Comments per category:**\n"
    for category, count in comments_per_category.items():
        statistics += f"- **{category}**: {count}\n"
    statistics += "\n\n"

    report = generate_report(comments, statistics)
    print("Report Successfully Generated!")
    return report

if __name__ == "__main__":

    report = main("data/ECLIPSE_ RISING.csv")

    with open('Sentiment Report.md', "w") as file:
        file.write(report.strip('```markdown').strip('```'))
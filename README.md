# Sentiment Analysis Tool

A Python application that automatically analyzes comments from CSV files, categorizes them using AI, and generates comprehensive sentiment reports.

**Limitation Note**: This project is a proof of concept (POC) and, in some steps, processes the entire comments dataset at once. Supplying very large datasets may lead to excessive token usage and reduced output quality.

## Features

- **Automatic Category Detection**: AI-powered analysis to identify relevant categories from your comments
- **Batch Processing**: Efficiently processes large volumes of comments in batches
- **Detailed Reporting**: Generates comprehensive markdown reports with statistics and insights
- **CSV Support**: Works with any CSV file containing a "Comment" column
- **Real-time Progress**: Shows processing progress as comments are analyzed

## Project Structure

```
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── source/                # Core modules
│   ├── define_categories.py    # AI-powered category definition
│   ├── classify_comments.py   # Comment classification logic
│   ├── generate_report.py     # Report generation
│   └── output_formats.py      # Output formatting utilities
├── data/                  # Input CSV files directory
│   └── ECLIPSE_ RISING.csv    # Sample data file
├── prompts/              # AI prompt templates (if any)
└── Sentiment Report.md   # Generated output report
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (for AI-powered categorization)

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   
   Create a `.env` file in the project root:
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
   
   Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

### Quick Start

To run the application with the sample data:

```bash
python main.py
```

This will process the included `data/ECLIPSE_ RISING.csv` file and generate a `Sentiment Report.md`.

### Using Your Own Data

1. **Prepare your CSV file**
   - Ensure your CSV has a column named "Comment"
   - Place the file in the `data/` directory

2. **Update the file path in main.py**
   ```python
   # Edit line 42 in main.py
   report = main("data/YOUR_FILE.csv")
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### CSV Format Requirements

Your CSV file must contain at least one column named "Comment". Example:

```csv
ID,Comment
1,"This is a positive comment"
2,"This is a negative comment"
3,"This is a neutral comment"
```

## How It Works

1. **Data Loading**: Reads comments from the specified CSV file
2. **Category Definition**: AI analyzes a sample of comments to automatically identify relevant categories
3. **Comment Classification**: Each comment is classified into one of the identified categories or marked as an outlier
4. **Report Generation**: Creates a detailed markdown report with:
   - Category definitions and descriptions
   - Comment distribution across categories
   - Statistical analysis
   - Key insights and trends

## Output

The application generates a `Sentiment Report.md` file containing:

- **Executive Summary**: Overview of the analysis
- **Category Breakdown**: Detailed statistics for each category
- **Key Insights**: AI-generated insights about the comment patterns
- **Recommendations**: Actionable recommendations based on the analysis

## Customization

### Modifying Categories

The categories are automatically generated, but you can influence them by:
- Modifying the prompts in the `source/define_categories.py` file
- Adjusting the sample size used for category detection

### Changing Output Format

- Modify `source/generate_report.py` to change the report structure
- Edit `source/output_formats.py` to customize the markdown formatting

### Batch Size

Comments are processed in batches of 10 by default. To change this:

```python
# In main.py, line 21, change the batch size:
for comments_batch in [comments[i:i+BATCH_SIZE] for i in range(0, len(comments), BATCH_SIZE)]:
```

## API Usage

The application uses OpenAI's API for:
- Automatic category detection from comment samples
- Individual comment classification
- Report generation and insight creation

Make sure you have sufficient API credits for your dataset size.

## Sample Data

The included `ECLIPSE_ RISING.csv` contains 200 sample comments about a fictional TV show adaptation, including:
- Fan reactions and excitement
- Casting suggestions and preferences  
- Concerns about adaptation quality
- Spam and promotional content
- Social media interactions

This provides a good example of mixed sentiment social media data for testing the tool. 
from pydantic import BaseModel, Field, create_model

# 1. Define Categories

class Category(BaseModel):
    name: str = Field(description="The name of the category")
    description: str = Field(description="A description of the category")

class CategoryList(BaseModel):
    categories: list[Category] = Field(description="A list of categories")

# 2. Classify Comments - Dynamic Creation

def create_comment_list_class(category_names: list[str]) -> BaseModel:
    """
    Dynamically create a CommentList class with specific category literal values. Automatically includes "Outlier" as a category.
    
    Args:
        category_names: List of category names to use as literal values
    
    Returns:
        CommentList class with embedded Comment class
    """
    # Create the comment class with string field that validates against category_names
    comment_class = create_model(
        'Comment',
        text=(str, Field(description="The text of the comment as it appears in the original data")),
        category=(str, Field(description="The category of the comment", enum=category_names+["Outlier"]))
    )
    
    # Create and return CommentList class
    return create_model(
        'CommentList',
        comments=(list[comment_class], Field(description="A list of comments"))
    )

"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Audit(BaseModel):
    """
    Mini Audit submissions from the website
    Collection name: "audit"
    """
    company_name: str = Field(..., description="Company name")
    contact_email: EmailStr = Field(..., description="Contact email")
    industry: Optional[str] = Field(None, description="Industry or sector")
    team_size: Optional[str] = Field(None, description="Team size bracket")
    processes: List[str] = Field(default_factory=list, description="Processes to automate")
    pain_points: Optional[str] = Field(None, description="Main bottlenecks or issues")
    current_tools: Optional[str] = Field(None, description="Current tools/stack")
    budget_range: Optional[str] = Field(None, description="Budget range")
    urgency: Optional[str] = Field(None, description="Project urgency")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!

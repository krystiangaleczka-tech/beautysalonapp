"""
Pydantic schemas for Client API endpoints.
Provides request/response validation and serialization for the Client management system.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
import re


class ClientCreateSchema(BaseModel):
    """
    Schema for creating a new client.
    Used for POST /api/clients/ requests.
    """
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Client's first name",
        example="Maria"
    )
    
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Client's last name",
        example="Rodriguez"
    )
    
    email: EmailStr = Field(
        ...,
        description="Client's email address for notifications",
        example="maria.rodriguez@email.com"
    )
    
    phone: Optional[str] = Field(
        None,
        max_length=15,
        description="Client's phone number in international format",
        example="+1234567890"
    )
    
    allergies: Optional[str] = Field(
        None,
        description="Any allergies or sensitivities to products",
        example="Allergic to shellfish-based products"
    )
    
    notes: Optional[str] = Field(
        None,
        description="Additional notes about the client",
        example="Prefers morning appointments, sensitive skin"
    )
    
    @validator('phone')
    def validate_phone(cls, v):
        """Validate phone number format."""
        if v is not None and v.strip():
            # Remove spaces and common separators
            phone_cleaned = re.sub(r'[\s\-\(\)]', '', v)
            # Check format: optional + followed by 9-15 digits
            if not re.match(r'^\+?1?\d{9,15}$', phone_cleaned):
                raise ValueError(
                    'Phone number must be in format: "+999999999". Up to 15 digits allowed.'
                )
            return phone_cleaned
        return v
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        """Validate name fields are not empty after stripping."""
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
    
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Maria",
                "last_name": "Rodriguez",
                "email": "maria.rodriguez@email.com",
                "phone": "+1234567890",
                "allergies": "Allergic to shellfish-based products",
                "notes": "Prefers morning appointments"
            }
        }


class ClientUpdateSchema(BaseModel):
    """
    Schema for updating an existing client.
    Used for PUT/PATCH /api/clients/{id}/ requests.
    All fields are optional for partial updates.
    """
    first_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Client's first name",
        example="Maria"
    )
    
    last_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Client's last name",
        example="Rodriguez"
    )
    
    email: Optional[EmailStr] = Field(
        None,
        description="Client's email address for notifications",
        example="maria.rodriguez@newemail.com"
    )
    
    phone: Optional[str] = Field(
        None,
        max_length=15,
        description="Client's phone number in international format",
        example="+1234567890"
    )
    
    allergies: Optional[str] = Field(
        None,
        description="Any allergies or sensitivities to products",
        example="Allergic to shellfish-based products"
    )
    
    notes: Optional[str] = Field(
        None,
        description="Additional notes about the client",
        example="Prefers morning appointments, sensitive skin"
    )
    
    @validator('phone')
    def validate_phone(cls, v):
        """Validate phone number format."""
        if v is not None and v.strip():
            # Remove spaces and common separators
            phone_cleaned = re.sub(r'[\s\-\(\)]', '', v)
            # Check format: optional + followed by 9-15 digits
            if not re.match(r'^\+?1?\d{9,15}$', phone_cleaned):
                raise ValueError(
                    'Phone number must be in format: "+999999999". Up to 15 digits allowed.'
                )
            return phone_cleaned
        return v
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        """Validate name fields are not empty after stripping."""
        if v is not None:
            if not v or not v.strip():
                raise ValueError('Name cannot be empty')
            return v.strip()
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "maria.rodriguez@newemail.com",
                "phone": "+1987654321",
                "notes": "Updated preferences: prefers afternoon appointments"
            }
        }


class ClientResponseSchema(BaseModel):
    """
    Schema for client API responses.
    Used for GET requests and successful POST/PUT responses.
    """
    id: int = Field(
        ...,
        description="Unique client identifier",
        example=1
    )
    
    first_name: str = Field(
        ...,
        description="Client's first name",
        example="Maria"
    )
    
    last_name: str = Field(
        ...,
        description="Client's last name",
        example="Rodriguez"
    )
    
    email: str = Field(
        ...,
        description="Client's email address",
        example="maria.rodriguez@email.com"
    )
    
    phone: Optional[str] = Field(
        None,
        description="Client's phone number",
        example="+1234567890"
    )
    
    allergies: Optional[str] = Field(
        None,
        description="Client's allergies and sensitivities",
        example="Allergic to shellfish-based products"
    )
    
    notes: Optional[str] = Field(
        None,
        description="Additional notes about the client",
        example="Prefers morning appointments, sensitive skin"
    )
    
    full_name: str = Field(
        ...,
        description="Client's full name (computed field)",
        example="Maria Rodriguez"
    )
    
    created_at: datetime = Field(
        ...,
        description="When the client record was created",
        example="2024-01-15T10:30:00Z"
    )
    
    updated_at: datetime = Field(
        ...,
        description="When the client record was last updated",
        example="2024-01-20T14:45:00Z"
    )
    
    class Config:
        from_attributes = True  # Enable ORM mode for Django model conversion
        json_schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Maria",
                "last_name": "Rodriguez",
                "email": "maria.rodriguez@email.com",
                "phone": "+1234567890",
                "allergies": "Allergic to shellfish-based products",
                "notes": "Prefers morning appointments, sensitive skin",
                "full_name": "Maria Rodriguez",
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": "2024-01-20T14:45:00Z"
            }
        }


class ClientListResponseSchema(BaseModel):
    """
    Schema for paginated client list responses.
    Used for GET /api/clients/ with pagination.
    """
    clients: list[ClientResponseSchema] = Field(
        ...,
        description="List of clients for current page"
    )
    
    total: int = Field(
        ...,
        description="Total number of clients",
        example=150
    )
    
    page: int = Field(
        ...,
        description="Current page number",
        example=1
    )
    
    page_size: int = Field(
        ...,
        description="Number of clients per page",
        example=20
    )
    
    total_pages: int = Field(
        ...,
        description="Total number of pages",
        example=8
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "clients": [
                    {
                        "id": 1,
                        "first_name": "Maria",
                        "last_name": "Rodriguez",
                        "email": "maria.rodriguez@email.com",
                        "phone": "+1234567890",
                        "allergies": "Allergic to shellfish-based products",
                        "notes": "Prefers morning appointments",
                        "full_name": "Maria Rodriguez",
                        "created_at": "2024-01-15T10:30:00Z",
                        "updated_at": "2024-01-20T14:45:00Z"
                    }
                ],
                "total": 150,
                "page": 1,
                "page_size": 20,
                "total_pages": 8
            }
        }


class ClientSearchSchema(BaseModel):
    """
    Schema for client search requests.
    Used for GET /api/clients/search/ query parameters.
    """
    query: Optional[str] = Field(
        None,
        description="Search query for client name or email",
        example="maria"
    )
    
    email: Optional[str] = Field(
        None,
        description="Filter by exact email address",
        example="maria@email.com"
    )
    
    phone: Optional[str] = Field(
        None,
        description="Filter by phone number",
        example="+1234567890"
    )
    
    page: int = Field(
        1,
        ge=1,
        description="Page number for pagination",
        example=1
    )
    
    page_size: int = Field(
        20,
        ge=1,
        le=100,
        description="Number of results per page (max 100)",
        example=20
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "maria",
                "page": 1,
                "page_size": 20
            }
        }
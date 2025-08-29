"""
Pydantic schemas for Client API endpoints.
Provides request/response validation and serialization for the Client management system.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
import re


class ClientCreateSchema(BaseModel):
    """
    Schema for creating a new client.
    Used for POST /api/clients/ requests.
    """
    first_name: str = Field(
        min_length=1,
        max_length=50,
        description="Client's first name"
    )
    
    last_name: str = Field(
        min_length=1,
        max_length=50,
        description="Client's last name"
    )
    
    email: EmailStr = Field(
        description="Client's email address for notifications"
    )
    
    phone: Optional[str] = Field(
        default=None,
        max_length=15,
        description="Client's phone number in international format"
    )
    
    allergies: Optional[str] = Field(
        default=None,
        description="Any allergies or sensitivities to products"
    )
    
    notes: Optional[str] = Field(
        default=None,
        description="Additional notes about the client"
    )
    
    @field_validator('phone')
    @classmethod
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
    
    @field_validator('first_name', 'last_name')
    @classmethod
    def validate_names(cls, v):
        """Validate name fields are not empty after stripping."""
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "first_name": "Maria",
                "last_name": "Rodriguez",
                "email": "maria.rodriguez@email.com",
                "phone": "+1234567890",
                "allergies": "Allergic to shellfish-based products",
                "notes": "Prefers morning appointments"
            }
        }
    )


class ClientUpdateSchema(BaseModel):
    """
    Schema for updating an existing client.
    Used for PUT/PATCH /api/clients/{id}/ requests.
    All fields are optional for partial updates.
    """
    first_name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Client's first name"
    )
    
    last_name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Client's last name"
    )
    
    email: Optional[EmailStr] = Field(
        default=None,
        description="Client's email address for notifications"
    )
    
    phone: Optional[str] = Field(
        default=None,
        max_length=15,
        description="Client's phone number in international format"
    )
    
    allergies: Optional[str] = Field(
        default=None,
        description="Any allergies or sensitivities to products"
    )
    
    notes: Optional[str] = Field(
        default=None,
        description="Additional notes about the client"
    )
    
    @field_validator('phone')
    @classmethod
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
    
    @field_validator('first_name', 'last_name')
    @classmethod
    def validate_names(cls, v):
        """Validate name fields are not empty after stripping."""
        if v is not None:
            if not v or not v.strip():
                raise ValueError('Name cannot be empty')
            return v.strip()
        return v
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "maria.rodriguez@newemail.com",
                "phone": "+1987654321",
                "notes": "Updated preferences: prefers afternoon appointments"
            }
        }
    )


class ClientResponseSchema(BaseModel):
    """
    Schema for client API responses.
    Used for GET requests and successful POST/PUT responses.
    """
    id: int = Field(description="Unique client identifier")
    first_name: str = Field(description="Client's first name")
    last_name: str = Field(description="Client's last name")
    email: str = Field(description="Client's email address")
    phone: Optional[str] = Field(default=None, description="Client's phone number")
    allergies: Optional[str] = Field(default=None, description="Client's allergies and sensitivities")
    notes: Optional[str] = Field(default=None, description="Additional notes about the client")
    full_name: str = Field(description="Client's full name (computed field)")
    created_at: datetime = Field(description="When the client record was created")
    updated_at: datetime = Field(description="When the client record was last updated")
    
    model_config = ConfigDict(
        from_attributes=True,  # Enable ORM mode for Django model conversion
        json_schema_extra={
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
    )


class ClientListResponseSchema(BaseModel):
    """
    Schema for paginated client list responses.
    Used for GET /api/clients/ with pagination.
    """
    clients: list[ClientResponseSchema] = Field(description="List of clients for current page")
    total: int = Field(description="Total number of clients")
    page: int = Field(description="Current page number")
    page_size: int = Field(description="Number of clients per page")
    total_pages: int = Field(description="Total number of pages")
    
    model_config = ConfigDict(
        json_schema_extra={
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
    )


class ClientSearchSchema(BaseModel):
    """
    Schema for client search requests.
    Used for GET /api/clients/search/ query parameters.
    """
    query: Optional[str] = Field(
        default=None,
        description="Search query for client name or email"
    )
    
    email: Optional[str] = Field(
        default=None,
        description="Filter by exact email address"
    )
    
    phone: Optional[str] = Field(
        default=None,
        description="Filter by phone number"
    )
    
    page: int = Field(
        default=1,
        ge=1,
        description="Page number for pagination"
    )
    
    page_size: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Number of results per page (max 100)"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query": "maria",
                "page": 1,
                "page_size": 20
            }
        }
    )
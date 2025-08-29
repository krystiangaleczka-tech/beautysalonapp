"""
Service API Schemas for Mario Beauty Salon Management System.
Implements Pydantic schemas for service categories and services.
"""

from pydantic import BaseModel, Field, validator
from typing import Optional
from decimal import Decimal
from datetime import datetime


class CategoryCreateSchema(BaseModel):
    """
    Schema for creating service categories.
    Task 5.4 - Create Service API Schemas implementation.
    """
    
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Category name (e.g., 'Hair Services', 'Nail Care')"
    )
    
    description: Optional[str] = Field(
        None,
        description="Category description"
    )
    
    parent_id: Optional[int] = Field(
        None,
        description="Parent category ID for hierarchy"
    )
    
    is_active: bool = Field(
        True,
        description="Whether this category is available for booking"
    )
    
    display_order: int = Field(
        0,
        ge=0,
        description="Order for displaying categories"
    )
    
    @validator('name')
    def validate_name(cls, v):
        """Validate category name."""
        if not v or not v.strip():
            raise ValueError("Category name cannot be empty")
        return v.strip()


class CategoryUpdateSchema(BaseModel):
    """Schema for updating service categories."""
    
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Category name"
    )
    
    description: Optional[str] = Field(
        None,
        description="Category description"
    )
    
    parent_id: Optional[int] = Field(
        None,
        description="Parent category ID"
    )
    
    is_active: Optional[bool] = Field(
        None,
        description="Whether category is active"
    )
    
    display_order: Optional[int] = Field(
        None,
        ge=0,
        description="Display order"
    )
    
    @validator('name')
    def validate_name(cls, v):
        """Validate category name."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("Category name cannot be empty")
        return v.strip() if v else v


class CategoryResponseSchema(BaseModel):
    """Schema for category API responses."""
    
    id: int
    name: str
    description: str
    parent_id: Optional[int]
    full_name: str
    level: int
    is_active: bool
    display_order: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ServiceCreateSchema(BaseModel):
    """
    Schema for creating services.
    Task 5.4 - Create Service API Schemas implementation.
    """
    
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Service name (e.g., 'Haircut', 'Manicure')"
    )
    
    description: Optional[str] = Field(
        None,
        description="Detailed service description"
    )
    
    category_id: int = Field(
        ...,
        description="Service category ID"
    )
    
    base_price: Decimal = Field(
        ...,
        ge=Decimal('1.00'),
        le=Decimal('1000.00'),
        description="Base price in salon currency ($1.00-$1000.00)"
    )
    
    duration_minutes: int = Field(
        ...,
        ge=15,
        le=480,
        description="Service duration in minutes (15-480 min)"
    )
    
    is_active: bool = Field(
        True,
        description="Whether service is available for booking"
    )
    
    requires_consultation: bool = Field(
        False,
        description="Whether service requires consultation first"
    )
    
    preparation_time: int = Field(
        0,
        ge=0,
        le=60,
        description="Preparation time in minutes (0-60 min)"
    )
    
    cleanup_time: int = Field(
        0,
        ge=0,
        le=30,
        description="Cleanup time in minutes (0-30 min)"
    )
    
    display_order: int = Field(
        0,
        ge=0,
        description="Order for displaying services within category"
    )
    
    @validator('name')
    def validate_name(cls, v):
        """Validate service name."""
        if not v or not v.strip():
            raise ValueError("Service name cannot be empty")
        return v.strip()
    
    @validator('base_price')
    def validate_price(cls, v):
        """Validate service price."""
        if v < Decimal('1.00') or v > Decimal('1000.00'):
            raise ValueError("Service price must be between $1.00 and $1000.00")
        return v


class ServiceUpdateSchema(BaseModel):
    """
    Schema for updating services.
    Task 5.4 - Create Service API Schemas implementation.
    """
    
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Service name"
    )
    
    description: Optional[str] = Field(
        None,
        description="Service description"
    )
    
    category_id: Optional[int] = Field(
        None,
        description="Service category ID"
    )
    
    base_price: Optional[Decimal] = Field(
        None,
        ge=Decimal('1.00'),
        le=Decimal('1000.00'),
        description="Base price"
    )
    
    duration_minutes: Optional[int] = Field(
        None,
        ge=15,
        le=480,
        description="Service duration in minutes"
    )
    
    is_active: Optional[bool] = Field(
        None,
        description="Whether service is active"
    )
    
    requires_consultation: Optional[bool] = Field(
        None,
        description="Requires consultation"
    )
    
    preparation_time: Optional[int] = Field(
        None,
        ge=0,
        le=60,
        description="Preparation time in minutes"
    )
    
    cleanup_time: Optional[int] = Field(
        None,
        ge=0,
        le=30,
        description="Cleanup time in minutes"
    )
    
    display_order: Optional[int] = Field(
        None,
        ge=0,
        description="Display order"
    )
    
    @validator('name')
    def validate_name(cls, v):
        """Validate service name."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("Service name cannot be empty")
        return v.strip() if v else v
    
    @validator('base_price')
    def validate_price(cls, v):
        """Validate service price."""
        if v is not None and (v < Decimal('1.00') or v > Decimal('1000.00')):
            raise ValueError("Service price must be between $1.00 and $1000.00")
        return v


class ServiceResponseSchema(BaseModel):
    """Schema for service API responses."""
    
    id: int
    name: str
    description: str
    category_id: int
    base_price: Decimal
    duration_minutes: int
    is_active: bool
    requires_consultation: bool
    preparation_time: int
    cleanup_time: int
    display_order: int
    total_duration_minutes: int
    formatted_price: str
    formatted_duration: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ServiceListResponseSchema(BaseModel):
    """Schema for service list responses with pagination."""
    
    services: list[ServiceResponseSchema]
    total: int
    page: int
    page_size: int
    total_pages: int


class CategoryListResponseSchema(BaseModel):
    """Schema for category list responses with pagination."""
    
    categories: list[CategoryResponseSchema]
    total: int
    page: int
    page_size: int
    total_pages: int
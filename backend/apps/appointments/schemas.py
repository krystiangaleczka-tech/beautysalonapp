"""
Pydantic schemas for Appointment API endpoints.
Provides request/response validation and serialization for the Appointment management system.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal


class AppointmentCreateSchema(BaseModel):
    """
    Schema for creating a new appointment.
    Used for POST /api/appointments/ requests.
    """
    client_id: int = Field(
        gt=0,
        description="ID of the client for this appointment"
    )
    
    service_id: int = Field(
        gt=0,
        description="ID of the service to be provided"
    )
    
    staff_member_id: int = Field(
        gt=0,
        description="ID of the staff member providing the service"
    )
    
    scheduled_start_time: datetime = Field(
        description="Scheduled start time for the appointment"
    )
    
    scheduled_end_time: datetime = Field(
        description="Scheduled end time for the appointment"
    )
    
    price: Decimal = Field(
        gt=0,
        description="Final price for the appointment"
    )
    
    notes: Optional[str] = Field(
        default=None,
        description="Additional notes about the appointment"
    )
    
    @field_validator('scheduled_start_time', 'scheduled_end_time')
    @classmethod
    def validate_future_time(cls, v):
        """Validate that appointment times are not in the past."""
        from django.utils import timezone
        if v < timezone.now():
            raise ValueError('Appointment times cannot be in the past')
        return v
    
    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        """Validate that price is positive."""
        if v <= 0:
            raise ValueError('Price must be positive')
        return v
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "client_id": 1,
                "service_id": 1,
                "staff_member_id": 1,
                "scheduled_start_time": "2024-02-15T10:00:00Z",
                "scheduled_end_time": "2024-02-15T10:30:00Z",
                "price": "25.00",
                "notes": "Client prefers morning appointments"
            }
        }
    )


class AppointmentUpdateSchema(BaseModel):
    """
    Schema for updating an existing appointment.
    Used for PUT/PATCH /api/appointments/{id}/ requests.
    All fields are optional for partial updates.
    """
    client_id: Optional[int] = Field(
        default=None,
        gt=0,
        description="ID of the client for this appointment"
    )
    
    service_id: Optional[int] = Field(
        default=None,
        gt=0,
        description="ID of the service to be provided"
    )
    
    staff_member_id: Optional[int] = Field(
        default=None,
        gt=0,
        description="ID of the staff member providing the service"
    )
    
    scheduled_start_time: Optional[datetime] = Field(
        default=None,
        description="Scheduled start time for the appointment"
    )
    
    scheduled_end_time: Optional[datetime] = Field(
        default=None,
        description="Scheduled end time for the appointment"
    )
    
    status: Optional[str] = Field(
        default=None,
        description="Current status of the appointment"
    )
    
    payment_status: Optional[str] = Field(
        default=None,
        description="Payment status of the appointment"
    )
    
    price: Optional[Decimal] = Field(
        default=None,
        gt=0,
        description="Final price for the appointment"
    )
    
    notes: Optional[str] = Field(
        default=None,
        description="Additional notes about the appointment"
    )
    
    cancellation_reason: Optional[str] = Field(
        default=None,
        description="Reason for cancellation (if applicable)"
    )
    
    @field_validator('scheduled_start_time', 'scheduled_end_time')
    @classmethod
    def validate_future_time(cls, v):
        """Validate that appointment times are not in the past."""
        if v is not None:
            from django.utils import timezone
            if v < timezone.now():
                raise ValueError('Appointment times cannot be in the past')
        return v
    
    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        """Validate that price is positive."""
        if v is not None and v <= 0:
            raise ValueError('Price must be positive')
        return v
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "confirmed",
                "notes": "Client confirmed via phone"
            }
        }
    )


class AppointmentResponseSchema(BaseModel):
    """
    Schema for appointment API responses.
    Used for GET requests and successful POST/PUT responses.
    """
    id: int = Field(description="Unique appointment identifier")
    client_id: int = Field(description="ID of the client for this appointment")
    service_id: int = Field(description="ID of the service to be provided")
    staff_member_id: int = Field(description="ID of the staff member providing the service")
    scheduled_start_time: datetime = Field(description="Scheduled start time for the appointment")
    scheduled_end_time: datetime = Field(description="Scheduled end time for the appointment")
    status: str = Field(description="Current status of the appointment")
    payment_status: str = Field(description="Payment status of the appointment")
    price: Decimal = Field(description="Final price for the appointment")
    notes: Optional[str] = Field(default=None, description="Additional notes about the appointment")
    cancellation_reason: Optional[str] = Field(default=None, description="Reason for cancellation (if applicable)")
    actual_start_time: Optional[datetime] = Field(default=None, description="Actual start time of the service")
    actual_end_time: Optional[datetime] = Field(default=None, description="Actual end time of the service")
    created_at: datetime = Field(description="When the appointment record was created")
    updated_at: datetime = Field(description="When the appointment record was last updated")
    
    # Computed fields
    client_name: str = Field(description="Client's full name")
    service_name: str = Field(description="Service name")
    staff_name: str = Field(description="Staff member's full name")
    duration_minutes: int = Field(description="Appointment duration in minutes")
    
    model_config = ConfigDict(
        from_attributes=True,  # Enable ORM mode for Django model conversion
        json_schema_extra={
            "example": {
                "id": 1,
                "client_id": 1,
                "service_id": 1,
                "staff_member_id": 1,
                "scheduled_start_time": "2024-02-15T10:00:00Z",
                "scheduled_end_time": "2024-02-15T10:30:00Z",
                "status": "pending",
                "payment_status": "pending",
                "price": "25.00",
                "notes": "Client prefers morning appointments",
                "cancellation_reason": None,
                "actual_start_time": None,
                "actual_end_time": None,
                "created_at": "2024-02-10T14:30:00Z",
                "updated_at": "2024-02-10T14:30:00Z",
                "client_name": "John Doe",
                "service_name": "Basic Manicure",
                "staff_name": "Jane Smith",
                "duration_minutes": 30
            }
        }
    )


class AppointmentListResponseSchema(BaseModel):
    """
    Schema for paginated appointment list responses.
    Used for GET /api/appointments/ with pagination.
    """
    appointments: List[AppointmentResponseSchema] = Field(description="List of appointments for current page")
    total: int = Field(description="Total number of appointments")
    page: int = Field(description="Current page number")
    page_size: int = Field(description="Number of appointments per page")
    total_pages: int = Field(description="Total number of pages")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "appointments": [
                    {
                        "id": 1,
                        "client_id": 1,
                        "service_id": 1,
                        "staff_member_id": 1,
                        "scheduled_start_time": "2024-02-15T10:00:00Z",
                        "scheduled_end_time": "2024-02-15T10:30:00Z",
                        "status": "pending",
                        "payment_status": "pending",
                        "price": "25.00",
                        "notes": "Client prefers morning appointments",
                        "cancellation_reason": None,
                        "actual_start_time": None,
                        "actual_end_time": None,
                        "created_at": "2024-02-10T14:30:00Z",
                        "updated_at": "2024-02-10T14:30:00Z",
                        "client_name": "John Doe",
                        "service_name": "Basic Manicure",
                        "staff_name": "Jane Smith",
                        "duration_minutes": 30
                    }
                ],
                "total": 150,
                "page": 1,
                "page_size": 20,
                "total_pages": 8
            }
        }
    )


class AvailabilityCheckSchema(BaseModel):
    """
    Schema for availability check requests.
    Used for GET /api/appointments/availability/ requests.
    """
    staff_member_id: int = Field(
        gt=0,
        description="ID of the staff member to check availability for"
    )
    
    date: str = Field(
        description="Date to check availability for (YYYY-MM-DD format)"
    )
    
    service_id: int = Field(
        gt=0,
        description="ID of the service to be provided"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "staff_member_id": 1,
                "date": "2024-02-15",
                "service_id": 1
            }
        }
    )


class AvailableSlotsResponseSchema(BaseModel):
    """
    Schema for available time slots response.
    Used for GET /api/appointments/availability/ responses.
    """
    date: str = Field(description="Date for which availability is checked")
    staff_member_id: int = Field(description="ID of the staff member")
    staff_member_name: str = Field(description="Name of the staff member")
    service_id: int = Field(description="ID of the service")
    service_name: str = Field(description="Name of the service")
    service_duration: int = Field(description="Duration of the service in minutes")
    available_slots: List[str] = Field(description="List of available time slots in HH:MM format")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "date": "2024-02-15",
                "staff_member_id": 1,
                "staff_member_name": "Jane Smith",
                "service_id": 1,
                "service_name": "Basic Manicure",
                "service_duration": 30,
                "available_slots": [
                    "09:00",
                    "09:30",
                    "10:00",
                    "11:00",
                    "11:30",
                    "14:00",
                    "14:30",
                    "15:00"
                ]
            }
        }
    )
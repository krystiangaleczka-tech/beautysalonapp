"""
Staff API schemas for Mario Beauty Salon Management System.
Provides Pydantic models for staff-related API operations.
"""

from typing import List, Optional, Dict, Any
from datetime import time, date
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum


class SpecializationType(str, Enum):
    """Specialization types for staff members."""
    NAIL_CARE = "nail_care"
    SKIN_CARE = "skin_care"
    FOOT_CARE = "foot_care"
    BEAUTY_TREATMENT = "beauty_treatment"


class CertificationLevel(str, Enum):
    """Certification levels for staff members."""
    TRAINEE = "trainee"
    JUNIOR = "junior"
    SENIOR = "senior"
    MASTER = "master"
    EXPERT = "expert"


class DayOfWeek(int, Enum):
    """Days of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class SpecializationSchema(BaseModel):
    """Schema for staff specialization."""
    id: Optional[int] = None
    name: str = Field(..., max_length=100, description="Specialization name")
    specialization_type: SpecializationType = Field(..., description="Type of specialization")
    description: Optional[str] = Field(None, description="Detailed description of the specialization")
    certification_required: bool = Field(False, description="Whether this specialization requires certification")
    is_active: bool = Field(True, description="Whether this specialization is currently offered")


class WorkingHoursSchema(BaseModel):
    """Schema for staff working hours."""
    id: Optional[int] = None
    day_of_week: DayOfWeek = Field(..., description="Day of the week (1=Monday, 7=Sunday)")
    start_time: time = Field(..., description="Start time for this day")
    end_time: time = Field(..., description="End time for this day")
    is_available: bool = Field(True, description="Whether the staff member is available on this day")
    break_start_time: Optional[time] = Field(None, description="Break start time (optional)")
    break_end_time: Optional[time] = Field(None, description="Break end time (optional)")

    @model_validator(mode='after')
    def validate_times(self) -> 'WorkingHoursSchema':
        """Validate that times are in correct order."""
        if self.is_available:
            # Validate start time is before end time
            if self.start_time and self.end_time and self.start_time >= self.end_time:
                raise ValueError("Start time must be before end time")
            
            # Validate break times if provided
            if self.break_start_time and self.break_end_time:
                if self.break_start_time >= self.break_end_time:
                    raise ValueError("Break start time must be before break end time")
                
                # Validate break times are within working hours
                if (self.break_start_time < self.start_time or 
                    self.break_end_time > self.end_time):
                    raise ValueError("Break times must be within working hours")
        
        return self


class StaffCreateSchema(BaseModel):
    """Schema for creating a new staff member."""
    # User fields
    username: str = Field(..., min_length=3, max_length=150, description="Username for the staff member")
    email: str = Field(..., description="Email address")
    first_name: str = Field(..., max_length=150, description="First name")
    last_name: str = Field(..., max_length=150, description="Last name")
    phone_number: Optional[str] = Field(None, max_length=20, description="Contact phone number")
    employee_id: Optional[str] = Field(None, max_length=10, description="Unique employee identifier")
    
    # Staff profile fields
    certification_level: CertificationLevel = Field(CertificationLevel.JUNIOR, description="Certification level")
    years_of_experience: int = Field(0, ge=0, le=50, description="Years of professional experience")
    hourly_rate: Optional[float] = Field(None, ge=0.01, description="Hourly rate for services")
    max_clients_per_day: int = Field(8, ge=1, le=20, description="Maximum number of clients per day")
    languages_spoken: Optional[str] = Field(None, description="Comma-separated list of languages spoken")
    availability_notes: Optional[str] = Field(None, description="Special notes about availability")
    is_accepting_new_clients: bool = Field(True, description="Whether accepting new clients")
    emergency_contact_name: Optional[str] = Field(None, max_length=100, description="Emergency contact name")
    emergency_contact_phone: Optional[str] = Field(None, max_length=20, description="Emergency contact phone")
    
    # Specializations
    specializations: List[int] = Field(default_factory=list, description="List of specialization IDs")
    
    # Working hours
    working_hours: List[WorkingHoursSchema] = Field(default_factory=list, description="List of working hours")


class StaffUpdateSchema(BaseModel):
    """Schema for updating a staff member."""
    # User fields
    email: Optional[str] = Field(None, description="Email address")
    first_name: Optional[str] = Field(None, max_length=150, description="First name")
    last_name: Optional[str] = Field(None, max_length=150, description="Last name")
    phone_number: Optional[str] = Field(None, max_length=20, description="Contact phone number")
    employee_id: Optional[str] = Field(None, max_length=10, description="Unique employee identifier")
    
    # Staff profile fields
    certification_level: Optional[CertificationLevel] = Field(None, description="Certification level")
    years_of_experience: Optional[int] = Field(None, ge=0, le=50, description="Years of professional experience")
    hourly_rate: Optional[float] = Field(None, ge=0.01, description="Hourly rate for services")
    max_clients_per_day: Optional[int] = Field(None, ge=1, le=20, description="Maximum number of clients per day")
    languages_spoken: Optional[str] = Field(None, description="Comma-separated list of languages spoken")
    availability_notes: Optional[str] = Field(None, description="Special notes about availability")
    is_accepting_new_clients: Optional[bool] = Field(None, description="Whether accepting new clients")
    emergency_contact_name: Optional[str] = Field(None, max_length=100, description="Emergency contact name")
    emergency_contact_phone: Optional[str] = Field(None, max_length=20, description="Emergency contact phone")
    
    # Specializations
    specializations: Optional[List[int]] = Field(None, description="List of specialization IDs")


class ScheduleUpdateSchema(BaseModel):
    """Schema for updating staff schedule."""
    working_hours: List[WorkingHoursSchema] = Field(..., description="List of working hours to update")


class StaffResponseSchema(BaseModel):
    """Schema for staff response data."""
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[str]
    employee_id: Optional[str]
    role: str
    is_active_staff: bool
    hire_date: Optional[date]
    
    # Staff profile fields
    certification_level: str
    years_of_experience: int
    hourly_rate: Optional[float]
    max_clients_per_day: int
    languages_spoken: Optional[str]
    availability_notes: Optional[str]
    is_accepting_new_clients: bool
    emergency_contact_name: Optional[str]
    emergency_contact_phone: Optional[str]
    
    # Related data
    specializations: List[SpecializationSchema]
    working_hours: List[WorkingHoursSchema]
    
    # Computed fields
    full_name: str
    primary_specialization: Optional[str]
    
    class Config:
        from_attributes = True


class AvailabilityCheckSchema(BaseModel):
    """Schema for checking staff availability."""
    check_date: date = Field(..., description="Date to check availability")
    specialization_id: Optional[int] = Field(None, description="Optional specialization filter")


class TimeSlotSchema(BaseModel):
    """Schema for available time slots."""
    start_time: time
    end_time: time
    duration_minutes: int


class StaffAvailabilitySchema(BaseModel):
    """Schema for staff availability response."""
    staff_id: int
    staff_name: str
    available_slots: List[TimeSlotSchema]


# Convenience schemas for common operations
class SpecializationCreateSchema(BaseModel):
    """Schema for creating a new specialization."""
    name: str = Field(..., max_length=100, description="Specialization name")
    specialization_type: SpecializationType = Field(..., description="Type of specialization")
    description: Optional[str] = Field(None, description="Detailed description of the specialization")
    certification_required: bool = Field(False, description="Whether this specialization requires certification")


class SpecializationUpdateSchema(BaseModel):
    """Schema for updating a specialization."""
    name: Optional[str] = Field(None, max_length=100, description="Specialization name")
    specialization_type: Optional[SpecializationType] = Field(None, description="Type of specialization")
    description: Optional[str] = Field(None, description="Detailed description of the specialization")
    certification_required: Optional[bool] = Field(None, description="Whether this specialization requires certification")
    is_active: Optional[bool] = Field(None, description="Whether this specialization is currently offered")
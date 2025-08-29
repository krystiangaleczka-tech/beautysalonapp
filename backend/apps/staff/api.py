"""
Staff API endpoints for Mario Beauty Salon Management System.
Provides CRUD operations for staff management and scheduling.
"""

from ninja import Router
from django.shortcuts import get_object_or_404
from django.db import transaction  # type: ignore
from django.core.exceptions import ValidationError
from typing import List

from apps.staff.models import StaffProfile, WorkingHours, Specialization
from apps.staff.schemas import (
    StaffCreateSchema, 
    StaffUpdateSchema, 
    StaffResponseSchema,
    ScheduleUpdateSchema,
    AvailabilityCheckSchema,
    StaffAvailabilitySchema,
    TimeSlotSchema,
    SpecializationCreateSchema,
    SpecializationUpdateSchema
)
from apps.staff.services import (
    StaffAvailabilityService,
    WorkingHoursService,
    get_available_staff,
    get_available_time_slots
)
from apps.authentication.models import SalonUser

router = Router(tags=["Staff"])


@router.post("/")
def create_staff(request, payload: StaffCreateSchema):
    """Create a new staff member."""
    with transaction.atomic():  # type: ignore
        # Create the user
        user = SalonUser.objects.create_user(
            username=payload.username,
            email=payload.email,
            first_name=payload.first_name,
            last_name=payload.last_name,
            phone_number=payload.phone_number,
            employee_id=payload.employee_id,
            is_active_staff=True
        )
        
        # Create the staff profile
        staff_profile = StaffProfile.objects.create(  # type: ignore
            user=user,
            certification_level=payload.certification_level,
            years_of_experience=payload.years_of_experience,
            hourly_rate=payload.hourly_rate,
            max_clients_per_day=payload.max_clients_per_day,
            languages_spoken=payload.languages_spoken,
            availability_notes=payload.availability_notes,
            is_accepting_new_clients=payload.is_accepting_new_clients,
            emergency_contact_name=payload.emergency_contact_name,
            emergency_contact_phone=payload.emergency_contact_phone
        )
        
        # Add specializations
        if payload.specializations:
            specializations = Specialization.objects.filter(id__in=payload.specializations)  # type: ignore
            staff_profile.specializations.set(specializations)
        
        # Create working hours
        for wh_data in payload.working_hours:
            WorkingHours.objects.create(  # type: ignore
                staff_profile=staff_profile,
                day_of_week=wh_data.day_of_week,
                start_time=wh_data.start_time,
                end_time=wh_data.end_time,
                is_available=wh_data.is_available,
                break_start_time=wh_data.break_start_time,
                break_end_time=wh_data.break_end_time
            )
    
    return {"success": True, "staff_id": staff_profile.id}  # type: ignore


@router.get("/")
def list_staff(request):
    """List all staff members."""
    staff_profiles = StaffProfile.objects.select_related('user').prefetch_related(  # type: ignore
        'specializations', 'working_hours'
    ).all()
    return [{"id": s.id, "name": s.user.get_full_name()} for s in staff_profiles]  # type: ignore


@router.get("/{staff_id}/")
def get_staff(request, staff_id: int):
    """Get a specific staff member."""
    staff_profile = get_object_or_404(
        StaffProfile.objects.select_related('user').prefetch_related(  # type: ignore
            'specializations', 'working_hours'
        ), 
        id=staff_id
    )  # type: ignore
    return {"id": staff_profile.id, "name": staff_profile.user.get_full_name()}  # type: ignore


@router.put("/{staff_id}/")
def update_staff(request, staff_id: int, payload: StaffUpdateSchema):
    """Update a staff member."""
    staff_profile = get_object_or_404(StaffProfile, id=staff_id)  # type: ignore
    user = staff_profile.user
    
    # Update user fields
    user_fields = [
        'email', 'first_name', 'last_name', 'phone_number', 
        'employee_id'
    ]
    for field in user_fields:
        value = getattr(payload, field)
        if value is not None:
            setattr(user, field, value)
    
    user.save()
    
    # Update staff profile fields
    staff_fields = [
        'certification_level', 'years_of_experience', 'hourly_rate',
        'max_clients_per_day', 'languages_spoken', 'availability_notes',
        'is_accepting_new_clients', 'emergency_contact_name', 
        'emergency_contact_phone'
    ]
    for field in staff_fields:
        value = getattr(payload, field)
        if value is not None:
            setattr(staff_profile, field, value)
    
    staff_profile.save()
    
    # Update specializations if provided
    if payload.specializations is not None:
        specializations = Specialization.objects.filter(id__in=payload.specializations)  # type: ignore
        staff_profile.specializations.set(specializations)
    
    return {"success": True}


@router.delete("/{staff_id}/")
def delete_staff(request, staff_id: int):
    """Delete a staff member (soft delete)."""
    staff_profile = get_object_or_404(StaffProfile, id=staff_id)  # type: ignore
    staff_profile.delete()  # This performs a soft delete
    return {"success": True}


@router.put("/{staff_id}/schedule/")
def update_staff_schedule(request, staff_id: int, payload: ScheduleUpdateSchema):
    """Update a staff member's schedule."""
    staff_profile = get_object_or_404(StaffProfile, id=staff_id)  # type: ignore
    
    # Delete existing working hours
    staff_profile.working_hours.all().delete()  # type: ignore
    
    # Create new working hours
    working_hours_list = []
    for wh_data in payload.working_hours:
        working_hours = WorkingHours.objects.create(  # type: ignore
            staff_profile=staff_profile,
            day_of_week=wh_data.day_of_week,
            start_time=wh_data.start_time,
            end_time=wh_data.end_time,
            is_available=wh_data.is_available,
            break_start_time=wh_data.break_start_time,
            break_end_time=wh_data.break_end_time
        )
        working_hours_list.append(working_hours)
    
    return {"success": True}


@router.get("/{staff_id}/availability/", response=List[TimeSlotSchema])
def check_staff_availability(request, staff_id: int, date: str):
    """Check availability for a specific staff member on a date."""
    from datetime import datetime
    
    staff_profile = get_object_or_404(StaffProfile, id=staff_id)  # type: ignore
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    
    slots = get_available_time_slots(staff_profile, target_date, 60)
    
    # Convert to TimeSlotSchema format
    time_slots = []
    for start_time, end_time in slots:
        # Calculate duration in minutes
        duration = (datetime.combine(target_date, end_time) - 
                   datetime.combine(target_date, start_time)).seconds // 60
        time_slots.append(TimeSlotSchema(
            start_time=start_time,
            end_time=end_time,
            duration_minutes=duration
        ))
    
    return time_slots


@router.post("/availability-check/", response=List[StaffAvailabilitySchema])
def check_availability(request, payload: AvailabilityCheckSchema):
    """Check availability for all staff on a specific date."""
    available_staff = get_available_staff(
        payload.check_date, 
        Specialization.objects.filter(id=payload.specialization_id).first()  # type: ignore 
        if payload.specialization_id else None
    )
    
    result = []
    for staff in available_staff:
        slots = get_available_time_slots(staff, payload.check_date, 60)
        time_slots = []
        for start_time, end_time in slots:
            time_slots.append(TimeSlotSchema(
                start_time=start_time,
                end_time=end_time,
                duration_minutes=60
            ))
        
        result.append(StaffAvailabilitySchema(
            staff_id=staff.id,  # type: ignore
            staff_name=staff.user.get_full_name(),  # type: ignore
            available_slots=time_slots
        ))
    
    return result


# Specialization endpoints
@router.post("/specializations/")
def create_specialization(request, payload: SpecializationCreateSchema):
    """Create a new specialization."""
    specialization = Specialization.objects.create(  # type: ignore
        name=payload.name,
        specialization_type=payload.specialization_type,
        description=payload.description,
        certification_required=payload.certification_required
    )
    return {"success": True, "id": specialization.id}  # type: ignore


@router.get("/specializations/")
def list_specializations(request):
    """List all specializations."""
    specializations = Specialization.objects.filter(is_active=True)  # type: ignore
    return [{"id": s.id, "name": s.name} for s in specializations]  # type: ignore


@router.put("/specializations/{specialization_id}/")
def update_specialization(request, specialization_id: int, payload: SpecializationUpdateSchema):
    """Update a specialization."""
    specialization = get_object_or_404(Specialization, id=specialization_id)  # type: ignore
    
    update_fields = [
        'name', 'specialization_type', 'description', 
        'certification_required', 'is_active'
    ]
    
    for field in update_fields:
        value = getattr(payload, field)
        if value is not None:
            setattr(specialization, field, value)
    
    specialization.save()
    return {"success": True}


@router.delete("/specializations/{specialization_id}/")
def delete_specialization(request, specialization_id: int):
    """Delete a specialization (soft delete)."""
    specialization = get_object_or_404(Specialization, id=specialization_id)
    specialization.delete()  # This performs a soft delete
    return {"success": True}
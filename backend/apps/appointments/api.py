from ninja import Router
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils import timezone
from typing import List, Optional
import math
from datetime import datetime, timedelta

from .models import Appointment
from .schemas import (
    AppointmentCreateSchema,
    AppointmentUpdateSchema,
    AppointmentResponseSchema,
    AppointmentListResponseSchema,
    AvailabilityCheckSchema,
    AvailableSlotsResponseSchema
)
from .services import AppointmentService
from apps.clients.models import Client
from apps.services.models import Service
from apps.staff.models import StaffProfile

router = Router()


@router.post("/", response=AppointmentResponseSchema, tags=["Appointments"])
def create_appointment(request, data: AppointmentCreateSchema):
    """
    Create a new appointment.
    
    Creates a new appointment with the provided information.
    Validates conflicts and returns the created appointment data.
    """
    try:
        # Get related objects
        client = get_object_or_404(Client, id=data.client_id)
        service = get_object_or_404(Service, id=data.service_id)
        staff_member = get_object_or_404(StaffProfile, id=data.staff_member_id)
        
        # Validate appointment time
        is_valid, error_message = AppointmentService.validate_appointment_time(
            staff_member, data.scheduled_start_time, data.scheduled_end_time
        )
        if not is_valid:
            raise ValidationError(error_message)
        
        # Validate duration matches service
        time_diff = data.scheduled_end_time - data.scheduled_start_time
        scheduled_duration = time_diff.total_seconds() / 60
        service_duration = service.total_duration_minutes
        if scheduled_duration != service_duration:
            raise ValidationError(
                f"Appointment duration ({scheduled_duration} minutes) must match service duration ({service_duration} minutes)"
            )
        
        # Create appointment
        appointment_data = data.model_dump()
        appointment = Appointment.objects.create(**appointment_data)
        
        # Return response with computed fields
        return AppointmentResponseSchema(
            id=appointment.id,
            client_id=appointment.client_id,
            service_id=appointment.service_id,
            staff_member_id=appointment.staff_member_id,
            scheduled_start_time=appointment.scheduled_start_time,
            scheduled_end_time=appointment.scheduled_end_time,
            status=appointment.status,
            payment_status=appointment.payment_status,
            price=appointment.price,
            notes=appointment.notes,
            cancellation_reason=appointment.cancellation_reason,
            actual_start_time=appointment.actual_start_time,
            actual_end_time=appointment.actual_end_time,
            created_at=appointment.created_at,
            updated_at=appointment.updated_at,
            client_name=appointment.client.full_name,
            service_name=appointment.service.name,
            staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            duration_minutes=appointment.duration_minutes
        )
    except ValidationError as e:
        raise ValidationError(f"Appointment creation failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error creating appointment: {e}")


@router.get("/{appointment_id}", response=AppointmentResponseSchema, tags=["Appointments"])
def get_appointment(request, appointment_id: int):
    """
    Get a specific appointment by ID.
    
    Returns detailed appointment information including computed fields.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.put("/{appointment_id}", response=AppointmentResponseSchema, tags=["Appointments"])
def update_appointment(request, appointment_id: int, data: AppointmentUpdateSchema):
    """
    Update an existing appointment.
    
    Updates appointment information with provided data.
    Only provided fields will be updated (partial update).
    Validates conflicts if time is changed.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    try:
        # Update only provided fields
        update_data = data.model_dump(exclude_unset=True)
        
        # If time is being updated, validate conflicts
        if 'scheduled_start_time' in update_data or 'scheduled_end_time' in update_data:
            # Get the staff member (existing or new)
            staff_member = appointment.staff_member
            if 'staff_member_id' in update_data:
                staff_member = get_object_or_404(StaffProfile, id=update_data['staff_member_id'])
            
            # Get start and end times (existing or new)
            start_time = update_data.get('scheduled_start_time', appointment.scheduled_start_time)
            end_time = update_data.get('scheduled_end_time', appointment.scheduled_end_time)
            
            # Validate appointment time
            is_valid, error_message = AppointmentService.validate_appointment_time(
                staff_member, start_time, end_time, appointment_id
            )
            if not is_valid:
                raise ValidationError(error_message)
        
        # Update fields
        for field, value in update_data.items():
            setattr(appointment, field, value)
        
        appointment.full_clean()  # Validate model
        appointment.save()
        
        return AppointmentResponseSchema(
            id=appointment.id,
            client_id=appointment.client_id,
            service_id=appointment.service_id,
            staff_member_id=appointment.staff_member_id,
            scheduled_start_time=appointment.scheduled_start_time,
            scheduled_end_time=appointment.scheduled_end_time,
            status=appointment.status,
            payment_status=appointment.payment_status,
            price=appointment.price,
            notes=appointment.notes,
            cancellation_reason=appointment.cancellation_reason,
            actual_start_time=appointment.actual_start_time,
            actual_end_time=appointment.actual_end_time,
            created_at=appointment.created_at,
            updated_at=appointment.updated_at,
            client_name=appointment.client.full_name,
            service_name=appointment.service.name,
            staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            duration_minutes=appointment.duration_minutes
        )
    except ValidationError as e:
        raise ValidationError(f"Appointment update failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error updating appointment: {e}")


@router.delete("/{appointment_id}", tags=["Appointments"])
def delete_appointment(request, appointment_id: int):
    """
    Delete an appointment.
    
    Permanently removes an appointment from the system.
    Use with caution - this action cannot be undone.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment_details = {
        "client": appointment.client.full_name,
        "service": appointment.service.name,
        "staff": f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        "time": appointment.scheduled_start_time.isoformat()
    }
    appointment.delete()
    
    return {
        "success": True,
        "message": f"Appointment for {appointment_details['client']} has been successfully deleted",
        "deleted_appointment": appointment_details
    }


@router.get("/", response=AppointmentListResponseSchema, tags=["Appointments"])
def list_appointments(request, page: int = 1, page_size: int = 20, status: Optional[str] = None):
    """
    List all appointments with pagination.
    
    Returns a paginated list of all appointments in the system.
    Optionally filter by status.
    """
    # Validate pagination parameters
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 100:
        page_size = 20
    
    # Build query
    queryset = Appointment.objects.all()
    
    # Filter by status if provided
    if status:
        queryset = queryset.filter(status=status)
    
    # Get total count
    total = queryset.count()
    total_pages = math.ceil(total / page_size)
    
    # Calculate offset
    offset = (page - 1) * page_size
    
    # Get appointments for current page
    appointments = queryset.order_by('-scheduled_start_time')[offset:offset + page_size]
    
    # Convert to response schemas
    appointment_list = [
        AppointmentResponseSchema(
            id=appointment.id,
            client_id=appointment.client_id,
            service_id=appointment.service_id,
            staff_member_id=appointment.staff_member_id,
            scheduled_start_time=appointment.scheduled_start_time,
            scheduled_end_time=appointment.scheduled_end_time,
            status=appointment.status,
            payment_status=appointment.payment_status,
            price=appointment.price,
            notes=appointment.notes,
            cancellation_reason=appointment.cancellation_reason,
            actual_start_time=appointment.actual_start_time,
            actual_end_time=appointment.actual_end_time,
            created_at=appointment.created_at,
            updated_at=appointment.updated_at,
            client_name=appointment.client.full_name,
            service_name=appointment.service.name,
            staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            duration_minutes=appointment.duration_minutes
        )
        for appointment in appointments
    ]
    
    return AppointmentListResponseSchema(
        appointments=appointment_list,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )


@router.post("/{appointment_id}/confirm", response=AppointmentResponseSchema, tags=["Appointments"])
def confirm_appointment(request, appointment_id: int):
    """
    Confirm an appointment.
    
    Changes appointment status to 'confirmed'.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if appointment.status != Appointment.AppointmentStatus.PENDING:
        raise ValidationError("Only pending appointments can be confirmed")
    
    appointment.confirm()
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.post("/{appointment_id}/cancel", response=AppointmentResponseSchema, tags=["Appointments"])
def cancel_appointment(request, appointment_id: int, reason: str = ""):
    """
    Cancel an appointment.
    
    Changes appointment status to 'cancelled' with optional reason.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if appointment.status == Appointment.AppointmentStatus.COMPLETED:
        raise ValidationError("Completed appointments cannot be cancelled")
    
    appointment.cancel(reason)
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.post("/{appointment_id}/check-in", response=AppointmentResponseSchema, tags=["Appointments"])
def check_in_appointment(request, appointment_id: int):
    """
    Mark appointment as checked in.
    
    Changes appointment status to 'checked_in' and records actual start time.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if appointment.status != Appointment.AppointmentStatus.CONFIRMED:
        raise ValidationError("Only confirmed appointments can be checked in")
    
    appointment.check_in()
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.post("/{appointment_id}/start-service", response=AppointmentResponseSchema, tags=["Appointments"])
def start_service(request, appointment_id: int):
    """
    Mark appointment as in progress.
    
    Changes appointment status to 'in_progress'.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if appointment.status != Appointment.AppointmentStatus.CHECKED_IN:
        raise ValidationError("Only checked-in appointments can start service")
    
    appointment.start_service()
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.post("/{appointment_id}/complete", response=AppointmentResponseSchema, tags=["Appointments"])
def complete_appointment(request, appointment_id: int):
    """
    Mark appointment as completed.
    
    Changes appointment status to 'completed' and records actual end time.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if appointment.status != Appointment.AppointmentStatus.IN_PROGRESS:
        raise ValidationError("Only in-progress appointments can be completed")
    
    appointment.complete()
    
    return AppointmentResponseSchema(
        id=appointment.id,
        client_id=appointment.client_id,
        service_id=appointment.service_id,
        staff_member_id=appointment.staff_member_id,
        scheduled_start_time=appointment.scheduled_start_time,
        scheduled_end_time=appointment.scheduled_end_time,
        status=appointment.status,
        payment_status=appointment.payment_status,
        price=appointment.price,
        notes=appointment.notes,
        cancellation_reason=appointment.cancellation_reason,
        actual_start_time=appointment.actual_start_time,
        actual_end_time=appointment.actual_end_time,
        created_at=appointment.created_at,
        updated_at=appointment.updated_at,
        client_name=appointment.client.full_name,
        service_name=appointment.service.name,
        staff_name=f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
        duration_minutes=appointment.duration_minutes
    )


@router.get("/availability/", response=AvailableSlotsResponseSchema, tags=["Appointments"])
def check_availability(request, data: AvailabilityCheckSchema):
    """
    Check available time slots for a staff member on a specific date.
    
    Returns available time slots based on staff working hours and existing appointments.
    """
    try:
        # Get related objects
        staff_member = get_object_or_404(StaffProfile, id=data.staff_member_id)
        service = get_object_or_404(Service, id=data.service_id)
        
        # Parse date
        date = datetime.strptime(data.date, "%Y-%m-%d").date()
        
        # Get working hours for the staff member on this day
        day_of_week = date.isoweekday()  # 1=Monday, 7=Sunday
        
        try:
            working_hours = staff_member.working_hours.get(
                day_of_week=day_of_week,
                is_available=True
            )
        except Exception:
            # Staff is not available on this day
            return AvailableSlotsResponseSchema(
                date=data.date,
                staff_member_id=staff_member.id,
                staff_member_name=f"{staff_member.user.first_name} {staff_member.user.last_name}",
                service_id=service.id,
                service_name=service.name,
                service_duration=service.total_duration_minutes,
                available_slots=[]
            )
        
        # Create datetime objects for working hours
        working_start = datetime.combine(date, working_hours.start_time)
        working_end = datetime.combine(date, working_hours.end_time)
        
        # Get available time slots
        available_slots = AppointmentService.get_available_time_slots(
            staff_member,
            datetime.combine(date, datetime.min.time()),
            service.total_duration_minutes,
            working_start,
            working_end
        )
        
        # Format time slots as strings
        formatted_slots = []
        for start_time, end_time in available_slots:
            formatted_slots.append(start_time.strftime("%H:%M"))
        
        return AvailableSlotsResponseSchema(
            date=data.date,
            staff_member_id=staff_member.id,
            staff_member_name=f"{staff_member.user.first_name} {staff_member.user.last_name}",
            service_id=service.id,
            service_name=service.name,
            service_duration=service.total_duration_minutes,
            available_slots=formatted_slots
        )
    except ValidationError as e:
        raise ValidationError(f"Availability check failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error checking availability: {e}")


# Health check endpoint
@router.get("/health", tags=["Health"])
def health_check(request):
    """Health check endpoint for appointment service."""
    return {"status": "ok", "app": "appointments"}
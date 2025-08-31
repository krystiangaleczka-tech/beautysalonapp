"""
Service layer for Appointment operations.
Provides business logic for appointment validation, conflict detection, and scheduling.
"""

from django.utils import timezone
from django.db.models import Q
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
import logging

from .models import Appointment

logger = logging.getLogger(__name__)


class AppointmentService:
    """Service class for appointment-related business logic."""
    
    @staticmethod
    def check_staff_availability(
        staff_member,
        start_time: datetime,
        end_time: datetime,
        exclude_appointment_id: Optional[int] = None
    ) -> bool:
        """
        Check if a staff member is available for the given time slot.
        
        Args:
            staff_member: StaffProfile instance
            start_time: Start time of the requested appointment
            end_time: End time of the requested appointment
            exclude_appointment_id: Appointment ID to exclude from conflict check (for updates)
            
        Returns:
            bool: True if staff is available, False if there's a conflict
        """
        try:
            # Build conflict query
            conflict_query = Q(
                staff_member=staff_member,
                scheduled_start_time__lt=end_time,
                scheduled_end_time__gt=start_time
            )
            
            # Exclude specific appointment if provided (for updates)
            if exclude_appointment_id:
                conflict_query &= ~Q(id=exclude_appointment_id)
            
            # Exclude cancelled appointments from conflict checking
            conflict_query &= ~Q(status=Appointment.AppointmentStatus.CANCELLED)
            
            # Check for conflicts
            conflicts = Appointment.objects.filter(conflict_query).exists()
            
            return not conflicts
        except Exception as e:
            logger.error(f"Error checking staff availability: {e}")
            return False
    
    @staticmethod
    def check_client_availability(
        client,
        start_time: datetime,
        end_time: datetime,
        exclude_appointment_id: Optional[int] = None
    ) -> bool:
        """
        Check if a client is available for the given time slot.
        
        Args:
            client: Client instance
            start_time: Start time of the requested appointment
            end_time: End time of the requested appointment
            exclude_appointment_id: Appointment ID to exclude from conflict check (for updates)
            
        Returns:
            bool: True if client is available, False if there's a conflict
        """
        try:
            # Build conflict query
            conflict_query = Q(
                client=client,
                scheduled_start_time__lt=end_time,
                scheduled_end_time__gt=start_time
            )
            
            # Exclude specific appointment if provided (for updates)
            if exclude_appointment_id:
                conflict_query &= ~Q(id=exclude_appointment_id)
            
            # Exclude cancelled appointments from conflict checking
            conflict_query &= ~Q(status=Appointment.AppointmentStatus.CANCELLED)
            
            # Check for conflicts
            conflicts = Appointment.objects.filter(conflict_query).exists()
            
            return not conflicts
        except Exception as e:
            logger.error(f"Error checking client availability: {e}")
            return False
    
    @staticmethod
    def get_available_time_slots(
        staff_member,
        date: datetime,
        service_duration: int,
        working_hours_start: datetime,
        working_hours_end: datetime
    ) -> List[Tuple[datetime, datetime]]:
        """
        Get available time slots for a staff member on a specific date.
        
        Args:
            staff_member: StaffProfile instance
            date: Date to check availability for
            service_duration: Duration of service in minutes
            working_hours_start: Start of working hours for the day
            working_hours_end: End of working hours for the day
            
        Returns:
            List[Tuple[datetime, datetime]]: List of available time slots (start, end)
        """
        try:
            # Get existing appointments for the day
            day_start = date.replace(hour=0, minute=0, second=0, microsecond=0)
            day_end = date.replace(hour=23, minute=59, second=59, microsecond=999999)
            
            existing_appointments = Appointment.objects.filter(
                staff_member=staff_member,
                scheduled_start_time__gte=day_start,
                scheduled_start_time__lte=day_end,
                status__in=[
                    Appointment.AppointmentStatus.PENDING,
                    Appointment.AppointmentStatus.CONFIRMED,
                    Appointment.AppointmentStatus.CHECKED_IN,
                    Appointment.AppointmentStatus.IN_PROGRESS
                ]
            ).order_by('scheduled_start_time')
            
            # Generate time slots
            available_slots = []
            current_time = working_hours_start
            
            while current_time + timedelta(minutes=service_duration) <= working_hours_end:
                slot_end = current_time + timedelta(minutes=service_duration)
                
                # Check if slot conflicts with existing appointments
                has_conflict = False
                for appointment in existing_appointments:
                    if (current_time < appointment.scheduled_end_time and 
                        slot_end > appointment.scheduled_start_time):
                        has_conflict = True
                        break
                
                if not has_conflict:
                    available_slots.append((current_time, slot_end))
                
                # Move to next slot (30-minute intervals)
                current_time += timedelta(minutes=30)
            
            return available_slots
        except Exception as e:
            logger.error(f"Error getting available time slots: {e}")
            return []
    
    @staticmethod
    def validate_appointment_time(
        staff_member,
        start_time: datetime,
        end_time: datetime,
        exclude_appointment_id: Optional[int] = None
    ) -> Tuple[bool, str]:
        """
        Validate appointment time for conflicts and business rules.
        
        Args:
            staff_member: StaffProfile instance
            start_time: Proposed start time
            end_time: Proposed end time
            exclude_appointment_id: Appointment ID to exclude from validation
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        # Check if start time is in the past
        if start_time < timezone.now():
            return False, "Cannot schedule appointments in the past"
        
        # Check if start time is before end time
        if start_time >= end_time:
            return False, "Start time must be before end time"
        
        # Check staff availability
        if not AppointmentService.check_staff_availability(
            staff_member, start_time, end_time, exclude_appointment_id
        ):
            return False, "Staff member is not available at the requested time"
        
        return True, ""
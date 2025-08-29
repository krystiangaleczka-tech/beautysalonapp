"""
Staff business logic services for Mario Beauty Salon Management System.
Provides advanced availability calculations and working hours management.
"""

from typing import List, Dict, Optional, Tuple
from datetime import datetime, date, time, timedelta
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ValidationError

from apps.staff.models import StaffProfile, WorkingHours, Specialization
from apps.authentication.models import SalonUser


class StaffAvailabilityService:
    """Service for managing staff availability and scheduling."""
    
    @staticmethod
    def get_available_staff_for_date(
        target_date: date,
        specialization: Optional[Specialization] = None
    ) -> List[StaffProfile]:
        """
        Get all staff members available on a specific date.
        
        Args:
            target_date: The date to check availability for
            specialization: Optional specialization filter
            
        Returns:
            List of StaffProfile objects available on the target date
        """
        day_of_week = target_date.isoweekday()  # 1=Monday, 7=Sunday
        
        # Start with all active staff
        staff_profiles = StaffProfile.objects.filter(
            user__is_active_staff=True,
            is_accepting_new_clients=True
        )  # type: ignore
        
        # Filter by specialization if provided
        if specialization:
            staff_profiles = staff_profiles.filter(specializations=specialization)  # type: ignore
        
        # Filter by availability on the specific day
        available_staff = []
        for staff in staff_profiles:
            if staff.is_available_on_day(day_of_week):
                available_staff.append(staff)
        
        return available_staff
    
    @staticmethod
    def get_available_time_slots(
        staff_profile: StaffProfile,
        target_date: date,
        service_duration: int = 60  # in minutes
    ) -> List[Tuple[time, time]]:
        """
        Get available time slots for a staff member on a specific date.
        
        Args:
            staff_profile: The staff member to check
            target_date: The date to check availability for
            service_duration: Duration of the service in minutes
            
        Returns:
            List of (start_time, end_time) tuples representing available slots
        """
        day_of_week = target_date.isoweekday()
        working_hours = staff_profile.get_working_hours_for_day(day_of_week)
        
        if not working_hours or not working_hours.is_available:
            return []  # Not available on this day
        
        # Calculate available time slots
        slots = []
        current_time = datetime.combine(target_date, working_hours.start_time)
        end_datetime = datetime.combine(target_date, working_hours.end_time)
        
        while current_time + timedelta(minutes=service_duration) <= end_datetime:
            slot_start = current_time.time()
            slot_end = (current_time + timedelta(minutes=service_duration)).time()
            
            # Check if this slot conflicts with break time
            if working_hours.break_start_time and working_hours.break_end_time:
                break_start = working_hours.break_start_time
                break_end = working_hours.break_end_time
                
                # Check if slot overlaps with break
                if not (slot_end <= break_start or slot_start >= break_end):
                    current_time += timedelta(minutes=service_duration)
                    continue
            
            slots.append((slot_start, slot_end))
            current_time += timedelta(minutes=service_duration)
        
        return slots
    
    @staticmethod
    def find_staff_with_availability(
        target_datetime: datetime,
        duration: int,
        specialization: Optional[Specialization] = None
    ) -> List[StaffProfile]:
        """
        Find staff members available for a specific time slot.
        
        Args:
            target_datetime: The datetime to check availability for
            duration: Duration of the service in minutes
            specialization: Optional specialization filter
            
        Returns:
            List of StaffProfile objects available for the time slot
        """
        target_date = target_datetime.date()
        day_of_week = target_datetime.isoweekday()
        end_datetime = target_datetime + timedelta(minutes=duration)
        
        # Get available staff for the date
        available_staff = StaffAvailabilityService.get_available_staff_for_date(
            target_date, specialization
        )
        
        # Filter by time slot availability
        suitable_staff = []
        for staff in available_staff:
            if not staff.has_schedule_conflict(target_datetime, end_datetime):
                suitable_staff.append(staff)
        
        return suitable_staff


class WorkingHoursService:
    """Service for managing staff working hours."""
    
    @staticmethod
    def create_working_hours(
        staff_profile: StaffProfile,
        day_of_week: int,
        start_time: time,
        end_time: time,
        is_available: bool = True,
        break_start_time: Optional[time] = None,
        break_end_time: Optional[time] = None
    ) -> WorkingHours:
        """
        Create working hours for a staff member.
        
        Args:
            staff_profile: The staff member
            day_of_week: Day of week (1=Monday, 7=Sunday)
            start_time: Start time for the day
            end_time: End time for the day
            is_available: Whether the staff is available on this day
            break_start_time: Optional break start time
            break_end_time: Optional break end time
            
        Returns:
            Created WorkingHours object
            
        Raises:
            ValidationError: If validation fails
        """
        # Create working hours object
        working_hours = WorkingHours(
            staff_profile=staff_profile,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            is_available=is_available,
            break_start_time=break_start_time,
            break_end_time=break_end_time
        )
        
        # Validate and save
        working_hours.full_clean()
        working_hours.save()
        
        return working_hours
    
    @staticmethod
    def update_working_hours(
        working_hours: WorkingHours,
        **kwargs
    ) -> WorkingHours:
        """
        Update working hours for a staff member.
        
        Args:
            working_hours: The working hours object to update
            **kwargs: Fields to update
            
        Returns:
            Updated WorkingHours object
            
        Raises:
            ValidationError: If validation fails
        """
        # Update fields
        for field, value in kwargs.items():
            setattr(working_hours, field, value)
        
        # Validate and save
        working_hours.full_clean()
        working_hours.save()
        
        return working_hours
    
    @staticmethod
    def get_weekly_schedule(staff_profile: StaffProfile) -> Dict[int, WorkingHours]:
        """
        Get the complete weekly schedule for a staff member.
        
        Args:
            staff_profile: The staff member
            
        Returns:
            Dictionary mapping day of week to WorkingHours objects
        """
        schedule = {}
        for day in range(1, 8):  # 1=Monday to 7=Sunday
            try:
                working_hours = staff_profile.working_hours.get(day_of_week=day)  # type: ignore
                schedule[day] = working_hours
            except WorkingHours.DoesNotExist:  # type: ignore
                schedule[day] = None
        
        return schedule


class StaffPerformanceService:
    """Service for tracking staff performance metrics."""
    
    @staticmethod
    def get_staff_utilization_rate(
        staff_profile: StaffProfile,
        start_date: date,
        end_date: date
    ) -> float:
        """
        Calculate staff utilization rate for a date range.
        
        Args:
            staff_profile: The staff member
            start_date: Start date for calculation
            end_date: End date for calculation
            
        Returns:
            Utilization rate as a percentage (0-100)
        """
        # This would typically integrate with appointment data
        # For now, we'll return a placeholder based on availability
        available_days = staff_profile.get_available_days()
        total_possible_days = 7
        if total_possible_days > 0:
            return (len(available_days) / total_possible_days) * 100
        return 0.0
    
    @staticmethod
    def get_staff_specialization_distribution() -> Dict[str, int]:
        """
        Get distribution of staff by specialization.
        
        Returns:
            Dictionary mapping specialization names to staff count
        """
        distribution = {}
        specializations = Specialization.objects.filter(is_active=True)  # type: ignore
        
        for specialization in specializations:
            count = specialization.staff_profiles.filter(
                user__is_active_staff=True
            ).count()  # type: ignore
            distribution[specialization.name] = count
        
        return distribution


# Convenience functions for common operations
def get_available_staff(
    target_date: date,
    specialization: Optional[Specialization] = None
) -> List[StaffProfile]:
    """Convenience function to get available staff for a date."""
    return StaffAvailabilityService.get_available_staff_for_date(target_date, specialization)


def get_available_time_slots(
    staff_profile: StaffProfile,
    target_date: date,
    service_duration: int = 60
) -> List[Tuple[time, time]]:
    """Convenience function to get available time slots for a staff member."""
    return StaffAvailabilityService.get_available_time_slots(
        staff_profile, target_date, service_duration
    )


def find_available_staff_for_time(
    target_datetime: datetime,
    duration: int,
    specialization: Optional[Specialization] = None
) -> List[StaffProfile]:
    """Convenience function to find staff available for a specific time slot."""
    return StaffAvailabilityService.find_staff_with_availability(
        target_datetime, duration, specialization
    )
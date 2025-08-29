"""
Staff models for Mario Beauty Salon Management System.
Provides staff profile management and specialization tracking.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

from apps.core.models import BaseModel, SalonModelMixin
from apps.authentication.models import SalonUser


class Specialization(BaseModel, SalonModelMixin):
    """
    Specialization model for tracking staff specialties.
    Allows for structured management of staff capabilities.
    """
    
    class SpecializationType(models.TextChoices):
        """
        Define specialization types for nail salon services.
        """
        NAIL_CARE = 'nail_care', _('Nail Care')
        SKIN_CARE = 'skin_care', _('Skin Care')
        FOOT_CARE = 'foot_care', _('Foot Care')
        BEAUTY_TREATMENT = 'beauty_treatment', _('Beauty Treatment')
    
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Specialization name (e.g., 'Manicure', 'Pedicure', 'Facial')"
    )
    
    specialization_type = models.CharField(
        max_length=20,
        choices=SpecializationType.choices,
        default=SpecializationType.NAIL_CARE,
        help_text="Type of specialization"
    )
    
    description = models.TextField(
        blank=True,
        help_text="Detailed description of the specialization"
    )
    
    certification_required = models.BooleanField(
        default=False,  # type: ignore
        help_text="Whether this specialization requires certification"
    )
    
    is_active = models.BooleanField(
        default=True,  # type: ignore
        help_text="Whether this specialization is currently offered"
    )
    
    class Meta(BaseModel.Meta):  # type: ignore
        db_table = 'staff_specializations'
        verbose_name = _('Specialization')
        verbose_name_plural = _('Specializations')
        ordering = ['specialization_type', 'name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['specialization_type']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self) -> str:  # type: ignore
        return f"{self.name} ({self.get_specialization_type_display()})"  # type: ignore


class StaffProfile(BaseModel, SalonModelMixin):
    """
    Extended staff profile information.
    Complements SalonUser with additional staff-specific details.
    """
    
    class CertificationLevel(models.TextChoices):
        """
        Define certification levels for staff.
        """
        TRAINEE = 'trainee', _('Trainee')
        JUNIOR = 'junior', _('Junior')
        SENIOR = 'senior', _('Senior')
        MASTER = 'master', _('Master')
        EXPERT = 'expert', _('Expert')
    
    user = models.OneToOneField(
        SalonUser,
        on_delete=models.CASCADE,
        related_name='staff_profile',
        help_text="Reference to the salon user"
    )
    
    specializations = models.ManyToManyField(
        Specialization,
        blank=True,
        related_name='staff_profiles',
        help_text="Staff member's specializations"
    )
    
    certification_level = models.CharField(
        max_length=20,
        choices=CertificationLevel.choices,
        default=CertificationLevel.JUNIOR,
        help_text="Overall certification level of the staff member"
    )
    
    years_of_experience = models.PositiveIntegerField(
        default=0,  # type: ignore
        validators=[MaxValueValidator(50)],
        help_text="Years of professional experience"
    )
    
    hourly_rate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Hourly rate for services (optional)"
    )
    
    max_clients_per_day = models.PositiveIntegerField(
        default=8,  # type: ignore
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Maximum number of clients per day"
    )
    
    languages_spoken = models.TextField(
        blank=True,
        help_text="Comma-separated list of languages spoken (e.g., 'English, Spanish, Polish')"
    )
    
    availability_notes = models.TextField(
        blank=True,
        help_text="Special notes about staff availability or working preferences"
    )
    
    is_accepting_new_clients = models.BooleanField(
        default=True,  # type: ignore
        help_text="Whether this staff member is accepting new clients"
    )
    
    emergency_contact_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Emergency contact person name"
    )
    
    emergency_contact_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Emergency contact phone number"
    )
    
    class Meta(BaseModel.Meta):  # type: ignore
        db_table = 'staff_profiles'
        verbose_name = _('Staff Profile')
        verbose_name_plural = _('Staff Profiles')
        indexes = [
            models.Index(fields=['certification_level']),
            models.Index(fields=['years_of_experience']),
            models.Index(fields=['is_accepting_new_clients']),
        ]
    
    def __str__(self) -> str:  # type: ignore
        return f"{self.user.get_full_name()} - {self.get_certification_level_display()}"  # type: ignore
    
    @property
    def specialization_names(self):
        """Return list of specialization names."""
        return [spec.name for spec in self.specializations.filter(is_active=True)]  # type: ignore
    
    @property
    def primary_specialization(self):
        """Return the first active specialization."""
        return self.specializations.filter(is_active=True).first()  # type: ignore
    
    def get_languages_list(self):
        """Return languages as a list."""
        if not self.languages_spoken:
            return []
        return [lang.strip() for lang in str(self.languages_spoken).split(',')]
    
    def add_specialization(self, specialization):
        """Add a specialization to this staff member."""
        if isinstance(specialization, str):
            # If string is passed, try to find the specialization by name
            try:
                specialization = Specialization.objects.get(name=specialization, is_active=True)  # type: ignore
            except Specialization.DoesNotExist:  # type: ignore
                raise ValidationError(f"Specialization '{specialization}' not found or inactive")
        
        self.specializations.add(specialization)  # type: ignore
    
    def remove_specialization(self, specialization):
        """Remove a specialization from this staff member."""
        if isinstance(specialization, str):
            # If string is passed, try to find the specialization by name
            try:
                specialization = Specialization.objects.get(name=specialization)  # type: ignore
            except Specialization.DoesNotExist:  # type: ignore
                return  # Silently ignore if not found
        
        self.specializations.remove(specialization)  # type: ignore
    
    def can_perform_service(self, service):
        """Check if staff member can perform a specific service based on specializations."""
        # This will be expanded when service-specialization relationships are defined
        service_specializations = getattr(service, 'required_specializations', [])
        if not service_specializations:
            return True  # No specific specializations required
        
        staff_spec_names = set(self.specialization_names)
        required_spec_names = set(spec.name for spec in service_specializations)
        
        return bool(staff_spec_names.intersection(required_spec_names))
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Ensure user is staff
        if self.user and not self.user.is_active_staff:  # type: ignore
            raise ValidationError("User must be active staff to have a staff profile")
        
        # Validate hourly rate if commission rate is set
        if self.hourly_rate and self.user and self.user.commission_rate:  # type: ignore
            # Both hourly rate and commission rate shouldn't typically be set
            pass  # This is just a note - both can coexist for different services
    
    def save(self, *args, **kwargs):
        """Override save to perform additional validation."""
        self.clean()
        super().save(*args, **kwargs)
    
    def is_available_on_day(self, day_of_week):
        """Check if staff member is available on a specific day of week."""
        try:
            working_hours = self.working_hours.get(day_of_week=day_of_week)  # type: ignore
            return working_hours.is_available
        except WorkingHours.DoesNotExist:  # type: ignore
            return False
    
    def get_working_hours_for_day(self, day_of_week):
        """Get working hours for a specific day."""
        try:
            return self.working_hours.get(day_of_week=day_of_week)  # type: ignore
        except WorkingHours.DoesNotExist:  # type: ignore
            return None
    
    def get_available_days(self):
        """Get list of days when staff member is available."""
        return self.working_hours.filter(is_available=True).values_list('day_of_week', flat=True)  # type: ignore
    
    def get_total_weekly_hours(self):
        """Calculate total working hours per week."""
        total_minutes = 0
        for working_hours in self.working_hours.filter(is_available=True):  # type: ignore
            total_minutes += working_hours.duration_minutes
        return total_minutes / 60  # Return hours as float
    
    def has_schedule_conflict(self, start_datetime, end_datetime):
        """Check if there's a schedule conflict for given time period."""
        # Get day of week (1=Monday, 7=Sunday)
        day_of_week = start_datetime.isoweekday()
        
        # Check if staff is available on this day
        if not self.is_available_on_day(day_of_week):
            return True  # Conflict: not available on this day
        
        working_hours = self.get_working_hours_for_day(day_of_week)
        if not working_hours:
            return True  # Conflict: no working hours defined
        
        # Extract time components
        start_time = start_datetime.time()
        end_time = end_datetime.time()
        
        # Check if requested time is within working hours
        if start_time < working_hours.start_time or end_time > working_hours.end_time:
            return True  # Conflict: outside working hours
        
        # Check if requested time conflicts with break time
        if working_hours.break_start_time and working_hours.break_end_time:
            if not (end_time <= working_hours.break_start_time or start_time >= working_hours.break_end_time):
                return True  # Conflict: overlaps with break time
        
        return False  # No conflict


class WorkingHours(BaseModel, SalonModelMixin):
    """
    Working hours model for staff scheduling.
    Defines when staff members are available to work.
    """
    
    class DayOfWeek(models.IntegerChoices):
        """
        Define days of the week.
        """
        MONDAY = 1, _('Monday')
        TUESDAY = 2, _('Tuesday')
        WEDNESDAY = 3, _('Wednesday')
        THURSDAY = 4, _('Thursday')
        FRIDAY = 5, _('Friday')
        SATURDAY = 6, _('Saturday')
        SUNDAY = 7, _('Sunday')
    
    staff_profile = models.ForeignKey(
        StaffProfile,
        on_delete=models.CASCADE,
        related_name='working_hours',
        help_text="Staff profile these working hours belong to"
    )
    
    day_of_week = models.IntegerField(
        choices=DayOfWeek.choices,
        help_text="Day of the week (1=Monday, 7=Sunday)"
    )
    
    start_time = models.TimeField(
        help_text="Start time for this day"
    )
    
    end_time = models.TimeField(
        help_text="End time for this day"
    )
    
    is_available = models.BooleanField(
        default=True,  # type: ignore
        help_text="Whether the staff member is available on this day"
    )
    
    break_start_time = models.TimeField(
        null=True,
        blank=True,
        help_text="Break start time (optional)"
    )
    
    break_end_time = models.TimeField(
        null=True,
        blank=True,
        help_text="Break end time (optional)"
    )
    
    class Meta(BaseModel.Meta):  # type: ignore
        db_table = 'staff_working_hours'
        verbose_name = _('Working Hours')
        verbose_name_plural = _('Working Hours')
        ordering = ['staff_profile', 'day_of_week']
        indexes = [
            models.Index(fields=['staff_profile', 'day_of_week']),
            models.Index(fields=['day_of_week']),
            models.Index(fields=['is_available']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['staff_profile', 'day_of_week'],
                name='unique_staff_day_working_hours'
            ),
        ]
    
    def __str__(self) -> str:  # type: ignore
        if self.is_available:
            time_str = f"{self.start_time} - {self.end_time}"
            if self.break_start_time and self.break_end_time:
                time_str += f" (Break: {self.break_start_time} - {self.break_end_time})"
            return f"{self.staff_profile.user.get_full_name()} - {self.get_day_of_week_display()}: {time_str}"  # type: ignore
        else:
            return f"{self.staff_profile.user.get_full_name()} - {self.get_day_of_week_display()}: Not Available"  # type: ignore
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        if self.is_available:
            # Validate start time is before end time
            if self.start_time and self.end_time and self.start_time >= self.end_time:
                raise ValidationError("Start time must be before end time")
            
            # Validate break times if provided
            if self.break_start_time and self.break_end_time:
                if self.break_start_time >= self.break_end_time:
                    raise ValidationError("Break start time must be before break end time")
                
                # Validate break times are within working hours
                if (self.break_start_time < self.start_time or 
                    self.break_end_time > self.end_time):
                    raise ValidationError("Break times must be within working hours")
    
    def save(self, *args, **kwargs):
        """Override save to perform additional validation."""
        self.clean()
        super().save(*args, **kwargs)
    
    @property
    def duration_minutes(self):
        """Calculate working duration in minutes."""
        if not self.is_available or not self.start_time or not self.end_time:
            return 0
        
        total_minutes = (self.end_time.hour * 60 + self.end_time.minute) - (self.start_time.hour * 60 + self.start_time.minute)  # type: ignore
        
        # Subtract break time if present
        if self.break_start_time and self.break_end_time:
            break_minutes = (self.break_end_time.hour * 60 + self.break_end_time.minute) - (self.break_start_time.hour * 60 + self.break_start_time.minute)  # type: ignore
            total_minutes -= break_minutes
        
        return max(0, total_minutes)
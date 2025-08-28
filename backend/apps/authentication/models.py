"""
Authentication models for Mario Beauty Salon Management System.
Provides custom user model with role-based permissions for salon operations.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel, SalonModelMixin


class SalonUser(AbstractUser, TimeStampedModel, SalonModelMixin):
    """
    Custom user model for salon staff and administrators.
    Extends Django's AbstractUser with salon-specific fields and role management.
    """
    
    class UserRole(models.TextChoices):
        """
        Define user roles with specific permissions for salon operations.
        """
        OWNER = 'owner', _('Owner')
        MANAGER = 'manager', _('Manager')
        STYLIST = 'stylist', _('Stylist')
        RECEPTIONIST = 'receptionist', _('Receptionist')
    
    # Additional user fields
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STYLIST,
        help_text="User's role in the salon determining their permissions"
    )
    
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="Contact phone number"
    )
    
    employee_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        help_text="Unique employee identifier"
    )
    
    is_active_staff = models.BooleanField(
        default=True,  # type: ignore
        help_text="Indicates if the user is currently active as staff member"
    )
    
    hire_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date when the employee was hired"
    )
    
    commission_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=40.00,
        help_text="Commission percentage for services (e.g., 40.00 for 40%)"
    )
    
    specialties = models.TextField(
        blank=True,
        help_text="Comma-separated list of specialties (e.g., manicure, pedicure, facial)"
    )
    
    bio = models.TextField(
        blank=True,
        help_text="Professional biography for client-facing profiles"
    )
    
    profile_image = models.ImageField(
        upload_to='staff_profiles/',
        blank=True,
        null=True,
        help_text="Profile photo for staff directory"
    )

    class Meta:  # type: ignore
        db_table = 'salon_users'
        verbose_name = _('Salon User')
        verbose_name_plural = _('Salon Users')
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['employee_id']),
            models.Index(fields=['is_active_staff']),
        ]

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"  # type: ignore

    def get_full_name(self) -> str:
        """
        Return the user's full name with fallback to username.
        """
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else str(self.username)

    @property
    def is_owner(self):
        """Check if user has owner role."""
        return self.role == self.UserRole.OWNER

    @property
    def is_manager(self):
        """Check if user has manager role."""
        return self.role == self.UserRole.MANAGER

    @property
    def is_stylist(self):
        """Check if user has stylist role."""
        return self.role == self.UserRole.STYLIST

    @property
    def is_receptionist(self):
        """Check if user has receptionist role."""
        return self.role == self.UserRole.RECEPTIONIST

    @property
    def can_manage_salon(self):
        """Check if user can manage salon operations."""
        return self.role in [self.UserRole.OWNER, self.UserRole.MANAGER]

    @property
    def can_manage_staff(self):
        """Check if user can manage staff."""
        return self.role == self.UserRole.OWNER

    @property
    def can_view_reports(self):
        """Check if user can view business reports."""
        return self.role in [self.UserRole.OWNER, self.UserRole.MANAGER]

    @property
    def can_manage_inventory(self):
        """Check if user can manage inventory."""
        return self.role in [self.UserRole.OWNER, self.UserRole.MANAGER]

    @property
    def can_process_payments(self):
        """Check if user can process payments."""
        return self.role in [
            self.UserRole.OWNER, 
            self.UserRole.MANAGER, 
            self.UserRole.RECEPTIONIST
        ]

    def get_specialties_list(self):
        """
        Return specialties as a list.
        """
        if not self.specialties:
            return []
        return [specialty.strip() for specialty in str(self.specialties).split(',')]

    def add_specialty(self, specialty):
        """
        Add a new specialty to the user's specialties.
        """
        specialties = self.get_specialties_list()
        if specialty not in specialties:
            specialties.append(specialty)
            self.specialties = ', '.join(specialties)
            self.save()

    def remove_specialty(self, specialty):
        """
        Remove a specialty from the user's specialties.
        """
        specialties = self.get_specialties_list()
        if specialty in specialties:
            specialties.remove(specialty)
            self.specialties = ', '.join(specialties)
            self.save()


class UserProfile(TimeStampedModel, SalonModelMixin):
    """
    Extended profile information for salon users.
    Stores additional non-authentication related information.
    """
    user = models.OneToOneField(
        SalonUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="Date of birth for age verification and birthday reminders"
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
    
    address = models.TextField(
        blank=True,
        help_text="Home address"
    )
    
    notes = models.TextField(
        blank=True,
        help_text="Internal notes about the staff member"
    )
    
    timezone = models.CharField(
        max_length=50,
        default='Europe/Warsaw',
        help_text="User's timezone for scheduling"
    )

    class Meta:  # type: ignore
        db_table = 'salon_user_profiles'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return f"Profile for {self.user.get_full_name()}"  # type: ignore
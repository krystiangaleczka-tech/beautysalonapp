"""
Client models for Mario Beauty Salon MVP System.
Provides basic client management for appointment booking.
"""

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.core.models import BaseModel


class Client(BaseModel):
    """
    Basic client model for MVP implementation.
    Stores essential client information for appointment booking.
    """
    
    # Basic Information
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First Name'),
        help_text=_('Client first name')
    )
    
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last Name'),
        help_text=_('Client last name')
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email Address'),
        help_text=_('Client email for notifications')
    )
    
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_('Phone number must be entered in format: "+999999999". Up to 15 digits allowed.')
        )],
        verbose_name=_('Phone Number'),
        help_text=_('Client phone number for SMS notifications')
    )
    
    # Basic Preferences
    allergies = models.TextField(
        blank=True,
        verbose_name=_('Allergies'),
        help_text=_('Any allergies or sensitivities to products')
    )
    
    notes = models.TextField(
        blank=True,
        verbose_name=_('Notes'),
        help_text=_('Additional notes about the client')
    )
    
    class Meta:
        db_table = 'clients'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['email']),
        ]
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self):
        """Return full name of the client."""
        return f'{self.first_name} {self.last_name}'
    
    def clean(self):
        """Validate client data."""
        super().clean()
        
        # Ensure at least one contact method is provided
        if not self.email and not self.phone:
            raise ValidationError(
                _('At least one contact method (email or phone) must be provided.')
            )

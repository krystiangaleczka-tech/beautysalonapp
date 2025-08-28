"""
Client models for Mario Beauty Salon Management System.
Provides comprehensive client tracking, preferences, and business analytics.
"""

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.authentication.models import SalonUser


class Client(BaseModel):
    """
    Client model with comprehensive tracking and preferences.
    Extends BaseModel to include timestamp and soft delete functionality.
    """
    
    # User relationship
    user = models.OneToOneField(
        SalonUser, 
        on_delete=models.CASCADE,
        related_name='client_profile',
        help_text="Associated user account for the client"
    )
    
    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be in format: '+999999999'. Up to 15 digits allowed.")
    )
    
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True,
        help_text="Primary contact phone number"
    )
    
    emergency_contact_name = models.CharField(
        max_length=100, 
        blank=True,
        help_text="Emergency contact person name"
    )
    
    emergency_contact_phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True,
        help_text="Emergency contact phone number"
    )
    
    # Client Preferences and Health Information
    service_preferences = models.JSONField(
        default=dict,
        blank=True,
        help_text="Client service preferences, favorite staff, and booking patterns"
    )
    
    allergies = models.TextField(
        blank=True,
        help_text="Known allergies and sensitivities for service safety"
    )
    
    skin_type = models.CharField(
        max_length=50, 
        blank=True,
        choices=[
            ('normal', _('Normal')),
            ('dry', _('Dry')),
            ('oily', _('Oily')),
            ('combination', _('Combination')),
            ('sensitive', _('Sensitive')),
            ('mature', _('Mature')),
            ('acne_prone', _('Acne-Prone')),
        ],
        help_text="Skin type for facial and skincare services"
    )
    
    hair_type = models.CharField(
        max_length=50, 
        blank=True,
        choices=[
            ('straight', _('Straight')),
            ('wavy', _('Wavy')),
            ('curly', _('Curly')),
            ('coily', _('Coily')),
            ('fine', _('Fine')),
            ('thick', _('Thick')),
            ('damaged', _('Damaged')),
            ('color_treated', _('Color-Treated')),
        ],
        help_text="Hair type and condition for hair services"
    )
    
    # Business Tracking Fields
    total_visits = models.PositiveIntegerField(
        default=0,  # type: ignore
        help_text="Total number of completed appointments"
    )
    
    total_spent = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        help_text="Total amount spent on services"
    )
    
    last_visit = models.DateTimeField(
        null=True, 
        blank=True,
        help_text="Date and time of last completed appointment"
    )
    
    loyalty_points = models.PositiveIntegerField(
        default=0,  # type: ignore
        help_text="Accumulated loyalty points for rewards"
    )
    
    # Communication Preferences
    CONTACT_METHOD_CHOICES = [
        ('email', _('Email')),
        ('sms', _('SMS')),
        ('phone', _('Phone Call')),
        ('app', _('App Notification')),
    ]
    
    preferred_contact_method = models.CharField(
        max_length=20,
        choices=CONTACT_METHOD_CHOICES,
        default='email',
        help_text="Preferred method for appointment reminders and communications"
    )
    
    marketing_consent = models.BooleanField(
        default=False,  # type: ignore
        help_text="Consent to receive marketing communications"
    )
    
    reminder_consent = models.BooleanField(
        default=True,  # type: ignore
        help_text="Consent to receive appointment reminders"
    )
    
    # Additional Notes
    notes = models.TextField(
        blank=True,
        help_text="Internal notes about the client for staff reference"
    )

    class Meta:  # type: ignore
        db_table = 'clients'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['last_visit']),
            models.Index(fields=['total_visits']),
            models.Index(fields=['total_spent']),
        ]
        
    def __str__(self):
        """String representation of the client."""
        return f"{self.user.get_full_name()} - {self.phone_number or self.user.email}"  # type: ignore
    
    def get_preferences_summary(self):
        """
        Return formatted summary of client preferences.
        
        Returns:
            dict: Summary of client preferences and important information
        """
        return {
            'favorite_services': self.service_preferences.get('favorite_services', []),  # type: ignore
            'preferred_staff': self.service_preferences.get('preferred_staff', []),  # type: ignore
            'preferred_times': self.service_preferences.get('preferred_times', []),  # type: ignore
            'skin_type': self.skin_type or 'Not specified',
            'hair_type': self.hair_type or 'Not specified',
            'allergies': self.allergies or 'None noted',
            'special_notes': self.notes or 'None'
        }
    
    def add_loyalty_points(self, points):
        """
        Add loyalty points and save the client record.
        
        Args:
            points (int): Number of points to add
        """
        if points > 0:
            self.loyalty_points += points
            self.save(update_fields=['loyalty_points', 'updated_at'])
    
    def redeem_loyalty_points(self, points):
        """
        Redeem loyalty points if sufficient balance exists.
        
        Args:
            points (int): Number of points to redeem
            
        Returns:
            bool: True if redemption successful, False otherwise
        """
        if points > 0 and self.loyalty_points >= points:
            self.loyalty_points -= points
            self.save(update_fields=['loyalty_points', 'updated_at'])
            return True
        return False
    
    def update_visit_stats(self, amount_spent):
        """
        Update visit statistics after a completed appointment.
        
        Args:
            amount_spent (Decimal): Amount spent on the appointment
        """
        from django.utils import timezone
        
        self.total_visits += 1  # type: ignore
        self.total_spent += amount_spent
        self.last_visit = timezone.now()
        
        # Calculate loyalty points (1 point per euro spent)
        loyalty_earned = int(amount_spent)
        self.loyalty_points += loyalty_earned  # type: ignore
        
        self.save(update_fields=[
            'total_visits', 
            'total_spent', 
            'last_visit', 
            'loyalty_points',
            'updated_at'
        ])
    
    def get_visit_frequency(self):
        """
        Calculate average days between visits.
        
        Returns:
            float: Average days between visits or None if insufficient data
        """
        if self.total_visits < 2 or not self.last_visit:
            return None
            
        from django.utils import timezone
        
        # Calculate based on time since first visit vs number of visits
        account_age_days = (timezone.now() - self.created_at).days  # type: ignore
        if account_age_days > 0:
            return account_age_days / max(self.total_visits - 1, 1)  # type: ignore
        return None
    
    def is_vip_client(self):
        """
        Determine if client qualifies as VIP based on spending and visits.
        
        Returns:
            bool: True if client is VIP status
        """
        # VIP criteria: 10+ visits OR 500+ euros spent OR 1000+ loyalty points
        return (
            self.total_visits >= 10 or 
            self.total_spent >= 500 or 
            self.loyalty_points >= 1000
        )
    
    def get_client_tier(self):
        """
        Get client tier based on engagement and spending.
        
        Returns:
            str: Client tier (bronze, silver, gold, platinum)
        """
        if self.total_spent >= 1000 and self.total_visits >= 20:
            return 'platinum'
        elif self.total_spent >= 500 and self.total_visits >= 10:
            return 'gold'
        elif self.total_spent >= 200 and self.total_visits >= 5:
            return 'silver'
        else:
            return 'bronze'
    
    def update_preferences(self, preference_key, value):
        """
        Update a specific preference in the service_preferences JSON field.
        
        Args:
            preference_key (str): The preference key to update
            value: The value to set
        """
        if not self.service_preferences:
            self.service_preferences = {}
            
        self.service_preferences[preference_key] = value  # type: ignore
        self.save(update_fields=['service_preferences', 'updated_at'])
    
    def get_communication_preferences(self):
        """
        Get client's communication preferences for notifications.
        
        Returns:
            dict: Communication preferences and consent status
        """
        return {
            'preferred_method': self.preferred_contact_method,
            'marketing_consent': self.marketing_consent,
            'reminder_consent': self.reminder_consent,
            'contact_info': {
                'email': self.user.email,  # type: ignore
                'phone': self.phone_number,
            }
        }
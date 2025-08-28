"""
Client models for Mario Beauty Salon Management System.
Provides comprehensive client tracking, preferences, and business analytics.
"""

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models import Q, Count, Avg, Sum
from django.core.exceptions import ValidationError

from apps.core.models import BaseModel
from apps.authentication.models import SalonUser


class ClientQuerySet(models.QuerySet):
    """
    Custom QuerySet for Client model with advanced search and filtering methods.
    """
    
    def search(self, query):
        """
        Full-text search across client fields.
        
        Args:
            query (str): Search term to find in client data
            
        Returns:
            QuerySet: Filtered clients matching the search query
        """
        if not query:
            return self
            
        return self.filter(
            Q(user__first_name__icontains=query) |  # type: ignore
            Q(user__last_name__icontains=query) |
            Q(user__email__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(notes__icontains=query)
        )
    
    def by_tier(self, tier):
        """
        Filter clients by their calculated tier status.
        
        Args:
            tier (str): Client tier ('bronze', 'silver', 'gold', 'platinum')
            
        Returns:
            QuerySet: Clients in the specified tier
        """
        if tier == 'platinum':
            return self.filter(total_spent__gte=1000, total_visits__gte=20)
        elif tier == 'gold':
            return self.filter(total_spent__gte=500, total_visits__gte=10)
        elif tier == 'silver':
            return self.filter(total_spent__gte=200, total_visits__gte=5)
        else:  # bronze
            return self.filter(
                Q(total_spent__lt=200) | Q(total_visits__lt=5)  # type: ignore
            )
    
    def vip_clients(self):
        """
        Get VIP clients based on multiple criteria.
        
        Returns:
            QuerySet: Clients who qualify as VIP
        """
        return self.filter(
            Q(total_visits__gte=10) |  # type: ignore
            Q(total_spent__gte=500) |
            Q(loyalty_points__gte=1000)
        )
    
    def active_clients(self, days=180):
        """
        Get clients who visited within specified days.
        
        Args:
            days (int): Number of days to look back (default: 180)
            
        Returns:
            QuerySet: Recently active clients
        """
        from django.utils import timezone
        from datetime import timedelta
        
        cutoff_date = timezone.now() - timedelta(days=days)
        return self.filter(last_visit__gte=cutoff_date)
    
    def inactive_clients(self, days=180):
        """
        Get clients who haven't visited within specified days.
        
        Args:
            days (int): Number of days to look back (default: 180)
            
        Returns:
            QuerySet: Inactive clients who might need re-engagement
        """
        from django.utils import timezone
        from datetime import timedelta
        
        cutoff_date = timezone.now() - timedelta(days=days)
        return self.filter(
            Q(last_visit__lt=cutoff_date) | Q(last_visit__isnull=True)  # type: ignore
        )
    
    def by_contact_method(self, method):
        """
        Filter clients by their preferred contact method.
        
        Args:
            method (str): Contact method ('email', 'sms', 'phone', 'app')
            
        Returns:
            QuerySet: Clients preferring the specified contact method
        """
        return self.filter(preferred_contact_method=method)
    
    def with_marketing_consent(self):
        """
        Get clients who have consented to marketing communications.
        
        Returns:
            QuerySet: Clients who can receive marketing messages
        """
        return self.filter(marketing_consent=True)
    
    def with_allergies(self):
        """
        Get clients who have recorded allergies.
        
        Returns:
            QuerySet: Clients with allergy information
        """
        return self.exclude(Q(allergies='') | Q(allergies__isnull=True))
    
    def new_clients(self, days=30):
        """
        Get clients who joined within specified days.
        
        Args:
            days (int): Number of days to look back (default: 30)
            
        Returns:
            QuerySet: Recently registered clients
        """
        from django.utils import timezone
        from datetime import timedelta
        
        cutoff_date = timezone.now() - timedelta(days=days)
        return self.filter(created_at__gte=cutoff_date)


class ClientManager(models.Manager):
    """
    Custom manager for Client model with business intelligence methods.
    """
    
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db).select_related('user')
    
    def search(self, query):
        return self.get_queryset().search(query)
    
    def by_tier(self, tier):
        return self.get_queryset().by_tier(tier)
    
    def vip_clients(self):
        return self.get_queryset().vip_clients()
    
    def active_clients(self, days=180):
        return self.get_queryset().active_clients(days)
    
    def inactive_clients(self, days=180):
        return self.get_queryset().inactive_clients(days)
    
    def get_analytics(self):
        """
        Get comprehensive client analytics.
        
        Returns:
            dict: Analytics data including counts, averages, and trends
        """
        from django.utils import timezone
        from datetime import timedelta
        
        total_clients = self.count()
        
        # Recent activity
        thirty_days_ago = timezone.now() - timedelta(days=30)
        new_clients_month = self.filter(created_at__gte=thirty_days_ago).count()
        active_clients_month = self.filter(last_visit__gte=thirty_days_ago).count()
        
        # Financial metrics
        aggregates = self.aggregate(
            avg_visits=Avg('total_visits'),
            avg_spending=Avg('total_spent'),
            total_revenue=Sum('total_spent'),
            avg_loyalty_points=Avg('loyalty_points')
        )
        
        # Tier distribution
        tier_stats = {
            'platinum': self.by_tier('platinum').count(),
            'gold': self.by_tier('gold').count(),
            'silver': self.by_tier('silver').count(),
            'bronze': self.by_tier('bronze').count()
        }
        
        # Contact preferences
        contact_stats = self.values('preferred_contact_method').annotate(
            count=Count('id')
        ).order_by('-count')
        
        return {
            'total_clients': total_clients,
            'new_clients_this_month': new_clients_month,
            'active_clients_this_month': active_clients_month,
            'vip_clients': self.vip_clients().count(),
            'clients_with_marketing_consent': self.filter(marketing_consent=True).count(),
            'tier_distribution': tier_stats,
            'contact_method_preferences': list(contact_stats),
            'financial_metrics': {
                'average_visits_per_client': round(aggregates['avg_visits'] or 0, 2),
                'average_spending_per_client': round(float(aggregates['avg_spending'] or 0), 2),
                'total_client_revenue': float(aggregates['total_revenue'] or 0),
                'average_loyalty_points': round(aggregates['avg_loyalty_points'] or 0, 2)
            }
        }


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
    
    # Custom managers
    objects = ClientManager()
    objects_with_deleted = models.Manager()  # For accessing soft-deleted records

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
    
    def add_preferred_service(self, service_name):
        """
        Add a service to client's preferred services list.
        
        Args:
            service_name (str): Name of the preferred service
        """
        if not self.service_preferences:
            self.service_preferences = {}
        
        preferred_services = self.service_preferences.get('favorite_services', [])  # type: ignore
        if service_name not in preferred_services:
            preferred_services.append(service_name)
            self.service_preferences['favorite_services'] = preferred_services  # type: ignore
            self.save(update_fields=['service_preferences', 'updated_at'])
    
    def remove_preferred_service(self, service_name):
        """
        Remove a service from client's preferred services list.
        
        Args:
            service_name (str): Name of the service to remove
        """
        if not self.service_preferences:
            return
        
        preferred_services = self.service_preferences.get('favorite_services', [])  # type: ignore
        if service_name in preferred_services:
            preferred_services.remove(service_name)
            self.service_preferences['favorite_services'] = preferred_services  # type: ignore
            self.save(update_fields=['service_preferences', 'updated_at'])
    
    def add_preferred_staff(self, staff_id):
        """
        Add a staff member to client's preferred staff list.
        
        Args:
            staff_id (int): ID of the preferred staff member
        """
        if not self.service_preferences:
            self.service_preferences = {}
        
        preferred_staff = self.service_preferences.get('preferred_staff', [])  # type: ignore
        if staff_id not in preferred_staff:
            preferred_staff.append(staff_id)
            self.service_preferences['preferred_staff'] = preferred_staff  # type: ignore
            self.save(update_fields=['service_preferences', 'updated_at'])
    
    def remove_preferred_staff(self, staff_id):
        """
        Remove a staff member from client's preferred staff list.
        
        Args:
            staff_id (int): ID of the staff member to remove
        """
        if not self.service_preferences:
            return
        
        preferred_staff = self.service_preferences.get('preferred_staff', [])  # type: ignore
        if staff_id in preferred_staff:
            preferred_staff.remove(staff_id)
            self.service_preferences['preferred_staff'] = preferred_staff  # type: ignore
            self.save(update_fields=['service_preferences', 'updated_at'])
    
    def add_preferred_time(self, time_slot):
        """
        Add a time slot to client's preferred booking times.
        
        Args:
            time_slot (str): Preferred time slot (e.g., 'morning', '10:00-12:00', 'weekends')
        """
        if not self.service_preferences:
            self.service_preferences = {}
        
        preferred_times = self.service_preferences.get('preferred_times', [])  # type: ignore
        if time_slot not in preferred_times:
            preferred_times.append(time_slot)
            self.service_preferences['preferred_times'] = preferred_times  # type: ignore
            self.save(update_fields=['service_preferences', 'updated_at'])
    
    def get_preference_analysis(self):
        """
        Analyze client preferences and booking patterns.
        
        Returns:
            dict: Comprehensive preference analysis
        """
        analysis = {
            'basic_info': {
                'skin_type': self.skin_type or 'Not specified',
                'hair_type': self.hair_type or 'Not specified',
                'allergies': bool(self.allergies),
                'allergy_details': self.allergies or 'None recorded'
            },
            'service_preferences': {
                'favorite_services': self.service_preferences.get('favorite_services', []),  # type: ignore
                'preferred_staff': self.service_preferences.get('preferred_staff', []),  # type: ignore
                'preferred_times': self.service_preferences.get('preferred_times', []),  # type: ignore
                'special_requests': self.service_preferences.get('special_requests', [])  # type: ignore
            },
            'engagement_metrics': {
                'total_visits': self.total_visits,
                'total_spent': float(self.total_spent),  # type: ignore
                'loyalty_points': self.loyalty_points,
                'average_spend_per_visit': float(self.total_spent / max(self.total_visits, 1)),  # type: ignore
                'client_tier': self.get_client_tier(),
                'is_vip': self.is_vip_client(),
                'visit_frequency': self.get_visit_frequency()
            },
            'communication': {
                'preferred_method': self.preferred_contact_method,
                'marketing_consent': self.marketing_consent,
                'reminder_consent': self.reminder_consent,
                'contact_info': {
                    'email': self.user.email,  # type: ignore
                    'phone': self.phone_number,
                    'emergency_contact': self.emergency_contact_name
                }
            },
            'risk_factors': {
                'has_allergies': bool(self.allergies),
                'emergency_contact_missing': not bool(self.emergency_contact_name),
                'phone_missing': not bool(self.phone_number),
                'long_time_since_visit': (self._days_since_last_visit() or 0) > 90 if self.last_visit else True
            }
        }
        
        return analysis
    
    def _days_since_last_visit(self):
        """
        Calculate days since last visit.
        
        Returns:
            int: Number of days since last visit, or None if no visits
        """
        if not self.last_visit:
            return None
        
        from django.utils import timezone
        return (timezone.now() - self.last_visit).days  # type: ignore
    
    def get_recommendations(self):
        """
        Generate personalized recommendations for the client.
        
        Returns:
            dict: Recommendations for services, times, and engagement
        """
        recommendations = {
            'services': [],
            'engagement': [],
            'scheduling': [],
            'care_notes': []
        }
        
        # Service recommendations based on tier and preferences
        tier = self.get_client_tier()
        if tier in ['gold', 'platinum']:
            recommendations['services'].append('Consider premium service packages')
            recommendations['services'].append('Offer exclusive treatments')
        
        # Engagement recommendations
        days_since_visit = self._days_since_last_visit()
        if days_since_visit and days_since_visit > 60:
            recommendations['engagement'].append('Client may need re-engagement campaign')
            recommendations['engagement'].append('Consider special offer to encourage return')
        
        if self.loyalty_points > 500:
            recommendations['engagement'].append('Client has high loyalty points - suggest redemption options')
        
        # Scheduling recommendations
        preferred_times = self.service_preferences.get('preferred_times', [])  # type: ignore
        if preferred_times:
            recommendations['scheduling'].append(f"Client prefers: {', '.join(preferred_times)}")
        
        # Care notes
        if self.allergies:
            recommendations['care_notes'].append(f'ALLERGIES: {self.allergies}')
        
        if self.skin_type:
            recommendations['care_notes'].append(f'Skin type: {self.skin_type}')
        
        if self.hair_type:
            recommendations['care_notes'].append(f'Hair type: {self.hair_type}')
        
        return recommendations
    
    def validate_contact_info(self):
        """
        Validate client contact information with business rules.
        
        Returns:
            dict: Validation results with errors and warnings
        """
        validation_result = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        # Email validation (already handled by Django's EmailField)
        if not self.user.email:  # type: ignore
            validation_result['errors'].append('Email address is required')
            validation_result['is_valid'] = False
        
        # Phone number validation
        if not self.phone_number:
            validation_result['warnings'].append('Phone number missing - may limit communication options')
            validation_result['suggestions'].append('Request phone number for appointment reminders')
        else:
            # Check phone number format
            import re
            phone_pattern = r'^\+?1?\d{9,15}$'
            if not re.match(phone_pattern, str(self.phone_number)):
                validation_result['errors'].append('Phone number format is invalid')
                validation_result['is_valid'] = False
        
        # Emergency contact validation
        if not self.emergency_contact_name and not self.emergency_contact_phone:
            validation_result['warnings'].append('Emergency contact information missing')
            validation_result['suggestions'].append('Collect emergency contact for safety protocols')
        elif self.emergency_contact_name and not self.emergency_contact_phone:
            validation_result['warnings'].append('Emergency contact name provided but phone number missing')
            validation_result['suggestions'].append('Request emergency contact phone number')
        elif self.emergency_contact_phone and not self.emergency_contact_name:
            validation_result['warnings'].append('Emergency contact phone provided but name missing')
            validation_result['suggestions'].append('Request emergency contact name')
        
        # Communication preferences validation
        if self.preferred_contact_method == 'sms' and not self.phone_number:
            validation_result['errors'].append('SMS selected as preferred contact method but no phone number provided')
            validation_result['is_valid'] = False
        
        if self.preferred_contact_method == 'phone' and not self.phone_number:
            validation_result['errors'].append('Phone selected as preferred contact method but no phone number provided')
            validation_result['is_valid'] = False
        
        # Marketing consent validation
        if not self.marketing_consent and not self.reminder_consent:
            validation_result['warnings'].append('Client has opted out of all communications')
            validation_result['suggestions'].append('Confirm communication preferences with client')
        
        return validation_result
    
    def clean(self):
        """
        Django model validation method.
        
        Raises:
            ValidationError: If validation fails
        """
        super().clean()
        
        validation = self.validate_contact_info()
        if not validation['is_valid']:
            raise ValidationError(validation['errors'])
    
    def update_contact_info(self, **kwargs):
        """
        Safely update contact information with validation.
        
        Args:
            **kwargs: Contact fields to update
            
        Returns:
            bool: True if update was successful
            
        Raises:
            ValidationError: If validation fails
        """
        # Store original values for rollback
        original_values = {}
        
        # Update fields
        updated_fields = []
        for field_name, value in kwargs.items():
            if hasattr(self, field_name):
                original_values[field_name] = getattr(self, field_name)
                setattr(self, field_name, value)
                updated_fields.append(field_name)
        
        try:
            # Validate the changes
            validation = self.validate_contact_info()
            if not validation['is_valid']:
                # Rollback changes
                for field_name, original_value in original_values.items():
                    setattr(self, field_name, original_value)
                raise ValidationError(validation['errors'])
            
            # Save the changes
            if updated_fields:
                updated_fields.append('updated_at')
                self.save(update_fields=updated_fields)
            
            return True
            
        except ValidationError:
            # Rollback changes
            for field_name, original_value in original_values.items():
                setattr(self, field_name, original_value)
            raise
    
    def get_contact_score(self):
        """
        Calculate a completeness score for contact information.
        
        Returns:
            dict: Contact score and breakdown
        """
        score = 0
        max_score = 100
        breakdown = {}
        
        # Email (required) - 30 points
        if self.user.email:  # type: ignore
            score += 30
            breakdown['email'] = 30
        else:
            breakdown['email'] = 0
        
        # Phone number - 25 points
        if self.phone_number:
            score += 25
            breakdown['phone'] = 25
        else:
            breakdown['phone'] = 0
        
        # Emergency contact name - 15 points
        if self.emergency_contact_name:
            score += 15
            breakdown['emergency_name'] = 15
        else:
            breakdown['emergency_name'] = 0
        
        # Emergency contact phone - 15 points
        if self.emergency_contact_phone:
            score += 15
            breakdown['emergency_phone'] = 15
        else:
            breakdown['emergency_phone'] = 0
        
        # Communication preferences set - 10 points
        if self.preferred_contact_method:
            score += 10
            breakdown['contact_method'] = 10
        else:
            breakdown['contact_method'] = 0
        
        # Consent status clear - 5 points
        if self.marketing_consent is not None and self.reminder_consent is not None:
            score += 5
            breakdown['consent_status'] = 5
        else:
            breakdown['consent_status'] = 0
        
        return {
            'score': score,
            'max_score': max_score,
            'percentage': round((score / max_score) * 100, 1),
            'breakdown': breakdown,
            'completeness_level': self._get_completeness_level(score)
        }
    
    def _get_completeness_level(self, score):
        """
        Get descriptive completeness level based on score.
        
        Args:
            score (int): Contact information score
            
        Returns:
            str: Completeness level description
        """
        if score >= 90:
            return 'excellent'
        elif score >= 75:
            return 'good'
        elif score >= 50:
            return 'fair'
        else:
            return 'poor'
    
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
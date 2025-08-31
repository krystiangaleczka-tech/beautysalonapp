"""
Appointment models for Mario Beauty Salon Management System.
Provides appointment scheduling with conflict prevention and status tracking.
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import connection
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

from apps.core.models import BaseModel
from apps.clients.models import Client
from apps.services.models import Service
from apps.staff.models import StaffProfile



class Appointment(BaseModel):
    """
    Appointment model with status tracking and conflict prevention.
    Task 7.1 - Create Appointment Model implementation.
    """
    
    class AppointmentStatus(models.TextChoices):
        """
        Define appointment status options.
        """
        PENDING = 'pending', _('Pending Confirmation')
        CONFIRMED = 'confirmed', _('Confirmed')
        CHECKED_IN = 'checked_in', _('Checked In')
        IN_PROGRESS = 'in_progress', _('In Progress')
        COMPLETED = 'completed', _('Completed')
        CANCELLED = 'cancelled', _('Cancelled')
        NO_SHOW = 'no_show', _('No Show')
    
    class PaymentStatus(models.TextChoices):
        """
        Define payment status options.
        """
        PENDING = 'pending', _('Payment Pending')
        PARTIAL = 'partial', _('Partially Paid')
        PAID = 'paid', _('Fully Paid')
        REFUNDED = 'refunded', _('Refunded')
    
    # Core appointment information
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='appointments',
        help_text="Client for this appointment"
    )
    
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='appointments',
        help_text="Service to be provided"
    )
    
    staff_member = models.ForeignKey(
        StaffProfile,
        on_delete=models.CASCADE,
        related_name='appointments',
        help_text="Staff member providing the service"
    )
    
    # Appointment scheduling
    scheduled_start_time = models.DateTimeField(
        help_text="Scheduled start time for the appointment"
    )
    
    scheduled_end_time = models.DateTimeField(
        help_text="Scheduled end time for the appointment"
    )
    
    # Status tracking
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.PENDING,
        help_text="Current status of the appointment"
    )
    
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        help_text="Payment status of the appointment"
    )
    
    # Pricing and notes
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Final price for the appointment"
    )
    
    notes = models.TextField(
        blank=True,
        help_text="Additional notes about the appointment"
    )
    
    # Cancellation information
    cancellation_reason = models.TextField(
        blank=True,
        help_text="Reason for cancellation (if applicable)"
    )
    
    # Check-in/check-out times
    actual_start_time = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Actual start time of the service"
    )
    
    actual_end_time = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Actual end time of the service"
    )
    
    class Meta(BaseModel.Meta):  # type: ignore
        db_table = 'appointments'
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
        ordering = ['-scheduled_start_time']
        indexes = [
            models.Index(fields=['scheduled_start_time']),
            models.Index(fields=['status']),
            models.Index(fields=['client']),
            models.Index(fields=['staff_member']),
            models.Index(fields=['service']),
        ]
        constraints = [
            # Ensure appointment times are valid
            models.CheckConstraint(
                check=models.Q(scheduled_start_time__lt=models.F('scheduled_end_time')),
                name='valid_appointment_time_range'
            ),
            # Ensure price is positive
            models.CheckConstraint(
                check=models.Q(price__gte=Decimal('0.00')),
                name='positive_appointment_price'
            ),
        ]
    
    def __str__(self) -> str:  # type: ignore
        client_name = f"{self.client.first_name} {self.client.last_name}"  # type: ignore
        staff_name = f"{self.staff_member.user.first_name} {self.staff_member.user.last_name}"  # type: ignore
        service_name = self.service.name  # type: ignore
        appointment_time = self.scheduled_start_time.strftime('%Y-%m-%d %H:%M')  # type: ignore
        return f"{client_name} - {service_name} with {staff_name} on {appointment_time}"
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Validate appointment time range
        if self.scheduled_start_time and self.scheduled_end_time:
            if self.scheduled_start_time >= self.scheduled_end_time:
                raise ValidationError("Scheduled start time must be before end time")
            
            # Validate that appointment duration matches service duration
            time_diff = self.scheduled_end_time - self.scheduled_start_time  # type: ignore
            scheduled_duration = time_diff.total_seconds() / 60
            service_duration = self.service.total_duration_minutes  # type: ignore
            if scheduled_duration != service_duration:
                raise ValidationError(f"Appointment duration ({scheduled_duration} minutes) must match service duration ({service_duration} minutes)")
        
        # Validate price is reasonable
        if self.price and self.price < Decimal('0.00'):
            raise ValidationError("Price cannot be negative")
        
        # Validate status transitions
        if self.pk:  # Only for existing appointments
            try:
                original = Appointment.objects_with_deleted.get(pk=self.pk)
                if not self._is_valid_status_transition(original.status, self.status):
                    raise ValidationError(f"Invalid status transition from {original.status} to {self.status}")
            except Appointment.DoesNotExist:
                pass  # New appointment, no transition validation needed
    
    def _is_valid_status_transition(self, from_status, to_status):
        """Validate appointment status transitions."""
        valid_transitions = {
            self.AppointmentStatus.PENDING: [self.AppointmentStatus.CONFIRMED, self.AppointmentStatus.CANCELLED],
            self.AppointmentStatus.CONFIRMED: [self.AppointmentStatus.CHECKED_IN, self.AppointmentStatus.CANCELLED, self.AppointmentStatus.NO_SHOW],
            self.AppointmentStatus.CHECKED_IN: [self.AppointmentStatus.IN_PROGRESS, self.AppointmentStatus.NO_SHOW],
            self.AppointmentStatus.IN_PROGRESS: [self.AppointmentStatus.COMPLETED, self.AppointmentStatus.CANCELLED],
            self.AppointmentStatus.COMPLETED: [],
            self.AppointmentStatus.CANCELLED: [self.AppointmentStatus.PENDING],  # Allow rebooking
            self.AppointmentStatus.NO_SHOW: [self.AppointmentStatus.PENDING],  # Allow rebooking
        }
        
        return to_status in valid_transitions.get(from_status, [])
    
    def save(self, *args, **kwargs):
        """Override save to perform additional validation."""
        is_new = self.pk is None
        old_status = None
        
        # Get old status if this is an update
        if not is_new:
            try:
                old_instance = Appointment.objects.get(pk=self.pk)
                old_status = old_instance.status
            except Appointment.DoesNotExist:
                pass
        
        self.clean()
        super().save(*args, **kwargs)
        
        # Trigger notifications for new appointments or status changes
        try:
            from apps.notifications.services import NotificationService
            
            # Prepare appointment details for notification
            appointment_details = {
                'service_name': self.service.name,
                'datetime': self.scheduled_start_time.strftime('%Y-%m-%d %H:%M'),
                'staff_name': f"{self.staff_member.user.first_name} {self.staff_member.user.last_name}",
                'duration': self.service.duration_minutes,
                'price': float(self.price),
            }
            
            # Handle status changes
            if is_new:
                # Send confirmation for new appointments
                NotificationService.send_appointment_confirmation(
                    client=self.client,
                    appointment_details=appointment_details
                )
            elif old_status != self.status:
                if (old_status == Appointment.AppointmentStatus.PENDING and 
                    self.status == Appointment.AppointmentStatus.CONFIRMED):
                    # Send confirmation when appointment is confirmed
                    NotificationService.send_appointment_confirmation(
                        client=self.client,
                        appointment_details=appointment_details
                    )
                elif self.status == Appointment.AppointmentStatus.CANCELLED:
                    # Add cancellation reason to details
                    appointment_details['cancellation_reason'] = self.cancellation_reason or "No reason provided"
                    # Send cancellation notification
                    NotificationService.send_appointment_cancellation(
                        client=self.client,
                        appointment_details=appointment_details
                    )
        except (ImportError, AttributeError):
            # Handle case where notification service is not available
            pass
    
    @property
    def duration_minutes(self):
        """Calculate appointment duration in minutes."""
        if self.scheduled_start_time and self.scheduled_end_time:
            time_diff = self.scheduled_end_time - self.scheduled_start_time  # type: ignore
            return time_diff.total_seconds() / 60
        return 0
    
    @property
    def is_confirmed(self):
        """Check if appointment is confirmed."""
        return self.status in [self.AppointmentStatus.CONFIRMED, self.AppointmentStatus.CHECKED_IN, 
                              self.AppointmentStatus.IN_PROGRESS, self.AppointmentStatus.COMPLETED]
    
    @property
    def is_cancelled(self):
        """Check if appointment is cancelled."""
        return self.status == self.AppointmentStatus.CANCELLED
    
    @property
    def is_completed(self):
        """Check if appointment is completed."""
        return self.status == self.AppointmentStatus.COMPLETED
    
    def confirm(self):
        """Confirm the appointment."""
        if self.status == self.AppointmentStatus.PENDING:
            self.status = self.AppointmentStatus.CONFIRMED
            self.save()
    
    def cancel(self, reason=""):
        """Cancel the appointment."""
        if self.status not in [self.AppointmentStatus.COMPLETED]:
            self.status = self.AppointmentStatus.CANCELLED
            self.cancellation_reason = reason
            self.save()
    
    def check_in(self):
        """Mark appointment as checked in."""
        if self.status == self.AppointmentStatus.CONFIRMED:
            self.status = self.AppointmentStatus.CHECKED_IN
            self.actual_start_time = timezone.now()
            self.save()
    
    def start_service(self):
        """Mark appointment as in progress."""
        if self.status == self.AppointmentStatus.CHECKED_IN:
            self.status = self.AppointmentStatus.IN_PROGRESS
            self.save()
    
    def complete(self):
        """Mark appointment as completed."""
        if self.status == self.AppointmentStatus.IN_PROGRESS:
            self.status = self.AppointmentStatus.COMPLETED
            self.actual_end_time = timezone.now()
            self.payment_status = self.PaymentStatus.PAID
            self.save()
    
    def mark_no_show(self):
        """Mark appointment as no show."""
        if self.status in [self.AppointmentStatus.CONFIRMED, self.AppointmentStatus.CHECKED_IN]:
            self.status = self.AppointmentStatus.NO_SHOW
            self.save()
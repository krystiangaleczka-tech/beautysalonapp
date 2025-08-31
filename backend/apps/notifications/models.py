"""
Notification models for Mario Beauty Salon Management System.
Provides notification tracking with delivery status and templates.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.core.models import BaseModel
from apps.clients.models import Client


class Notification(BaseModel):
    """
    Notification tracking model.
    Task 8.1 - Create Notification Models implementation.
    """
    
    class NotificationType(models.TextChoices):
        """
        Define notification types.
        """
        EMAIL = 'email', _('Email')
        SMS = 'sms', _('SMS')
        PUSH = 'push', _('Push Notification')
        IN_APP = 'in_app', _('In-App Notification')
    
    class DeliveryStatus(models.TextChoices):
        """
        Define delivery status options.
        """
        PENDING = 'pending', _('Pending')
        SENT = 'sent', _('Sent')
        DELIVERED = 'delivered', _('Delivered')
        FAILED = 'failed', _('Failed')
        READ = 'read', _('Read')
    
    # Core notification information
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='notifications',
        help_text="Client to receive this notification"
    )
    
    notification_type = models.CharField(
        max_length=10,
        choices=NotificationType.choices,
        help_text="Type of notification"
    )
    
    subject = models.CharField(
        max_length=200,
        blank=True,
        help_text="Notification subject (for email)"
    )
    
    message = models.TextField(
        help_text="Notification message content"
    )
    
    # Delivery tracking
    delivery_status = models.CharField(
        max_length=15,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING,
        help_text="Current delivery status of the notification"
    )
    
    sent_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the notification was sent"
    )
    
    delivered_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the notification was delivered"
    )
    
    read_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the notification was read"
    )
    
    # Metadata
    template_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Template used for this notification"
    )
    
    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Additional metadata for the notification"
    )
    
    error_message = models.TextField(
        blank=True,
        help_text="Error message if delivery failed"
    )
    
    class Meta(BaseModel.Meta):  # type: ignore
        db_table = 'notifications'
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['client']),
            models.Index(fields=['notification_type']),
            models.Index(fields=['delivery_status']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self) -> str:  # type: ignore
        client_name = f"{self.client.first_name} {self.client.last_name}"  # type: ignore
        return f"Notification to {client_name} - {self.notification_type} - {self.delivery_status}"
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Validate subject is required for email notifications
        if self.notification_type == self.NotificationType.EMAIL and not self.subject:
            raise ValidationError("Subject is required for email notifications")
    
    def save(self, *args, **kwargs):
        """Override save to perform additional validation."""
        self.clean()
        super().save(*args, **kwargs)
    
    @property
    def is_read(self):
        """Check if notification has been read."""
        return self.delivery_status == self.DeliveryStatus.READ
    
    @property
    def is_delivered(self):
        """Check if notification has been delivered."""
        return self.delivery_status in [self.DeliveryStatus.DELIVERED, self.DeliveryStatus.READ]
    
    def mark_as_sent(self):
        """Mark notification as sent."""
        from django.utils import timezone
        if self.delivery_status == self.DeliveryStatus.PENDING:
            self.delivery_status = self.DeliveryStatus.SENT
            self.sent_at = timezone.now()
            self.save()
    
    def mark_as_delivered(self):
        """Mark notification as delivered."""
        from django.utils import timezone
        if self.delivery_status in [self.DeliveryStatus.PENDING, self.DeliveryStatus.SENT]:
            self.delivery_status = self.DeliveryStatus.DELIVERED
            self.delivered_at = timezone.now()
            self.save()
    
    def mark_as_read(self):
        """Mark notification as read."""
        from django.utils import timezone
        if self.delivery_status in [self.DeliveryStatus.DELIVERED, self.DeliveryStatus.SENT]:
            self.delivery_status = self.DeliveryStatus.READ
            self.read_at = timezone.now()
            self.save()
    
    def mark_as_failed(self, error_message=""):
        """Mark notification as failed."""
        if self.delivery_status != self.DeliveryStatus.READ:
            self.delivery_status = self.DeliveryStatus.FAILED
            self.error_message = error_message
            self.save()
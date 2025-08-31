"""
Notification services for Mario Beauty Salon Management System.
Provides email and SMS sending logic with basic templates.
"""

import logging
from typing import Optional, Dict, Any
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from twilio.rest import Client as TwilioClient

from .models import Notification, Client

logger = logging.getLogger(__name__)


class NotificationService:
    """
    Service class for handling notification sending.
    Task 8.3 - Implement Notification Services implementation.
    """
    
    @staticmethod
    def send_email_notification(
        client: Client,
        subject: str,
        message: str,
        template_name: str = "",
        metadata: Optional[Dict[str, Any]] = None
    ) -> Notification:
        """
        Send an email notification to a client.
        
        Args:
            client: Client to send notification to
            subject: Email subject
            message: Email message content
            template_name: Template used (optional)
            metadata: Additional metadata (optional)
            
        Returns:
            Notification: Created notification object
        """
        # Create notification record
        notification = Notification.objects.create(
            client=client,
            notification_type=Notification.NotificationType.EMAIL,
            subject=subject,
            message=message,
            template_name=template_name,
            metadata=metadata or {}
        )
        
        try:
            # Send email
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[client.email],
                fail_silently=False,
            )
            
            # Mark as sent
            notification.mark_as_sent()
            logger.info(f"Email notification sent to {client.email}")
            
        except Exception as e:
            error_message = str(e)
            notification.mark_as_failed(error_message)
            logger.error(f"Failed to send email notification to {client.email}: {error_message}")
            raise
        
        return notification
    
    @staticmethod
    def send_sms_notification(
        client: Client,
        message: str,
        template_name: str = "",
        metadata: Optional[Dict[str, Any]] = None
    ) -> Notification:
        """
        Send an SMS notification to a client.
        
        Args:
            client: Client to send notification to
            message: SMS message content
            template_name: Template used (optional)
            metadata: Additional metadata (optional)
            
        Returns:
            Notification: Created notification object
        """
        # Create notification record
        notification = Notification.objects.create(
            client=client,
            notification_type=Notification.NotificationType.SMS,
            message=message,
            template_name=template_name,
            metadata=metadata or {}
        )
        
        try:
            # Send SMS using Twilio
            if hasattr(settings, 'TWILIO_ACCOUNT_SID') and hasattr(settings, 'TWILIO_AUTH_TOKEN'):
                twilio_client = TwilioClient(
                    settings.TWILIO_ACCOUNT_SID,
                    settings.TWILIO_AUTH_TOKEN
                )
                
                twilio_client.messages.create(
                    body=message,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=client.phone
                )
                
                # Mark as sent
                notification.mark_as_sent()
                logger.info(f"SMS notification sent to {client.phone}")
            else:
                # If Twilio is not configured, mark as failed
                error_message = "Twilio not configured"
                notification.mark_as_failed(error_message)
                logger.error(f"Failed to send SMS notification to {client.phone}: {error_message}")
                raise Exception(error_message)
                
        except Exception as e:
            error_message = str(e)
            notification.mark_as_failed(error_message)
            logger.error(f"Failed to send SMS notification to {client.phone}: {error_message}")
            raise
        
        return notification
    
    @staticmethod
    def send_appointment_confirmation(
        client: Client,
        appointment_details: Dict[str, Any]
    ) -> None:
        """
        Send appointment confirmation notification.
        
        Args:
            client: Client to send notification to
            appointment_details: Appointment details
        """
        # Email template
        subject = "Appointment Confirmation"
        email_message = f"""
Dear {client.first_name},

Your appointment has been confirmed with the following details:

Service: {appointment_details.get('service_name', 'N/A')}
Date & Time: {appointment_details.get('datetime', 'N/A')}
Staff: {appointment_details.get('staff_name', 'N/A')}
Duration: {appointment_details.get('duration', 'N/A')} minutes
Price: ${appointment_details.get('price', 'N/A')}

Please arrive 10 minutes before your scheduled appointment time.

Thank you for choosing Mario Beauty Salon!

Best regards,
Mario Beauty Salon Team
        """.strip()
        
        # SMS template
        sms_message = f"""
Appointment confirmed: {appointment_details.get('service_name', 'N/A')} on {appointment_details.get('datetime', 'N/A')}. 
Please arrive 10 mins early. 
Mario Beauty Salon
        """.strip()
        
        # Send email notification
        NotificationService.send_email_notification(
            client=client,
            subject=subject,
            message=email_message,
            template_name="appointment_confirmation_email",
            metadata=appointment_details
        )
        
        # Send SMS notification if phone number is available
        if client.phone:
            try:
                NotificationService.send_sms_notification(
                    client=client,
                    message=sms_message,
                    template_name="appointment_confirmation_sms",
                    metadata=appointment_details
                )
            except Exception as e:
                logger.warning(f"Failed to send SMS for appointment confirmation: {e}")
    
    @staticmethod
    def send_appointment_reminder(
        client: Client,
        appointment_details: Dict[str, Any]
    ) -> None:
        """
        Send appointment reminder notification.
        
        Args:
            client: Client to send notification to
            appointment_details: Appointment details
        """
        # Email template
        subject = "Appointment Reminder"
        email_message = f"""
Dear {client.first_name},

This is a reminder for your upcoming appointment:

Service: {appointment_details.get('service_name', 'N/A')}
Date & Time: {appointment_details.get('datetime', 'N/A')}
Staff: {appointment_details.get('staff_name', 'N/A')}
Duration: {appointment_details.get('duration', 'N/A')} minutes

Please remember to arrive 10 minutes before your scheduled appointment time.

We look forward to seeing you at Mario Beauty Salon!

Best regards,
Mario Beauty Salon Team
        """.strip()
        
        # SMS template
        sms_message = f"""
Reminder: {appointment_details.get('service_name', 'N/A')} tomorrow at {appointment_details.get('time', 'N/A')}. 
Please arrive 10 mins early. 
Mario Beauty Salon
        """.strip()
        
        # Send email notification
        NotificationService.send_email_notification(
            client=client,
            subject=subject,
            message=email_message,
            template_name="appointment_reminder_email",
            metadata=appointment_details
        )
        
        # Send SMS notification if phone number is available
        if client.phone:
            try:
                NotificationService.send_sms_notification(
                    client=client,
                    message=sms_message,
                    template_name="appointment_reminder_sms",
                    metadata=appointment_details
                )
            except Exception as e:
                logger.warning(f"Failed to send SMS for appointment reminder: {e}")
    
    @staticmethod
    def send_appointment_cancellation(
        client: Client,
        appointment_details: Dict[str, Any]
    ) -> None:
        """
        Send appointment cancellation notification.
        
        Args:
            client: Client to send notification to
            appointment_details: Appointment details
        """
        # Email template
        subject = "Appointment Cancellation"
        email_message = f"""
Dear {client.first_name},

Your appointment has been cancelled with the following details:

Service: {appointment_details.get('service_name', 'N/A')}
Original Date & Time: {appointment_details.get('datetime', 'N/A')}
Staff: {appointment_details.get('staff_name', 'N/A')}

Reason: {appointment_details.get('cancellation_reason', 'No reason provided')}

We apologize for any inconvenience this may cause. Please contact us to reschedule your appointment.

Best regards,
Mario Beauty Salon Team
        """.strip()
        
        # SMS template
        sms_message = f"""
Appointment cancelled: {appointment_details.get('service_name', 'N/A')} on {appointment_details.get('datetime', 'N/A')}. 
Reason: {appointment_details.get('cancellation_reason', 'N/A')}. 
Call to reschedule. 
Mario Beauty Salon
        """.strip()
        
        # Send email notification
        NotificationService.send_email_notification(
            client=client,
            subject=subject,
            message=email_message,
            template_name="appointment_cancellation_email",
            metadata=appointment_details
        )
        
        # Send SMS notification if phone number is available
        if client.phone:
            try:
                NotificationService.send_sms_notification(
                    client=client,
                    message=sms_message,
                    template_name="appointment_cancellation_sms",
                    metadata=appointment_details
                )
            except Exception as e:
                logger.warning(f"Failed to send SMS for appointment cancellation: {e}")
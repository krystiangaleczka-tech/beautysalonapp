"""
Tests for Notification models and services.
"""

import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest.mock import patch, MagicMock
from datetime import datetime

from apps.clients.models import Client
from .models import Notification
from .services import NotificationService


class NotificationModelTest(TestCase):
    """Test cases for Notification model."""
    
    def setUp(self):
        """Set up test data."""
        self.client = Client.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890"
        )
    
    def test_notification_creation(self):
        """Test creating a notification."""
        notification = Notification.objects.create(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Test Subject",
            message="Test Message",
            delivery_status=Notification.DeliveryStatus.PENDING
        )
        
        self.assertEqual(notification.client, self.client)
        self.assertEqual(notification.notification_type, Notification.NotificationType.EMAIL)
        self.assertEqual(notification.subject, "Test Subject")
        self.assertEqual(notification.message, "Test Message")
        self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.PENDING)
        self.assertFalse(notification.is_read)
        self.assertFalse(notification.is_delivered)
    
    def test_notification_string_representation(self):
        """Test notification string representation."""
        notification = Notification.objects.create(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Test Subject",
            message="Test Message"
        )
        
        expected_str = f"Notification to John Doe - {Notification.NotificationType.EMAIL} - {Notification.DeliveryStatus.PENDING}"
        self.assertEqual(str(notification), expected_str)
    
    def test_email_notification_requires_subject(self):
        """Test that email notifications require a subject."""
        with self.assertRaises(ValidationError):
            notification = Notification(
                client=self.client,
                notification_type=Notification.NotificationType.EMAIL,
                message="Test Message"
            )
            notification.full_clean()
    
    def test_sms_notification_does_not_require_subject(self):
        """Test that SMS notifications don't require a subject."""
        notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.SMS,
            message="Test Message"
        )
        # This should not raise an exception
        notification.full_clean()
        notification.save()
    
    def test_notification_status_transitions(self):
        """Test notification status transitions."""
        notification = Notification.objects.create(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Test Subject",
            message="Test Message"
        )
        
        # Test mark as sent
        notification.mark_as_sent()
        self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.SENT)
        self.assertIsNotNone(notification.sent_at)
        
        # Test mark as delivered
        notification.mark_as_delivered()
        self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.DELIVERED)
        self.assertIsNotNone(notification.delivered_at)
        
        # Test mark as read
        notification.mark_as_read()
        self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.READ)
        self.assertIsNotNone(notification.read_at)
        
        # Create a new notification to test mark as failed
        notification2 = Notification.objects.create(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Test Subject 2",
            message="Test Message 2"
        )
        
        # Test mark as failed
        notification2.mark_as_failed("Test error")
        self.assertEqual(notification2.delivery_status, Notification.DeliveryStatus.FAILED)
        self.assertEqual(notification2.error_message, "Test error")


class NotificationServiceTest(TestCase):
    """Test cases for NotificationService."""
    
    def setUp(self):
        """Set up test data."""
        self.client = Client.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890"
        )
        
        self.appointment_details = {
            'service_name': 'Manicure',
            'datetime': '2025-09-15 14:00',
            'staff_name': 'Jane Smith',
            'duration': 60,
            'price': 25.00
        }
    
    @patch('apps.notifications.services.send_mail')
    def test_send_email_notification(self, mock_send_mail):
        """Test sending email notification."""
        mock_send_mail.return_value = 1  # Simulate successful send
        
        notification = NotificationService.send_email_notification(
            client=self.client,
            subject="Test Subject",
            message="Test Message"
        )
        
        # Verify notification was created
        self.assertEqual(notification.client, self.client)
        self.assertEqual(notification.notification_type, Notification.NotificationType.EMAIL)
        self.assertEqual(notification.subject, "Test Subject")
        self.assertEqual(notification.message, "Test Message")
        self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.SENT)
        
        # Verify email was sent
        mock_send_mail.assert_called_once()
    
    @patch('apps.notifications.services.TwilioClient')
    def test_send_sms_notification(self, mock_twilio_client):
        """Test sending SMS notification."""
        # Configure mock
        mock_message = MagicMock()
        mock_twilio_client_instance = MagicMock()
        mock_twilio_client_instance.messages.create.return_value = mock_message
        mock_twilio_client.return_value = mock_twilio_client_instance
        
        with self.settings(TWILIO_ACCOUNT_SID='test_sid', TWILIO_AUTH_TOKEN='test_token'):
            notification = NotificationService.send_sms_notification(
                client=self.client,
                message="Test SMS Message"
            )
            
            # Verify notification was created
            self.assertEqual(notification.client, self.client)
            self.assertEqual(notification.notification_type, Notification.NotificationType.SMS)
            self.assertEqual(notification.message, "Test SMS Message")
            self.assertEqual(notification.delivery_status, Notification.DeliveryStatus.SENT)
            
            # Verify SMS was sent
            mock_twilio_client_instance.messages.create.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_email_notification')
    @patch('apps.notifications.services.NotificationService.send_sms_notification')
    def test_send_appointment_confirmation(self, mock_send_sms, mock_send_email):
        """Test sending appointment confirmation."""
        # Configure mocks
        email_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Appointment Confirmation",
            message="Test email message"
        )
        sms_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.SMS,
            message="Test SMS message"
        )
        mock_send_email.return_value = email_notification
        mock_send_sms.return_value = sms_notification
        
        # Send appointment confirmation
        NotificationService.send_appointment_confirmation(
            client=self.client,
            appointment_details=self.appointment_details
        )
        
        # Verify both email and SMS notifications were sent
        mock_send_email.assert_called_once()
        mock_send_sms.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_email_notification')
    @patch('apps.notifications.services.NotificationService.send_sms_notification')
    def test_send_appointment_reminder(self, mock_send_sms, mock_send_email):
        """Test sending appointment reminder."""
        # Configure mocks
        email_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Appointment Reminder",
            message="Test email message"
        )
        sms_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.SMS,
            message="Test SMS message"
        )
        mock_send_email.return_value = email_notification
        mock_send_sms.return_value = sms_notification
        
        # Send appointment reminder
        NotificationService.send_appointment_reminder(
            client=self.client,
            appointment_details=self.appointment_details
        )
        
        # Verify both email and SMS notifications were sent
        mock_send_email.assert_called_once()
        mock_send_sms.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_email_notification')
    @patch('apps.notifications.services.NotificationService.send_sms_notification')
    def test_send_appointment_cancellation(self, mock_send_sms, mock_send_email):
        """Test sending appointment cancellation."""
        # Configure mocks
        email_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.EMAIL,
            subject="Appointment Cancellation",
            message="Test email message"
        )
        sms_notification = Notification(
            client=self.client,
            notification_type=Notification.NotificationType.SMS,
            message="Test SMS message"
        )
        mock_send_email.return_value = email_notification
        mock_send_sms.return_value = sms_notification
        
        # Add cancellation reason to details
        cancellation_details = self.appointment_details.copy()
        cancellation_details['cancellation_reason'] = "Staff unavailable"
        
        # Send appointment cancellation
        NotificationService.send_appointment_cancellation(
            client=self.client,
            appointment_details=cancellation_details
        )
        
        # Verify both email and SMS notifications were sent
        mock_send_email.assert_called_once()
        mock_send_sms.assert_called_once()
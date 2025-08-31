"""
Test suite for Appointment Models.
Tests Appointment model functionality, constraints, and status tracking.
"""

import pytest
from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

from apps.clients.models import Client
from apps.services.models import Service, ServiceCategory
from apps.staff.models import StaffProfile, Specialization
from apps.authentication.models import SalonUser
from .models import Appointment
from .services import AppointmentService
from .tasks import send_appointment_confirmation, send_appointment_reminder, send_appointment_cancellation


class AppointmentNotificationTest(TestCase):
    """Test cases for appointment notification integration."""
    
    def setUp(self):
        """Set up test data."""
        # Create client
        self.client_obj = Client.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890"
        )
        
        # Create staff user
        self.staff_user = SalonUser.objects.create_user(
            username="jane_smith",
            email="staff@example.com",
            password="testpass123",
            first_name="Jane",
            last_name="Smith"
        )
        
        # Create specialization
        self.specialization = Specialization.objects.create(
            name="Hair Styling",
            specialization_type=Specialization.SpecializationType.BEAUTY_TREATMENT,
            description="Hair styling services",
            is_active=True
        )
        
        # Create staff profile
        self.staff_member = StaffProfile.objects.create(
            user=self.staff_user,
            certification_level=StaffProfile.CertificationLevel.SENIOR,
            years_of_experience=5,
            hourly_rate=50.00,
            max_clients_per_day=8,
            languages_spoken="English,Spanish",
            availability_notes="Available weekdays",
            is_accepting_new_clients=True,
            emergency_contact_name="Emergency Contact",
            emergency_contact_phone="+1234567891"
        )
        
        # Add specialization to staff member
        self.staff_member.specializations.add(self.specialization)
        
        # Create service category
        self.category = ServiceCategory.objects.create(
            name="Hair Services",
            description="Hair care services",
            is_active=True,
            display_order=1
        )
        
        # Create service
        self.service = Service.objects.create(
            name="Haircut",
            description="Basic haircut service",
            base_price=30.00,
            duration_minutes=30,
            is_active=True,
            requires_consultation=False,
            preparation_time=5,
            cleanup_time=5,
            display_order=1,
            category=self.category
        )
        
        # Create appointment without triggering notifications by mocking the service
        with patch('apps.notifications.services.NotificationService'):
            self.appointment_time = timezone.now() + timedelta(days=1)
            self.appointment = Appointment.objects.create(
                client=self.client_obj,
                service=self.service,
                staff_member=self.staff_member,
                scheduled_start_time=self.appointment_time,
                scheduled_end_time=self.appointment_time + timedelta(minutes=40),  # 30 min service + 5 min prep + 5 min cleanup
                price=30.00
            )
    
    @patch('apps.notifications.services.NotificationService.send_appointment_confirmation')
    def test_appointment_creation_triggers_confirmation(self, mock_send_confirmation):
        """Test that creating a new appointment triggers a confirmation notification."""
        # Create a new appointment
        appointment_time = timezone.now() + timedelta(days=2)
        # Don't mock the NotificationService here so the notification is actually sent
        new_appointment = Appointment.objects.create(
            client=self.client_obj,
            service=self.service,
            staff_member=self.staff_member,
            scheduled_start_time=appointment_time,
            scheduled_end_time=appointment_time + timedelta(minutes=40),  # 30 min service + 5 min prep + 5 min cleanup
            price=30.00
        )
        
        # Verify that the confirmation notification was triggered
        mock_send_confirmation.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_appointment_confirmation')
    def test_appointment_confirmation_triggers_notification(self, mock_send_confirmation):
        """Test that confirming an appointment triggers a confirmation notification."""
        # Change appointment status from pending to confirmed
        self.appointment.status = Appointment.AppointmentStatus.CONFIRMED
        self.appointment.save()
        
        # Verify that the confirmation notification was triggered
        mock_send_confirmation.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_appointment_cancellation')
    def test_appointment_cancellation_triggers_notification(self, mock_send_cancellation):
        """Test that cancelling an appointment triggers a cancellation notification."""
        # Change appointment status to cancelled
        self.appointment.status = Appointment.AppointmentStatus.CANCELLED
        self.appointment.cancellation_reason = "Client request"
        self.appointment.save()
        
        # Verify that the cancellation notification was triggered
        mock_send_cancellation.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_appointment_reminder')
    def test_send_appointment_reminder_task(self, mock_send_reminder):
        """Test the send_appointment_reminder task."""
        # Call the task directly
        send_appointment_reminder(self.appointment.id)
        
        # Verify that the reminder notification was sent
        mock_send_reminder.assert_called_once()
    
    @patch('apps.notifications.services.NotificationService.send_appointment_cancellation')
    def test_send_appointment_cancellation_task(self, mock_send_cancellation):
        """Test the send_appointment_cancellation task."""
        # Create a new appointment specifically for this test to avoid conflicts
        with patch('apps.notifications.services.NotificationService'):
            appointment_time = timezone.now() + timedelta(days=3)
            test_appointment = Appointment.objects.create(
                client=self.client_obj,
                service=self.service,
                staff_member=self.staff_member,
                scheduled_start_time=appointment_time,
                scheduled_end_time=appointment_time + timedelta(minutes=40),
                price=30.00,
                status=Appointment.AppointmentStatus.CANCELLED,
                cancellation_reason="Staff unavailable"
            )
        
        # Call the task directly (without saving the appointment again)
        send_appointment_cancellation(test_appointment.id)
        
        # Verify that the cancellation notification was sent
        mock_send_cancellation.assert_called_once()
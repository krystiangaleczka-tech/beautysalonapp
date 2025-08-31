"""
Test suite for Appointment Models.
Tests Appointment model functionality, constraints, and status tracking.
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from apps.clients.models import Client
from apps.services.models import Service, ServiceCategory
from apps.staff.models import StaffProfile, Specialization
from apps.authentication.models import SalonUser
from apps.appointments.models import Appointment


class AppointmentModelTestCase(TestCase):
    """Test suite for Appointment model functionality."""
    
    def setUp(self):
        """Set up test data."""
        # Create a client
        self.client = Client.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890"
        )
        
        # Create a service category
        self.category = ServiceCategory.objects.create(
            name="Nail Services",
            description="Various nail care services"
        )
        
        # Create a service
        self.service = Service.objects.create(
            name="Basic Manicure",
            description="Basic nail care service",
            category=self.category,
            base_price=25.00,
            duration_minutes=30
        )
        
        # Create a salon user (staff)
        self.salon_user = SalonUser.objects.create_user(
            username="jane_smith",
            email="staff@example.com",
            password="testpass123",
            first_name="Jane",
            last_name="Smith"
        )
        
        # Create a staff profile
        self.staff_profile = StaffProfile.objects.create(
            user=self.salon_user,
            certification_level=StaffProfile.CertificationLevel.JUNIOR,
            years_of_experience=2
        )
        
        # Create appointment start and end times
        self.start_time = timezone.now() + timedelta(days=1)
        self.end_time = self.start_time + timedelta(minutes=30)
        
        # Create an appointment
        self.appointment = Appointment.objects.create(
            client=self.client,
            service=self.service,
            staff_member=self.staff_profile,
            scheduled_start_time=self.start_time,
            scheduled_end_time=self.end_time,
            price=25.00
        )
    
    def test_appointment_creation(self):
        """Test that appointment is created correctly."""
        self.assertEqual(self.appointment.client, self.client)
        self.assertEqual(self.appointment.service, self.service)
        self.assertEqual(self.appointment.staff_member, self.staff_profile)
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.PENDING)
        self.assertEqual(self.appointment.payment_status, Appointment.PaymentStatus.PENDING)
        self.assertEqual(self.appointment.price, 25.00)
    
    def test_appointment_string_representation(self):
        """Test appointment string representation."""
        expected_str = f"{self.client.first_name} {self.client.last_name} - {self.service.name} with {self.salon_user.first_name} {self.salon_user.last_name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"
        self.assertEqual(str(self.appointment), expected_str)
    
    def test_appointment_duration_property(self):
        """Test appointment duration calculation."""
        self.assertEqual(self.appointment.duration_minutes, 30)
    
    def test_appointment_status_properties(self):
        """Test appointment status properties."""
        # Test initial state
        self.assertFalse(self.appointment.is_confirmed)
        self.assertFalse(self.appointment.is_cancelled)
        self.assertFalse(self.appointment.is_completed)
        
        # Confirm appointment
        self.appointment.confirm()
        self.assertTrue(self.appointment.is_confirmed)
        self.assertFalse(self.appointment.is_cancelled)
        self.assertFalse(self.appointment.is_completed)
    
    def test_appointment_status_transitions(self):
        """Test appointment status transitions."""
        # Test confirming appointment
        self.appointment.confirm()
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.CONFIRMED)
        
        # Test checking in
        self.appointment.check_in()
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.CHECKED_IN)
        self.assertIsNotNone(self.appointment.actual_start_time)
        
        # Test starting service
        self.appointment.start_service()
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.IN_PROGRESS)
        
        # Test completing appointment
        self.appointment.complete()
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.COMPLETED)
        self.assertEqual(self.appointment.payment_status, Appointment.PaymentStatus.PAID)
        self.assertIsNotNone(self.appointment.actual_end_time)
    
    def test_invalid_appointment_time_range(self):
        """Test that invalid time ranges are rejected."""
        with self.assertRaises(ValidationError):
            appointment = Appointment(
                client=self.client,
                service=self.service,
                staff_member=self.staff_profile,
                scheduled_start_time=self.end_time,  # Start after end
                scheduled_end_time=self.start_time,
                price=25.00
            )
            appointment.clean()
    
    def test_appointment_cancellation(self):
        """Test appointment cancellation."""
        self.appointment.cancel("Client request")
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.CANCELLED)
        self.assertEqual(self.appointment.cancellation_reason, "Client request")
    
    def test_appointment_no_show(self):
        """Test marking appointment as no show."""
        # Confirm appointment first
        self.appointment.confirm()
        
        # Mark as no show
        self.appointment.mark_no_show()
        self.assertEqual(self.appointment.status, Appointment.AppointmentStatus.NO_SHOW)
    
    def test_invalid_status_transitions(self):
        """Test that invalid status transitions are rejected."""
        # Try to complete a pending appointment (should fail)
        with self.assertRaises(ValidationError):
            original_status = self.appointment.status
            self.appointment.status = Appointment.AppointmentStatus.COMPLETED
            self.appointment.clean()
    
    def test_appointment_duration_validation(self):
        """Test that appointment duration matches service duration."""
        # Create appointment with incorrect duration
        with self.assertRaises(ValidationError):
            appointment = Appointment(
                client=self.client,
                service=self.service,
                staff_member=self.staff_profile,
                scheduled_start_time=self.start_time,
                scheduled_end_time=self.start_time + timedelta(minutes=60),  # 60 min instead of 30
                price=25.00
            )
            appointment.clean()


class AppointmentServiceTestCase(TestCase):
    """Test suite for Appointment service functionality."""
    
    def setUp(self):
        """Set up test data."""
        # Create test data (similar to above)
        self.client = Client.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890"
        )
        
        self.category = ServiceCategory.objects.create(
            name="Nail Services",
            description="Various nail care services"
        )
        
        self.service = Service.objects.create(
            name="Basic Manicure",
            description="Basic nail care service",
            category=self.category,
            base_price=25.00,
            duration_minutes=30
        )
        
        self.salon_user = SalonUser.objects.create_user(
            username="jane_smith",
            email="staff@example.com",
            password="testpass123",
            first_name="Jane",
            last_name="Smith"
        )
        
        self.staff_profile = StaffProfile.objects.create(
            user=self.salon_user,
            certification_level=StaffProfile.CertificationLevel.JUNIOR,
            years_of_experience=2
        )
        
        self.start_time = timezone.now() + timedelta(days=1)
        self.end_time = self.start_time + timedelta(minutes=30)
        
        self.appointment = Appointment.objects.create(
            client=self.client,
            service=self.service,
            staff_member=self.staff_profile,
            scheduled_start_time=self.start_time,
            scheduled_end_time=self.end_time,
            price=25.00
        )
    
    def test_staff_availability_check(self):
        """Test staff availability checking."""
        from apps.appointments.services import AppointmentService
        
        # Test available time slot
        available_start = self.start_time + timedelta(hours=2)
        available_end = available_start + timedelta(minutes=30)
        
        is_available = AppointmentService.check_staff_availability(
            self.staff_profile, available_start, available_end
        )
        self.assertTrue(is_available)
    
    def test_client_availability_check(self):
        """Test client availability checking."""
        from apps.appointments.services import AppointmentService
        
        # Test available time slot
        available_start = self.start_time + timedelta(hours=2)
        available_end = available_start + timedelta(minutes=30)
        
        is_available = AppointmentService.check_client_availability(
            self.client, available_start, available_end
        )
        self.assertTrue(is_available)
"""
Task functions for appointment notifications.
Provides functions for appointment-related notifications.
"""

from django.utils import timezone
from datetime import timedelta
import logging

from .models import Appointment
from apps.notifications.services import NotificationService

logger = logging.getLogger(__name__)


def send_appointment_confirmation(appointment_id: int) -> None:
    """
    Send appointment confirmation notification.
    
    Args:
        appointment_id: ID of the appointment to send confirmation for
    """
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Prepare appointment details for notification
        appointment_details = {
            'service_name': appointment.service.name,
            'datetime': appointment.scheduled_start_time.strftime('%Y-%m-%d %H:%M'),
            'staff_name': f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            'duration': appointment.service.duration_minutes,
            'price': float(appointment.price),
        }
        
        # Send confirmation notification
        NotificationService.send_appointment_confirmation(
            client=appointment.client,
            appointment_details=appointment_details
        )
        
        logger.info(f"Appointment confirmation sent for appointment {appointment_id}")
    except Appointment.DoesNotExist:
        logger.error(f"Appointment {appointment_id} not found for confirmation")
    except Exception as e:
        logger.error(f"Failed to send appointment confirmation for appointment {appointment_id}: {e}")


def send_appointment_reminder(appointment_id: int) -> None:
    """
    Send appointment reminder notification.
    
    Args:
        appointment_id: ID of the appointment to send reminder for
    """
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Prepare appointment details for notification
        appointment_details = {
            'service_name': appointment.service.name,
            'datetime': appointment.scheduled_start_time.strftime('%Y-%m-%d %H:%M'),
            'time': appointment.scheduled_start_time.strftime('%H:%M'),
            'staff_name': f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            'duration': appointment.service.duration_minutes,
        }
        
        # Send reminder notification
        NotificationService.send_appointment_reminder(
            client=appointment.client,
            appointment_details=appointment_details
        )
        
        logger.info(f"Appointment reminder sent for appointment {appointment_id}")
    except Appointment.DoesNotExist:
        logger.error(f"Appointment {appointment_id} not found for reminder")
    except Exception as e:
        logger.error(f"Failed to send appointment reminder for appointment {appointment_id}: {e}")


def send_appointment_cancellation(appointment_id: int) -> None:
    """
    Send appointment cancellation notification.
    
    Args:
        appointment_id: ID of the appointment to send cancellation for
    """
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Prepare appointment details for notification
        appointment_details = {
            'service_name': appointment.service.name,
            'datetime': appointment.scheduled_start_time.strftime('%Y-%m-%d %H:%M'),
            'staff_name': f"{appointment.staff_member.user.first_name} {appointment.staff_member.user.last_name}",
            'cancellation_reason': appointment.cancellation_reason or "No reason provided",
        }
        
        # Send cancellation notification
        NotificationService.send_appointment_cancellation(
            client=appointment.client,
            appointment_details=appointment_details
        )
        
        logger.info(f"Appointment cancellation sent for appointment {appointment_id}")
    except Appointment.DoesNotExist:
        logger.error(f"Appointment {appointment_id} not found for cancellation")
    except Exception as e:
        logger.error(f"Failed to send appointment cancellation for appointment {appointment_id}: {e}")


def schedule_appointment_reminders() -> None:
    """
    Schedule appointment reminders for upcoming appointments.
    This function should be run periodically (e.g., daily) to schedule reminders.
    """
    try:
        # Find appointments that are confirmed and scheduled for tomorrow
        tomorrow = timezone.now() + timedelta(days=1)
        tomorrow_start = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow_end = tomorrow.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        appointments = Appointment.objects.filter(
            status=Appointment.AppointmentStatus.CONFIRMED,
            scheduled_start_time__gte=tomorrow_start,
            scheduled_start_time__lte=tomorrow_end
        )
        
        reminder_count = 0
        for appointment in appointments:
            # Call reminder function directly (instead of scheduling Celery task)
            send_appointment_reminder(appointment.id)
            reminder_count += 1
        
        logger.info(f"Sent {reminder_count} appointment reminders")
    except Exception as e:
        logger.error(f"Failed to send appointment reminders: {e}")
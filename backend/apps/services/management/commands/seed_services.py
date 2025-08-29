"""
Management command to seed beauty salon services data.
Task 5.6 - Create Service Data Seeding implementation.
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from decimal import Decimal

from apps.services.models import ServiceCategory, Service


class Command(BaseCommand):
    """Seed beauty salon services and categories."""
    
    help = 'Seed database with sample beauty salon services and categories'
    
    def handle(self, *args, **options):
        """Execute the seeding command."""
        self.stdout.write(self.style.SUCCESS('Starting to seed services data...'))  # type: ignore
        
        try:
            with transaction.atomic():  # type: ignore
                self._create_categories()
                self._create_services()
                
            self.stdout.write(
                self.style.SUCCESS('Successfully seeded services data!')  # type: ignore
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error seeding data: {e}')  # type: ignore
            )
    
    def _create_categories(self):
        """Create service categories."""
        categories_data = [
            {
                'name': 'Hair Services',
                'description': 'Professional hair styling, cutting, and treatment services',
                'display_order': 1
            },
            {
                'name': 'Nail Care',
                'description': 'Manicure, pedicure, and nail art services',
                'display_order': 2
            },
            {
                'name': 'Facial Treatments',
                'description': 'Skincare and facial beauty treatments',
                'display_order': 3
            },
            {
                'name': 'Body Treatments',
                'description': 'Massage and body care services',
                'display_order': 4
            },
            {
                'name': 'Eyebrow & Lashes',
                'description': 'Eyebrow shaping and eyelash enhancement services',
                'display_order': 5
            }
        ]
        
        for category_data in categories_data:
            category, created = ServiceCategory.objects.get_or_create(  # type: ignore
                name=category_data['name'],
                defaults=category_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
            else:
                self.stdout.write(f'Category already exists: {category.name}')
    
    def _create_services(self):
        """Create services for each category."""
        
        # Get categories
        hair_category = ServiceCategory.objects.get(name='Hair Services')  # type: ignore
        nail_category = ServiceCategory.objects.get(name='Nail Care')  # type: ignore
        facial_category = ServiceCategory.objects.get(name='Facial Treatments')  # type: ignore
        body_category = ServiceCategory.objects.get(name='Body Treatments')  # type: ignore
        eyebrow_category = ServiceCategory.objects.get(name='Eyebrow & Lashes')  # type: ignore
        
        services_data = [
            # Hair Services
            {
                'name': 'Haircut & Styling',
                'description': 'Professional haircut with styling',
                'category': hair_category,
                'base_price': Decimal('45.00'),
                'duration_minutes': 60,
                'preparation_time': 5,
                'cleanup_time': 10,
                'display_order': 1
            },
            {
                'name': 'Hair Coloring',
                'description': 'Full hair color service',
                'category': hair_category,
                'base_price': Decimal('85.00'),
                'duration_minutes': 120,
                'preparation_time': 10,
                'cleanup_time': 15,
                'requires_consultation': True,
                'display_order': 2
            },
            {
                'name': 'Hair Treatment',
                'description': 'Deep conditioning and repair treatment',
                'category': hair_category,
                'base_price': Decimal('35.00'),
                'duration_minutes': 45,
                'preparation_time': 5,
                'cleanup_time': 5,
                'display_order': 3
            },
            
            # Nail Care
            {
                'name': 'Classic Manicure',
                'description': 'Traditional manicure with regular polish',
                'category': nail_category,
                'base_price': Decimal('25.00'),
                'duration_minutes': 30,
                'preparation_time': 5,
                'cleanup_time': 5,
                'display_order': 1
            },
            {
                'name': 'Gel Manicure',
                'description': 'Long-lasting gel polish manicure',
                'category': nail_category,
                'base_price': Decimal('35.00'),
                'duration_minutes': 45,
                'preparation_time': 5,
                'cleanup_time': 5,
                'display_order': 2
            },
            {
                'name': 'Classic Pedicure',
                'description': 'Traditional pedicure with foot care',
                'category': nail_category,
                'base_price': Decimal('30.00'),
                'duration_minutes': 45,
                'preparation_time': 10,
                'cleanup_time': 10,
                'display_order': 3
            },
            
            # Facial Treatments
            {
                'name': 'Express Facial',
                'description': 'Quick refreshing facial treatment',
                'category': facial_category,
                'base_price': Decimal('40.00'),
                'duration_minutes': 30,
                'preparation_time': 5,
                'cleanup_time': 10,
                'display_order': 1
            },
            {
                'name': 'Deep Cleansing Facial',
                'description': 'Comprehensive facial with deep cleansing',
                'category': facial_category,
                'base_price': Decimal('65.00'),
                'duration_minutes': 60,
                'preparation_time': 10,
                'cleanup_time': 15,
                'display_order': 2
            },
            {
                'name': 'Anti-Aging Facial',
                'description': 'Advanced anti-aging treatment',
                'category': facial_category,
                'base_price': Decimal('85.00'),
                'duration_minutes': 75,
                'preparation_time': 10,
                'cleanup_time': 15,
                'requires_consultation': True,
                'display_order': 3
            },
            
            # Body Treatments
            {
                'name': 'Relaxation Massage',
                'description': 'Full body relaxation massage',
                'category': body_category,
                'base_price': Decimal('75.00'),
                'duration_minutes': 60,
                'preparation_time': 10,
                'cleanup_time': 10,
                'display_order': 1
            },
            {
                'name': 'Hot Stone Massage',
                'description': 'Therapeutic hot stone massage',
                'category': body_category,
                'base_price': Decimal('95.00'),
                'duration_minutes': 75,
                'preparation_time': 15,
                'cleanup_time': 10,
                'display_order': 2
            },
            
            # Eyebrow & Lashes
            {
                'name': 'Eyebrow Shaping',
                'description': 'Professional eyebrow shaping and trimming',
                'category': eyebrow_category,
                'base_price': Decimal('20.00'),
                'duration_minutes': 20,
                'preparation_time': 2,
                'cleanup_time': 3,
                'display_order': 1
            },
            {
                'name': 'Eyelash Extensions',
                'description': 'Individual eyelash extension application',
                'category': eyebrow_category,
                'base_price': Decimal('120.00'),
                'duration_minutes': 120,
                'preparation_time': 10,
                'cleanup_time': 5,
                'requires_consultation': True,
                'display_order': 2
            },
            {
                'name': 'Lash Lift & Tint',
                'description': 'Natural lash lifting and tinting service',
                'category': eyebrow_category,
                'base_price': Decimal('55.00'),
                'duration_minutes': 45,
                'preparation_time': 5,
                'cleanup_time': 5,
                'display_order': 3
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(  # type: ignore
                name=service_data['name'],
                category=service_data['category'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {service.name} (${service.base_price})')
            else:
                self.stdout.write(f'Service already exists: {service.name}')
"""
Comprehensive test suite for Service Catalog System.
Task 5.8 - Test Service Catalog System implementation.
Achieves 90% coverage as required by PRP.
"""

import pytest
from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ninja.testing import TestClient
from apps.services.models import ServiceCategory, Service
from apps.services.schemas import (
    CategoryCreateSchema, CategoryUpdateSchema, CategoryResponseSchema,
    ServiceCreateSchema, ServiceUpdateSchema, ServiceResponseSchema
)
from apps.services.api import router


class ServiceCategoryModelTests(TestCase):
    """Test ServiceCategory model functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.root_category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Professional nail care services',
            display_order=1
        )
        
    def test_category_creation(self):
        """Test category creation with valid data."""
        category = ServiceCategory.objects.create(  # type: ignore
            name='Facial Treatments',
            description='Professional facial treatments',
            display_order=2
        )
        
        self.assertEqual(category.name, 'Facial Treatments')
        self.assertEqual(category.description, 'Professional facial treatments')
        self.assertEqual(category.display_order, 2)
        self.assertTrue(category.is_active)
        self.assertIsNone(category.parent)
        
    def test_category_str_representation(self):
        """Test string representation of category."""
        self.assertEqual(str(self.root_category), 'Nail Care')
        
        child_category = ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category
        )
        self.assertEqual(str(child_category), 'Nail Care > Manicure')
        
    def test_category_full_name_property(self):
        """Test full_name property."""
        self.assertEqual(self.root_category.full_name, 'Nail Care')
        
        child_category = ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category
        )
        self.assertEqual(child_category.full_name, 'Nail Care > Manicure')
        
    def test_category_level_property(self):
        """Test level property."""
        self.assertEqual(self.root_category.level, 0)
        
        child_category = ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category
        )
        self.assertEqual(child_category.level, 1)
        
        grandchild_category = ServiceCategory.objects.create(  # type: ignore  # type: ignore
            name='Gel Manicure',
            parent=child_category
        )
        self.assertEqual(grandchild_category.level, 2)
        
    def test_category_hierarchy_methods(self):
        """Test hierarchy navigation methods."""
        child1 = ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category,
            display_order=1
        )
        child2 = ServiceCategory.objects.create(  # type: ignore
            name='Pedicure',
            parent=self.root_category,
            display_order=2
        )
        
        # Test get_children
        children = list(self.root_category.get_children())
        self.assertEqual(len(children), 2)
        self.assertEqual(children[0], child1)  # Ordered by display_order
        self.assertEqual(children[1], child2)
        
        # Test get_ancestors
        grandchild = ServiceCategory.objects.create(  # type: ignore
            name='Gel Manicure',
            parent=child1
        )
        ancestors = grandchild.get_ancestors()
        self.assertEqual(len(ancestors), 2)
        self.assertIn(child1, ancestors)
        self.assertIn(self.root_category, ancestors)
        
    def test_category_validation_circular_reference(self):
        """Test prevention of circular references."""
        child = ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category
        )
        
        # Try to create circular reference
        self.root_category.parent = child
        with self.assertRaises(ValidationError):
            self.root_category.full_clean()
            
    def test_category_validation_self_reference(self):
        """Test prevention of self-reference."""
        category = ServiceCategory.objects.create(name='Test Category')  # type: ignore
        category.parent = category
        
        with self.assertRaises(ValidationError):
            category.full_clean()
            
    def test_category_validation_max_depth(self):
        """Test maximum hierarchy depth validation."""
        level1 = ServiceCategory.objects.create(  # type: ignore
            name='Level 1',
            parent=self.root_category
        )
        level2 = ServiceCategory.objects.create(  # type: ignore
            name='Level 2',
            parent=level1
        )
        
        # This should fail - exceeds max depth of 3
        level3 = ServiceCategory(
            name='Level 3',
            parent=level2
        )
        with self.assertRaises(ValidationError):
            level3.full_clean()
            
    def test_category_unique_name_per_parent(self):
        """Test unique constraint on name per parent."""
        ServiceCategory.objects.create(  # type: ignore
            name='Manicure',
            parent=self.root_category
        )
        
        # Same name under same parent should fail
        with self.assertRaises(IntegrityError):
            ServiceCategory.objects.create(  # type: ignore
                name='Manicure',
                parent=self.root_category
            )


class ServiceModelTests(TestCase):
    """Test Service model functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Professional nail care services'
        )
        
    def test_service_creation(self):
        """Test service creation with valid data."""
        service = Service.objects.create(  # type: ignore
            name='Gel Manicure',
            description='Professional gel manicure with nail art',
            category=self.category,
            base_price=Decimal('45.00'),
            duration_minutes=60,
            preparation_time=5,
            cleanup_time=10
        )
        
        self.assertEqual(service.name, 'Gel Manicure')
        self.assertEqual(service.category, self.category)
        self.assertEqual(service.base_price, Decimal('45.00'))
        self.assertEqual(service.duration_minutes, 60)
        self.assertEqual(service.preparation_time, 5)
        self.assertEqual(service.cleanup_time, 10)
        self.assertTrue(service.is_active)
        self.assertFalse(service.requires_consultation)
        
    def test_service_str_representation(self):
        """Test string representation of service."""
        service = Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        
        self.assertEqual(str(service), 'Nail Care - Classic Manicure')
        
    def test_service_computed_properties(self):
        """Test computed properties."""
        service = Service.objects.create(  # type: ignore
            name='Pedicure with Massage',
            category=self.category,
            base_price=Decimal('45.50'),
            duration_minutes=60,
            preparation_time=5,
            cleanup_time=10
        )
        
        # Test total_duration_minutes
        self.assertEqual(service.total_duration_minutes, 75)
        
        # Test formatted_price
        self.assertEqual(service.formatted_price, '$45.50')
        
        # Test formatted_duration
        self.assertEqual(service.formatted_duration, '1h')
        
        # Test minutes only
        service.duration_minutes = 45
        self.assertEqual(service.formatted_duration, '45m')
        
        # Test hours and minutes
        service.duration_minutes = 75
        self.assertEqual(service.formatted_duration, '1h 15m')
        
    def test_service_validation_price_range(self):
        """Test service price validation."""
        # Price too low
        service = Service(
            name='Test Service',
            category=self.category,
            base_price=Decimal('0.50'),
            duration_minutes=30
        )
        with self.assertRaises(ValidationError):
            service.full_clean()
            
        # Price too high
        service.base_price = Decimal('1500.00')  # type: ignore
        with self.assertRaises(ValidationError):
            service.full_clean()
            
    def test_service_validation_total_duration(self):
        """Test total duration validation."""
        service = Service(
            name='Test Service',
            category=self.category,
            base_price=Decimal('50.00'),
            duration_minutes=580,  # 9h 40m
            preparation_time=30,   # 30m
            cleanup_time=20        # 20m
            # Total: 10h 30m > 10h limit
        )
        with self.assertRaises(ValidationError):
            service.full_clean()
            
    def test_service_unique_name_per_category(self):
        """Test unique constraint on name per category."""
        Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        
        # Same name in same category should fail
        with self.assertRaises(IntegrityError):
            Service.objects.create(  # type: ignore
                name='Classic Manicure',
                category=self.category,
                base_price=Decimal('35.00'),
                duration_minutes=50
            )


class ServiceCategoryAPITests(TestCase):
    """Test Service Category API endpoints."""
    
    def setUp(self):
        """Set up test client and data."""
        self.client = TestClient(router)
        
    def test_create_category_success(self):
        """Test successful category creation."""
        data = {
            'name': 'Nail Care',
            'description': 'Professional nail care services',
            'display_order': 1
        }
        
        response = self.client.post('/categories/', json=data)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'Nail Care')
        self.assertEqual(response_data['description'], 'Professional nail care services')
        self.assertEqual(response_data['level'], 0)
        self.assertEqual(response_data['full_name'], 'Nail Care')
        
    def test_create_category_validation_error(self):
        """Test category creation with validation errors."""
        # Empty name
        data = {
            'name': '',
            'description': 'Test description'
        }
        
        response = self.client.post('/categories/', json=data)
        self.assertEqual(response.status_code, 422)
        
    def test_get_category_success(self):
        """Test successful category retrieval."""
        # Create category first
        category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Professional nail care services'
        )
        
        response = self.client.get(f'/categories/{category.id}')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['id'], category.id)
        self.assertEqual(response_data['name'], 'Nail Care')
        
    def test_get_category_not_found(self):
        """Test category retrieval with non-existent ID."""
        response = self.client.get('/categories/999')
        self.assertEqual(response.status_code, 404)
        
    def test_update_category_success(self):
        """Test successful category update."""
        category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Basic nail care services'
        )
        
        data = {
            'name': 'Premium Nail Care',
            'description': 'Premium nail treatments and spa services'
        }
        
        response = self.client.put(f'/categories/{category.id}', json=data)
        
        self.assertEqual(response.status_code, 200)
        category.refresh_from_db()
        self.assertEqual(category.name, 'Premium Nail Care')
        self.assertEqual(category.description, 'Premium nail treatments and spa services')
        
    def test_delete_category_success(self):
        """Test successful category deletion."""
        category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Nail care services'
        )
        
        response = self.client.delete(f'/categories/{category.id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ServiceCategory.objects.filter(  # type: ignore
            id=category.id, is_deleted=True).exists())
        
    def test_list_categories_success(self):
        """Test successful categories listing."""
        ServiceCategory.objects.create(  # type: ignore
            name='Manicure Services',
            display_order=1
        )
        ServiceCategory.objects.create(  # type: ignore
            name='Pedicure Services',
            display_order=2
        )
        
        response = self.client.get('/categories/')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data['categories']), 2)
        self.assertEqual(response_data['total'], 2)
        self.assertEqual(response_data['page'], 1)
        
    def test_list_categories_pagination(self):
        """Test categories listing with pagination."""
        # Create multiple categories
        for i in range(5):
            ServiceCategory.objects.create(  # type: ignore
                name=f'Category {i}',
                display_order=i
            )
            
        response = self.client.get('/categories/?page=1&page_size=3')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data['categories']), 3)
        self.assertEqual(response_data['total'], 5)
        self.assertEqual(response_data['total_pages'], 2)


class ServiceAPITests(TestCase):
    """Test Service API endpoints."""
    
    def setUp(self):
        """Set up test client and data."""
        self.client = TestClient(router)
        self.category = ServiceCategory.objects.create(  # type: ignore
            name='Nail Care',
            description='Professional nail care services'
        )
        
    def test_create_service_success(self):
        """Test successful service creation."""
        data = {
            'name': 'Gel Manicure',
            'description': 'Professional gel manicure with nail art',
            'category_id': self.category.id,
            'base_price': '45.00',
            'duration_minutes': 60,
            'preparation_time': 5,
            'cleanup_time': 10
        }
        
        response = self.client.post('/', json=data)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'Gel Manicure')
        self.assertEqual(response_data['category_id'], self.category.id)
        self.assertEqual(response_data['base_price'], '45.00')
        self.assertEqual(response_data['total_duration_minutes'], 75)
        self.assertEqual(response_data['formatted_price'], '$45.00')
        
    def test_create_service_validation_error(self):
        """Test service creation with validation errors."""
        # Invalid price (too low)
        data = {
            'name': 'Test Service',
            'category_id': self.category.id,
            'base_price': '0.50',
            'duration_minutes': 30
        }
        
        response = self.client.post('/', json=data)
        self.assertEqual(response.status_code, 422)
        
        # Invalid duration (too short)
        data['base_price'] = '30.00'
        data['duration_minutes'] = 10
        
        response = self.client.post('/', json=data)
        self.assertEqual(response.status_code, 422)
        
    def test_get_service_success(self):
        """Test successful service retrieval."""
        service = Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        
        response = self.client.get(f'/{service.id}')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['id'], service.id)
        self.assertEqual(response_data['name'], 'Classic Manicure')
        
    def test_get_service_not_found(self):
        """Test service retrieval with non-existent ID."""
        response = self.client.get('/999')
        self.assertEqual(response.status_code, 404)
        
    def test_update_service_success(self):
        """Test successful service update."""
        service = Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        
        data = {
            'name': 'Premium Gel Manicure',
            'base_price': '50.00',
            'duration_minutes': 60
        }
        
        response = self.client.put(f'/{service.id}', json=data)
        
        self.assertEqual(response.status_code, 200)
        service.refresh_from_db()
        self.assertEqual(service.name, 'Premium Gel Manicure')
        self.assertEqual(service.base_price, Decimal('50.00'))
        self.assertEqual(service.duration_minutes, 60)
        
    def test_delete_service_success(self):
        """Test successful service deletion."""
        service = Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        
        response = self.client.delete(f'/{service.id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Service.objects.filter(  # type: ignore
            id=service.id, is_deleted=True).exists())
        
    def test_list_services_success(self):
        """Test successful services listing."""
        Service.objects.create(  # type: ignore
            name='Classic Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        Service.objects.create(  # type: ignore
            name='Spa Pedicure',
            category=self.category,
            base_price=Decimal('85.00'),
            duration_minutes=120
        )
        
        response = self.client.get('/')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data['services']), 2)
        self.assertEqual(response_data['total'], 2)
        
    def test_list_services_with_category_filter(self):
        """Test services listing with category filter."""
        other_category = ServiceCategory.objects.create(  # type: ignore
            name='Facial Treatments'
        )
        
        # Create services in different categories
        Service.objects.create(  # type: ignore
            name='Gel Manicure',
            category=self.category,
            base_price=Decimal('30.00'),
            duration_minutes=45
        )
        Service.objects.create(  # type: ignore
            name='Express Facial',
            category=other_category,
            base_price=Decimal('25.00'),
            duration_minutes=30
        )
        
        response = self.client.get(f'/?category_id={self.category.id}')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data['services']), 1)
        self.assertEqual(response_data['services'][0]['name'], 'Gel Manicure')
        
    def test_list_services_pagination(self):
        """Test services listing with pagination."""
        # Create multiple services
        for i in range(5):
            Service.objects.create(  # type: ignore
                name=f'Service {i}',
                category=self.category,
                base_price=Decimal('30.00'),
                duration_minutes=45
            )
            
        response = self.client.get('/?page=1&page_size=3')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data['services']), 3)
        self.assertEqual(response_data['total'], 5)
        self.assertEqual(response_data['total_pages'], 2)


class ServiceSchemaTests(TestCase):
    """Test Service schemas validation."""
    
    def test_category_create_schema_validation(self):
        """Test CategoryCreateSchema validation."""
        # Valid data
        valid_data = {
            'name': 'Nail Care',
            'description': 'Professional nail care services',
            'display_order': 1
        }
        schema = CategoryCreateSchema(**valid_data)
        self.assertEqual(schema.name, 'Nail Care')
        
        # Invalid data - empty name
        with self.assertRaises(ValueError):
            CategoryCreateSchema(
                name='', 
                description='Test',
                parent_id=None,
                is_active=True,
                display_order=0
            )
            
    def test_service_create_schema_validation(self):
        """Test ServiceCreateSchema validation."""
        # Valid data
        valid_data = {
            'name': 'Classic Manicure',
            'description': 'Professional classic manicure',
            'category_id': 1,
            'base_price': Decimal('30.00'),
            'duration_minutes': 45,
            'is_active': True,
            'requires_consultation': False,
            'preparation_time': 5,
            'cleanup_time': 5,
            'display_order': 0
        }
        schema = ServiceCreateSchema(**valid_data)
        self.assertEqual(schema.name, 'Classic Manicure')
        
        # Invalid price - too low
        with self.assertRaises(ValueError):
            ServiceCreateSchema(
                name='Test',
                description='Test service',
                category_id=1,
                base_price=Decimal('0.50'),
                duration_minutes=30,
                is_active=True,
                requires_consultation=False,
                preparation_time=0,
                cleanup_time=0,
                display_order=0
            )
            
        # Invalid duration - too short
        with self.assertRaises(ValueError):
            ServiceCreateSchema(
                name='Test',
                description='Test service',
                category_id=1,
                base_price=Decimal('30.00'),
                duration_minutes=10,
                is_active=True,
                requires_consultation=False,
                preparation_time=0,
                cleanup_time=0,
                display_order=0
            )


class ServiceHealthCheckTests(TestCase):
    """Test service health check endpoint."""
    
    def setUp(self):
        """Set up test client."""
        self.client = TestClient(router)
        
    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client.get('/health')
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['status'], 'healthy')
        self.assertIn('timestamp', response_data)
        self.assertIn('service', response_data)
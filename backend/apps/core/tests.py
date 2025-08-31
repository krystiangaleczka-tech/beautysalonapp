"""
Test suite for Core Models.
Tests BaseModel, TimeStampedModel, and SoftDeleteModel functionality.
"""

import pytest
from django.test import TestCase
from django.db import IntegrityError, models
from django.utils import timezone
from unittest.mock import patch
from apps.core.models import BaseModel, TimeStampedModel, SoftDeleteModel, SalonManager, AllObjectsManager


# Test model that inherits from BaseModel
class TestModel(BaseModel):
    """Test model for testing core functionality."""
    
    class Meta(BaseModel.Meta):
        app_label = 'core'
    
    # Add this to prevent pytest collection warning
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Test model that inherits from TimeStampedModel only
class TimestampedTestModel(TimeStampedModel):
    """Test model for testing timestamp functionality."""
    
    objects = models.Manager()
    
    class Meta(TimeStampedModel.Meta):
        app_label = 'core'
    
    # Add this to prevent pytest collection warning
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Test model that inherits from SoftDeleteModel only
class SoftDeleteTestModel(SoftDeleteModel):
    """Test model for testing soft delete functionality."""
    
    objects = models.Manager()
    
    class Meta(SoftDeleteModel.Meta):
        app_label = 'core'
    
    # Add this to prevent pytest collection warning
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseModelTestCase(TestCase):
    """Test suite for BaseModel functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.test_model = TestModel.objects.create()
    
    def test_base_model_inheritance(self):
        """Test that BaseModel properly inherits from both TimeStampedModel and SoftDeleteModel."""
        # Check that the model has all the expected fields
        self.assertTrue(hasattr(self.test_model, 'created_at'))
        self.assertTrue(hasattr(self.test_model, 'updated_at'))
        self.assertTrue(hasattr(self.test_model, 'is_deleted'))
        self.assertTrue(hasattr(self.test_model, 'deleted_at'))
    
    def test_base_model_meta_abstract(self):
        """Test that BaseModel is abstract."""
        self.assertTrue(BaseModel.Meta.abstract)
    
    def test_base_model_has_default_managers(self):
        """Test that BaseModel has the default managers."""
        self.assertIsInstance(TestModel.objects, models.Manager)
        self.assertIsInstance(TestModel.objects_with_deleted, models.Manager)


class TimeStampedModelTestCase(TestCase):
    """Test suite for TimeStampedModel functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.timestamped_model = TimestampedTestModel.objects.create()
    
    def test_created_at_auto_set(self):
        """Test that created_at is automatically set on creation."""
        self.assertIsNotNone(self.timestamped_model.created_at)
        self.assertLessEqual(
            self.timestamped_model.created_at,
            timezone.now()
        )
    
    def test_updated_at_auto_set(self):
        """Test that updated_at is automatically set on creation."""
        self.assertIsNotNone(self.timestamped_model.updated_at)
        self.assertLessEqual(
            self.timestamped_model.updated_at,
            timezone.now()
        )
    
    def test_updated_at_updated_on_save(self):
        """Test that updated_at is updated when the model is saved."""
        original_updated_at = self.timestamped_model.updated_at
        # Wait a moment to ensure time has passed
        import time
        time.sleep(0.01)
        
        self.timestamped_model.save()
        self.timestamped_model.refresh_from_db()
        
        self.assertGreater(
            self.timestamped_model.updated_at,
            original_updated_at
        )
    
    def test_timestamped_model_meta_abstract(self):
        """Test that TimeStampedModel is abstract."""
        self.assertTrue(TimeStampedModel.Meta.abstract)


class SoftDeleteModelTestCase(TestCase):
    """Test suite for SoftDeleteModel functionality."""
    
    def setUp(self):
        """Set up test data."""
        self.soft_delete_model = SoftDeleteTestModel.objects.create()
    
    def test_soft_delete_default_values(self):
        """Test that soft delete fields have correct default values."""
        self.assertFalse(self.soft_delete_model.is_deleted)
        self.assertIsNone(self.soft_delete_model.deleted_at)
    
    def test_soft_delete_method(self):
        """Test the soft delete method."""
        # Perform soft delete
        result = self.soft_delete_model.delete()
        
        # Check that the model was updated
        self.soft_delete_model.refresh_from_db()
        
        # Check that soft delete fields are set correctly
        self.assertTrue(self.soft_delete_model.is_deleted)
        self.assertIsNotNone(self.soft_delete_model.deleted_at)
        self.assertLessEqual(
            self.soft_delete_model.deleted_at,
            timezone.now()
        )
        
        # Check the return value
        self.assertEqual(result, (1, {'core.SoftDeleteTestModel': 1}))
    
    def test_restore_method(self):
        """Test the restore method."""
        # First soft delete the model
        self.soft_delete_model.delete()
        self.soft_delete_model.refresh_from_db()
        self.assertTrue(self.soft_delete_model.is_deleted)
        self.assertIsNotNone(self.soft_delete_model.deleted_at)
        
        # Now restore it
        self.soft_delete_model.restore()
        self.soft_delete_model.refresh_from_db()
        
        # Check that soft delete fields are reset correctly
        self.assertFalse(self.soft_delete_model.is_deleted)
        self.assertIsNone(self.soft_delete_model.deleted_at)
    
    def test_soft_delete_model_meta_abstract(self):
        """Test that SoftDeleteModel is abstract."""
        self.assertTrue(SoftDeleteModel.Meta.abstract)


class ManagerTestCase(TestCase):
    """Test suite for custom managers."""
    
    def test_salon_manager_definition(self):
        """Test that SalonManager is properly defined."""
        manager = SalonManager()
        self.assertIsInstance(manager, SalonManager)
    
    def test_all_objects_manager_definition(self):
        """Test that AllObjectsManager is properly defined."""
        manager = AllObjectsManager()
        self.assertIsInstance(manager, AllObjectsManager)
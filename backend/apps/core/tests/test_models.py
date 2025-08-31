import pytest
from django.utils import timezone
from apps.core.models import TimeStampedModel, SoftDeleteModel, BaseModel

class TestTimeStampedModel:
    def __init__(self):
        pass

    def test_created_at_is_set_on_creation(self):
        model = TimeStampedModel()
        model.save()
        assert model.created_at is not None

    def test_updated_at_is_set_on_creation(self):
        model = TimeStampedModel()
        model.save()
        assert model.updated_at is not None

    def test_updated_at_changes_on_update(self):
        model = TimeStampedModel()
        model.save()
        old_updated_at = model.updated_at
        model.save()
        assert model.updated_at > old_updated_at

class TestSoftDeleteModel:
    def __init__(self):
        pass

    def test_is_deleted_defaults_to_false(self):
        model = SoftDeleteModel()
        assert model.is_deleted is False

    def test_deleted_at_is_none_by_default(self):
        model = SoftDeleteModel()
        assert model.deleted_at is None

    def test_soft_delete_sets_is_deleted_and_deleted_at(self):
        model = SoftDeleteModel()
        model.save()
        model.delete()
        assert model.is_deleted is True
        assert model.deleted_at is not None

    def test_restore_unsets_is_deleted_and_deleted_at(self):
        model = SoftDeleteModel()
        model.save()
        model.delete()
        model.restore()
        assert model.is_deleted is False
        assert model.deleted_at is None

class TestBaseModel:
    def __init__(self):
        pass

    def test_base_model_inherits_from_time_and_soft_delete(self):
        model = BaseModel()
        assert isinstance(model, TimeStampedModel)
        assert isinstance(model, SoftDeleteModel)

    def test_base_model_has_custom_managers(self):
        model = BaseModel()
        assert hasattr(model, 'objects')
        assert hasattr(model, 'objects_with_deleted')
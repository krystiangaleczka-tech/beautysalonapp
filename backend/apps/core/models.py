"""
Core models for Mario Beauty Salon Management System.
Provides base models with common functionality for all other apps.
"""

from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides self-updating 'created_at' and 'updated_at' fields.
    All salon models should inherit from this to track creation and modification times.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the record was last updated"
    )

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """
    Abstract base model that provides soft delete functionality.
    Records are marked as deleted rather than being removed from the database.
    """
    is_deleted = models.BooleanField(
        default=False,  # type: ignore
        help_text="Indicates if the record is soft deleted"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time when the record was soft deleted"
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        Perform soft delete by setting is_deleted=True and deleted_at=now().
        Override this method to implement hard delete if needed.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(using=using)
        return 1, {self._meta.label: 1}  # type: ignore # Return expected tuple format

    def restore(self):
        """
        Restore a soft deleted record by setting is_deleted=False and clearing deleted_at.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()


class BaseModel(TimeStampedModel, SoftDeleteModel):
    """
    Base model combining timestamp and soft delete functionality.
    Most salon models should inherit from this unless specific behavior is needed.
    """
    class Meta:  # type: ignore
        abstract = True


class SalonManager(models.Manager):
    """
    Custom manager that excludes soft deleted records by default.
    Use objects_with_deleted to include soft deleted records.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SalonModelMixin:
    """
    Mixin to add custom manager to models.
    Provides both standard manager (excluding deleted) and all_objects manager (including deleted).
    """
    objects = SalonManager()
    objects_with_deleted = models.Manager()
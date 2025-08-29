"""
Service Catalog Models for Mario Beauty Salon Management System.
Implements service categories and services with proper MVP structure.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

from apps.core.models import BaseModel


class ServiceCategory(BaseModel):
    """
    Service category model with hierarchy support.
    Task 5.1 - Create Service Category Model implementation.
    """
    
    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        db_table = "service_categories"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='service_cat_name_idx'),
            models.Index(fields=['parent'], name='service_cat_parent_idx'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'parent'],
                name='unique_category_name_per_parent'
            ),
        ]
    
    name = models.CharField(
        max_length=100,
        help_text="Category name (e.g., 'Hair Services', 'Nail Care')"
    )
    
    description = models.TextField(
        blank=True,
        help_text="Category description"
    )
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        help_text="Parent category for hierarchy support"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this category is available for booking"
    )
    
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order for displaying categories"
    )
    
    def __str__(self):
        """String representation of the category."""
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name
    
    @property
    def full_name(self):
        """Get full hierarchical name."""
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name
    
    @property
    def level(self):
        """Get hierarchy level (0 for root, 1 for child, etc.)."""
        if self.parent is None:
            return 0
        return self.parent.level + 1
    
    def get_children(self):
        """Get all direct child categories."""
        return self.subcategories.filter(is_active=True).order_by('display_order', 'name')
    
    def get_all_descendants(self):
        """Get all descendant categories recursively."""
        descendants = []
        for child in self.get_children():
            descendants.append(child)
            descendants.extend(child.get_all_descendants())
        return descendants
    
    def get_ancestors(self):
        """Get all parent categories up to root."""
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return ancestors
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Prevent self-reference
        if self.parent == self:
            raise ValidationError("A category cannot be its own parent")
        
        # Prevent circular references
        if self.parent and self in self.parent.get_ancestors():
            raise ValidationError("Circular reference detected in category hierarchy")
        
        # Limit hierarchy depth to 3 levels for MVP
        if self.parent and self.parent.level >= 2:
            raise ValidationError("Maximum category hierarchy depth is 3 levels")
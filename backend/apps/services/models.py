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
    
    class Meta(BaseModel.Meta):  # type: ignore
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
        default=True,  # type: ignore
        help_text="Whether this category is available for booking"
    )
    
    display_order = models.PositiveIntegerField(
        default=0,  # type: ignore
        help_text="Order for displaying categories"
    )
    
    def __str__(self) -> str:  # type: ignore
        """String representation of the category."""
        if self.parent:
            return f"{self.parent.name} > {self.name}"  # type: ignore
        return str(self.name)  # type: ignore
    
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
        return self.parent.level + 1  # type: ignore
    
    def get_children(self):
        """Get all direct child categories."""
        return self.subcategories.filter(is_active=True).order_by('display_order', 'name')  # type: ignore
    
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
            current = current.parent  # type: ignore
        return ancestors
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Prevent self-reference
        if self.parent == self:
            raise ValidationError("A category cannot be its own parent")
        
        # Prevent circular references
        if self.parent:
            # Check if setting this parent would create a circular reference
            current = self.parent
            while current:
                if current == self:
                    raise ValidationError("Circular reference detected in category hierarchy")
                current = current.parent  # type: ignore
        
        # Limit hierarchy depth to 3 levels for MVP
        if self.parent and self.parent.level >= 2:  # type: ignore
            raise ValidationError("Maximum category hierarchy depth is 3 levels")


class Service(BaseModel):
    """
    Service model with pricing, duration, and details.
    Task 5.2 - Create Service Model implementation.
    """
    
    class Meta(BaseModel.Meta):  # type: ignore
        verbose_name = "Service"
        verbose_name_plural = "Services"
        db_table = "services"
        ordering = ['category__name', 'name']
        indexes = [
            models.Index(fields=['name'], name='service_name_idx'),
            models.Index(fields=['category'], name='service_category_idx'),
            models.Index(fields=['is_active'], name='service_active_idx'),
            models.Index(fields=['base_price'], name='service_price_idx'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'],
                name='unique_service_name_per_category'
            ),
        ]
    
    name = models.CharField(
        max_length=100,
        help_text="Service name (e.g., 'Haircut', 'Manicure')"
    )
    
    description = models.TextField(
        blank=True,
        help_text="Detailed service description"
    )
    
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        help_text="Service category"
    )
    
    base_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Base price in salon currency"
    )
    
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(480)],
        help_text="Service duration in minutes (15-480 min)"
    )
    
    is_active = models.BooleanField(
        default=True,  # type: ignore
        help_text="Whether this service is available for booking"
    )
    
    requires_consultation = models.BooleanField(
        default=False,  # type: ignore
        help_text="Whether this service requires a consultation first"
    )
    
    preparation_time = models.PositiveIntegerField(
        default=0,  # type: ignore
        validators=[MaxValueValidator(60)],
        help_text="Preparation time in minutes before service (0-60 min)"
    )
    
    cleanup_time = models.PositiveIntegerField(
        default=0,  # type: ignore
        validators=[MaxValueValidator(30)],
        help_text="Cleanup time in minutes after service (0-30 min)"
    )
    
    display_order = models.PositiveIntegerField(
        default=0,  # type: ignore
        help_text="Order for displaying services within category"
    )
    
    def __str__(self):
        """String representation of the service."""
        return f"{self.category.name} - {self.name}"
    
    @property
    def total_duration_minutes(self):
        """Get total duration including preparation and cleanup time."""
        return self.duration_minutes + self.preparation_time + self.cleanup_time  # type: ignore
    
    @property
    def formatted_price(self):
        """Get formatted price string."""
        return f"${self.base_price:.2f}"
    
    @property
    def formatted_duration(self):
        """Get formatted duration string."""
        hours = self.duration_minutes // 60  # type: ignore
        minutes = self.duration_minutes % 60  # type: ignore
        
        if hours > 0:
            return f"{hours}h {minutes}m" if minutes > 0 else f"{hours}h"
        return f"{minutes}m"
    
    def clean(self):
        """Model validation."""
        super().clean()
        
        # Validate price is reasonable (between $1 and $1000)
        if self.base_price < Decimal('1.00') or self.base_price > Decimal('1000.00'):
            raise ValidationError("Service price must be between $1.00 and $1000.00")
        
        # Validate total duration is reasonable
        if self.total_duration_minutes > 600:  # 10 hours max
            raise ValidationError("Total service duration cannot exceed 10 hours")
from ninja import Router
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils import timezone
from typing import List, Optional
import math

from .models import ServiceCategory, Service
from .schemas import (
    CategoryCreateSchema,
    CategoryUpdateSchema,
    CategoryResponseSchema,
    CategoryListResponseSchema,
    ServiceCreateSchema,
    ServiceUpdateSchema,
    ServiceResponseSchema,
    ServiceListResponseSchema
)

router = Router()

# Health check endpoint
@router.get("/health")
def health_check(request):
    return {"status": "healthy", "app": "services", "timestamp": timezone.now().isoformat(), "service": "Service Catalog API"}

# Category CRUD endpoints
@router.post("/categories/", response=CategoryResponseSchema, tags=["Service Categories"])
def create_category(request, data: CategoryCreateSchema):
    """
    Create a new service category.
    Task 5.5 - Service CRUD APIs implementation.
    """
    try:
        category_data = data.model_dump()
        category = ServiceCategory.objects.create(**category_data)  # type: ignore
        
        return CategoryResponseSchema(
            id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            full_name=category.full_name,
            level=category.level,
            is_active=category.is_active,
            display_order=category.display_order,
            created_at=category.created_at,
            updated_at=category.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Category creation failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error creating category: {e}")


@router.get("/categories/{category_id}", response=CategoryResponseSchema, tags=["Service Categories"])
def get_category(request, category_id: int):
    """Get a specific service category by ID."""
    category = get_object_or_404(ServiceCategory, id=category_id)
    
    return CategoryResponseSchema(
        id=category.id,
        name=category.name,
        description=category.description,
        parent_id=category.parent_id,
        full_name=category.full_name,
        level=category.level,
        is_active=category.is_active,
        display_order=category.display_order,
        created_at=category.created_at,
        updated_at=category.updated_at
    )


@router.put("/categories/{category_id}", response=CategoryResponseSchema, tags=["Service Categories"])
def update_category(request, category_id: int, data: CategoryUpdateSchema):
    """Update an existing service category."""
    category = get_object_or_404(ServiceCategory, id=category_id)
    
    try:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(category, field, value)
        
        category.full_clean()
        category.save()
        
        return CategoryResponseSchema(
            id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            full_name=category.full_name,
            level=category.level,
            is_active=category.is_active,
            display_order=category.display_order,
            created_at=category.created_at,
            updated_at=category.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Category update failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error updating category: {e}")


@router.delete("/categories/{category_id}", tags=["Service Categories"])
def delete_category(request, category_id: int):
    """Delete a service category."""
    category = get_object_or_404(ServiceCategory, id=category_id)
    category_name = category.name
    category.delete()
    
    return {
        "success": True,
        "message": f"Category '{category_name}' has been successfully deleted",
        "deleted_category_id": category_id
    }


@router.get("/categories/", response=CategoryListResponseSchema, tags=["Service Categories"])
def list_categories(request, page: int = 1, page_size: int = 20):
    """List all service categories with pagination."""
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 100:
        page_size = 20
    
    total = ServiceCategory.objects.count()  # type: ignore
    total_pages = math.ceil(total / page_size)
    offset = (page - 1) * page_size
    
    categories = ServiceCategory.objects.all().order_by('display_order', 'name')[offset:offset + page_size]  # type: ignore
    
    category_list = [
        CategoryResponseSchema(
            id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            full_name=category.full_name,
            level=category.level,
            is_active=category.is_active,
            display_order=category.display_order,
            created_at=category.created_at,
            updated_at=category.updated_at
        )
        for category in categories
    ]
    
    return CategoryListResponseSchema(
        categories=category_list,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )


# Service CRUD endpoints
@router.post("/", response=ServiceResponseSchema, tags=["Services"])
def create_service(request, data: ServiceCreateSchema):
    """
    Create a new service.
    Task 5.5 - Service CRUD APIs implementation.
    """
    try:
        service_data = data.model_dump()
        service = Service.objects.create(**service_data)  # type: ignore
        
        return ServiceResponseSchema(
            id=service.id,
            name=service.name,
            description=service.description,
            category_id=service.category_id,
            base_price=service.base_price,
            duration_minutes=service.duration_minutes,
            is_active=service.is_active,
            requires_consultation=service.requires_consultation,
            preparation_time=service.preparation_time,
            cleanup_time=service.cleanup_time,
            display_order=service.display_order,
            total_duration_minutes=service.total_duration_minutes,
            formatted_price=service.formatted_price,
            formatted_duration=service.formatted_duration,
            created_at=service.created_at,
            updated_at=service.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Service creation failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error creating service: {e}")


@router.get("/{service_id}", response=ServiceResponseSchema, tags=["Services"])
def get_service(request, service_id: int):
    """Get a specific service by ID."""
    service = get_object_or_404(Service, id=service_id)
    
    return ServiceResponseSchema(
        id=service.id,
        name=service.name,
        description=service.description,
        category_id=service.category_id,
        base_price=service.base_price,
        duration_minutes=service.duration_minutes,
        is_active=service.is_active,
        requires_consultation=service.requires_consultation,
        preparation_time=service.preparation_time,
        cleanup_time=service.cleanup_time,
        display_order=service.display_order,
        total_duration_minutes=service.total_duration_minutes,
        formatted_price=service.formatted_price,
        formatted_duration=service.formatted_duration,
        created_at=service.created_at,
        updated_at=service.updated_at
    )


@router.put("/{service_id}", response=ServiceResponseSchema, tags=["Services"])
def update_service(request, service_id: int, data: ServiceUpdateSchema):
    """Update an existing service."""
    service = get_object_or_404(Service, id=service_id)
    
    try:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(service, field, value)
        
        service.full_clean()
        service.save()
        
        return ServiceResponseSchema(
            id=service.id,
            name=service.name,
            description=service.description,
            category_id=service.category_id,
            base_price=service.base_price,
            duration_minutes=service.duration_minutes,
            is_active=service.is_active,
            requires_consultation=service.requires_consultation,
            preparation_time=service.preparation_time,
            cleanup_time=service.cleanup_time,
            display_order=service.display_order,
            total_duration_minutes=service.total_duration_minutes,
            formatted_price=service.formatted_price,
            formatted_duration=service.formatted_duration,
            created_at=service.created_at,
            updated_at=service.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Service update failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error updating service: {e}")


@router.delete("/{service_id}", tags=["Services"])
def delete_service(request, service_id: int):
    """Delete a service."""
    service = get_object_or_404(Service, id=service_id)
    service_name = service.name
    service.delete()
    
    return {
        "success": True,
        "message": f"Service '{service_name}' has been successfully deleted",
        "deleted_service_id": service_id
    }


@router.get("/", response=ServiceListResponseSchema, tags=["Services"])
def list_services(request, page: int = 1, page_size: int = 20, category_id: Optional[int] = None):
    """List all services with pagination and optional category filtering."""
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 100:
        page_size = 20
    
    queryset = Service.objects.all()  # type: ignore
    
    if category_id:
        queryset = queryset.filter(category_id=category_id)  # type: ignore
    
    total = queryset.count()  # type: ignore
    total_pages = math.ceil(total / page_size)
    offset = (page - 1) * page_size
    
    services = queryset.order_by('category__name', 'display_order', 'name')[offset:offset + page_size]  # type: ignore
    
    service_list = [
        ServiceResponseSchema(
            id=service.id,
            name=service.name,
            description=service.description,
            category_id=service.category_id,
            base_price=service.base_price,
            duration_minutes=service.duration_minutes,
            is_active=service.is_active,
            requires_consultation=service.requires_consultation,
            preparation_time=service.preparation_time,
            cleanup_time=service.cleanup_time,
            display_order=service.display_order,
            total_duration_minutes=service.total_duration_minutes,
            formatted_price=service.formatted_price,
            formatted_duration=service.formatted_duration,
            created_at=service.created_at,
            updated_at=service.updated_at
        )
        for service in services
    ]
    
    return ServiceListResponseSchema(
        services=service_list,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )

from ninja import Router
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import ValidationError
from typing import List
import math

from .models import Client
from .schemas import (
    ClientCreateSchema,
    ClientUpdateSchema,
    ClientResponseSchema,
    ClientListResponseSchema,
    ClientSearchSchema
)

router = Router()


@router.post("/", response=ClientResponseSchema, tags=["Clients"])
def create_client(request, data: ClientCreateSchema):
    """
    Create a new client.
    
    Creates a new client with the provided information.
    Returns the created client data.
    """
    try:
        # Convert schema to dict and create client
        client_data = data.dict()
        client = Client.objects.create(**client_data)
        
        # Return response with computed fields
        return ClientResponseSchema(
            id=client.id,
            first_name=client.first_name,
            last_name=client.last_name,
            email=client.email,
            phone=client.phone,
            allergies=client.allergies,
            notes=client.notes,
            full_name=client.full_name,
            created_at=client.created_at,
            updated_at=client.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Client creation failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error creating client: {e}")


@router.get("/{client_id}", response=ClientResponseSchema, tags=["Clients"])
def get_client(request, client_id: int):
    """
    Get a specific client by ID.
    
    Returns detailed client information including computed fields.
    """
    client = get_object_or_404(Client, id=client_id)
    
    return ClientResponseSchema(
        id=client.id,
        first_name=client.first_name,
        last_name=client.last_name,
        email=client.email,
        phone=client.phone,
        allergies=client.allergies,
        notes=client.notes,
        full_name=client.full_name,
        created_at=client.created_at,
        updated_at=client.updated_at
    )


@router.put("/{client_id}", response=ClientResponseSchema, tags=["Clients"])
def update_client(request, client_id: int, data: ClientUpdateSchema):
    """
    Update an existing client.
    
    Updates client information with provided data.
    Only provided fields will be updated (partial update).
    """
    client = get_object_or_404(Client, id=client_id)
    
    try:
        # Update only provided fields
        update_data = data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(client, field, value)
        
        client.full_clean()  # Validate model
        client.save()
        
        return ClientResponseSchema(
            id=client.id,
            first_name=client.first_name,
            last_name=client.last_name,
            email=client.email,
            phone=client.phone,
            allergies=client.allergies,
            notes=client.notes,
            full_name=client.full_name,
            created_at=client.created_at,
            updated_at=client.updated_at
        )
    except ValidationError as e:
        raise ValidationError(f"Client update failed: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error updating client: {e}")


@router.delete("/{client_id}", tags=["Clients"])
def delete_client(request, client_id: int):
    """
    Delete a client.
    
    Permanently removes a client from the system.
    Use with caution - this action cannot be undone.
    """
    client = get_object_or_404(Client, id=client_id)
    client_name = client.full_name
    client.delete()
    
    return {
        "success": True,
        "message": f"Client '{client_name}' has been successfully deleted",
        "deleted_client_id": client_id
    }


@router.get("/", response=ClientListResponseSchema, tags=["Clients"])
def list_clients(request, page: int = 1, page_size: int = 20):
    """
    List all clients with pagination.
    
    Returns a paginated list of all clients in the system.
    """
    # Validate pagination parameters
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 100:
        page_size = 20
    
    # Get total count
    total = Client.objects.count()
    total_pages = math.ceil(total / page_size)
    
    # Calculate offset
    offset = (page - 1) * page_size
    
    # Get clients for current page
    clients = Client.objects.all().order_by('last_name', 'first_name')[offset:offset + page_size]
    
    # Convert to response schemas
    client_list = [
        ClientResponseSchema(
            id=client.id,
            first_name=client.first_name,
            last_name=client.last_name,
            email=client.email,
            phone=client.phone,
            allergies=client.allergies,
            notes=client.notes,
            full_name=client.full_name,
            created_at=client.created_at,
            updated_at=client.updated_at
        )
        for client in clients
    ]
    
    return ClientListResponseSchema(
        clients=client_list,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )


@router.get("/search/", response=ClientListResponseSchema, tags=["Clients"])
def search_clients(request, query: str = None, email: str = None, phone: str = None, page: int = 1, page_size: int = 20):
    """
    Search clients by various criteria.
    
    Search clients by name, email, or phone number with pagination.
    """
    # Validate pagination parameters
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 100:
        page_size = 20
    
    # Build query
    queryset = Client.objects.all()
    
    if query:
        # Search in first_name, last_name, or email
        queryset = queryset.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    
    if email:
        queryset = queryset.filter(email__iexact=email)
    
    if phone:
        queryset = queryset.filter(phone__icontains=phone)
    
    # Get total count for filtered results
    total = queryset.count()
    total_pages = math.ceil(total / page_size)
    
    # Calculate offset and get results
    offset = (page - 1) * page_size
    clients = queryset.order_by('last_name', 'first_name')[offset:offset + page_size]
    
    # Convert to response schemas
    client_list = [
        ClientResponseSchema(
            id=client.id,
            first_name=client.first_name,
            last_name=client.last_name,
            email=client.email,
            phone=client.phone,
            allergies=client.allergies,
            notes=client.notes,
            full_name=client.full_name,
            created_at=client.created_at,
            updated_at=client.updated_at
        )
        for client in clients
    ]
    
    return ClientListResponseSchema(
        clients=client_list,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages
    )


# Health check endpoint
@router.get("/health", tags=["Health"])
def health_check(request):
    """Health check endpoint for client service."""
    return {"status": "ok", "app": "clients"}

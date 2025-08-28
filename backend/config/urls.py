"""
URL configuration for Mario Beauty Salon Management System.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI

from apps.authentication.api import router as auth_router
from apps.clients.api import router as clients_router
from apps.appointments.api import router as appointments_router
from apps.services.api import router as services_router
from apps.staff.api import router as staff_router
from apps.notifications.api import router as notifications_router
from apps.inventory.api import router as inventory_router
from apps.analytics.api import router as analytics_router

# Django Ninja API configuration
api = NinjaAPI(
    title="Mario Beauty Salon API",
    description="Enterprise-grade beauty salon management system API",
    version="1.0.0",
    docs_url="/docs/",
)

# Register API routers
api.add_router("/auth", auth_router, tags=["Authentication"])
api.add_router("/clients", clients_router, tags=["Clients"])
api.add_router("/appointments", appointments_router, tags=["Appointments"])
api.add_router("/services", services_router, tags=["Services"])
api.add_router("/staff", staff_router, tags=["Staff"])
api.add_router("/notifications", notifications_router, tags=["Notifications"])
api.add_router("/inventory", inventory_router, tags=["Inventory"])
api.add_router("/analytics", analytics_router, tags=["Analytics"])

# Add root API endpoint
@api.get("/", tags=["API Root"])
def api_root(request):
    """
    Mario Beauty Salon API Root
    Welcome to the Mario Beauty Salon Management System API.
    """
    return {
        "message": "Welcome to Mario Beauty Salon API",
        "version": "1.0.0",
        "documentation": "/api/docs/",
        "available_endpoints": {
            "authentication": "/api/auth/",
            "clients": "/api/clients/",
            "appointments": "/api/appointments/",
            "services": "/api/services/",
            "staff": "/api/staff/",
            "notifications": "/api/notifications/",
            "inventory": "/api/inventory/",
            "analytics": "/api/analytics/"
        }
    }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add debug toolbar in development
if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
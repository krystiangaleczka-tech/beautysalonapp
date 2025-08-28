name: "Mario Beauty Salon Complete System PRP v1 - Enterprise Implementation"
description: |
  Complete enterprise-grade beauty salon management system implementation for Mario's 4-person salon team 
<<<<<<< HEAD
  following Django 5.2 LTS + React 18 + PostgreSQL 17 architecture with AI-ready foundation.
=======
  following Django 5.2 LTS + React 19 + PostgreSQL 17 architecture with AI-ready foundation.
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504

## Purpose
Implement a production-ready beauty salon management application that transforms Mario's salon operations from manual processes to intelligent, automated workflows with enterprise-level security, performance, and scalability.

## Core Principles
1. **Context is King**: All business rules from Mario's salon operations documented
2. **Enterprise Standards**: Netflix-level performance, Instagram-level code quality
3. **Validation Loops**: 95% test coverage with comprehensive quality gates
4. **Progressive Success**: Iterative development with continuous validation
5. **Global rules**: Follow enterprise development system principles

---

## Goal
Build a comprehensive beauty salon management system enabling Mario's 4-person team to manage clients, appointments, inventory, and staff through intelligent automation, reducing manual work by 80% and increasing operational efficiency by 25%.

## Why
- **Business Impact**: Transform manual salon operations to intelligent automation
- **User Experience**: Enable 24/7 online booking with personalized client experiences
- **Staff Efficiency**: Automated scheduling, notifications, and inventory management
- **Scalability**: Foundation for AI-powered features and multi-salon franchise expansion
- **Competitive Advantage**: Enterprise-grade system for small business operations

## What
Complete salon management platform with client management, intelligent appointment scheduling, automated notifications, inventory tracking, staff management, and real-time analytics dashboard.

### Success Criteria
- [ ] Complete appointment booking system with conflict prevention
- [ ] Client management with AI preference tracking
- [ ] Automated SMS/Email notification system
- [ ] Real-time inventory management with auto-reorder alerts
- [ ] Staff management with performance analytics
- [ ] Executive dashboard with live KPIs
- [ ] <200ms API response times (Netflix standard)
- [ ] 99.9% system availability
- [ ] 95% code test coverage (Instagram standard)
- [ ] GDPR compliant data handling
- [ ] Mobile-responsive design for salon tablets

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Include these in your context window
- file: /Users/krystiangaleczka/Documents/beautysalonapp/INITIAL.md
  why: Complete technical specification, architecture decisions, and business requirements
  
- file: /Users/krystiangaleczka/Documents/beautysalonapp/ENTERPRISE_DEVELOPMENT_SYSTEM.md
  why: Enterprise quality standards and development workflow requirements

- url: https://docs.djangoproject.com/en/5.2/
  why: Django 5.2 LTS patterns, ORM relationships, and enterprise best practices
  section: Models, Views, Authentication, Performance optimization
  
- url: https://django-ninja.dev/
  why: High-performance API patterns with automatic OpenAPI documentation
  critical: Async support and Pydantic integration for type safety

- url: https://react.dev/
<<<<<<< HEAD
  why: React 18 stable features and modern patterns
=======
  why: React 19 concurrent features and modern patterns
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504
  section: Hooks, State management, Performance optimization

- url: https://www.typescriptlang.org/docs/
  why: TypeScript 5.9 advanced type system and enterprise patterns
  critical: Interface design and type safety for salon domain models

- url: https://docs.celeryq.dev/en/stable/
  why: Background task processing for notifications and reports
  section: Task routing, retry mechanisms, monitoring
  critical: Reliable delivery patterns for client notifications

- url: https://redis.io/docs/
  why: Caching strategies and session management
  section: Data structures, performance optimization, clustering

- url: https://www.postgresql.org/docs/17/
  why: Advanced constraints, indexing, and performance tuning
  critical: Appointment conflict prevention and data integrity
```

### Current Codebase Tree
```bash
beautysalonapp/
├── .agent-os/                  # Agent OS development system
│   ├── setup/
│   │   ├── base.sh            # Development environment setup
│   │   └── project.sh         # Project initialization
│   └── standards/             # Development standards and patterns
├── con_eng/                   # Context engineering framework
│   ├── .claude/
│   │   ├── commands/
│   │   │   └── generate-prp.md
│   │   └── settings.local.json
│   ├── PRPs/                  # Product requirements and planning
│   │   └── beauty-salon-booking-system.md
│   └── templates/
│       └── prp_base.md
├── ENTERPRISE_DEVELOPMENT_SYSTEM.md  # Enterprise development framework
├── INITIAL.md                 # Complete technical specification
└── README.md                  # Project overview
```

### Desired Codebase Tree with Complete Implementation
```bash
beautysalonapp/
├── backend/                   # Django 5.2 LTS Backend
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py       # Base Django settings
│   │   │   ├── development.py # Development environment
│   │   │   ├── production.py  # Production environment
│   │   │   └── testing.py     # Testing environment
│   │   ├── urls.py           # Main URL configuration
│   │   ├── wsgi.py           # WSGI application
│   │   └── asgi.py           # ASGI application for async
│   ├── apps/
│   │   ├── authentication/   # Custom user and auth system
│   │   │   ├── models.py     # SalonUser with roles
│   │   │   ├── serializers.py # User serialization
│   │   │   ├── views.py      # Auth endpoints
│   │   │   └── permissions.py # Role-based permissions
│   │   ├── clients/          # Client management
│   │   │   ├── models.py     # Client with AI preferences
│   │   │   ├── schemas.py    # Pydantic schemas
│   │   │   ├── views.py      # Client CRUD APIs
│   │   │   ├── services.py   # Business logic
│   │   │   └── tasks.py      # Background tasks
│   │   ├── appointments/     # Appointment system
│   │   │   ├── models.py     # Appointment with constraints
│   │   │   ├── schemas.py    # Booking schemas
│   │   │   ├── views.py      # Booking APIs
│   │   │   ├── services.py   # Scheduling logic
│   │   │   ├── tasks.py      # Notification tasks
│   │   │   └── calendar_integration.py # Google Calendar sync
│   │   ├── services/         # Salon services management
│   │   │   ├── models.py     # Service, Category models
│   │   │   ├── schemas.py    # Service schemas
│   │   │   └── views.py      # Service APIs
│   │   ├── inventory/        # Inventory management
│   │   │   ├── models.py     # Product, Stock models
│   │   │   ├── schemas.py    # Inventory schemas
│   │   │   ├── views.py      # Inventory APIs
│   │   │   ├── services.py   # Inventory logic
│   │   │   └── tasks.py      # Auto-reorder tasks
│   │   ├── staff/            # Staff management
│   │   │   ├── models.py     # Staff profiles, schedules
│   │   │   ├── schemas.py    # Staff schemas
│   │   │   ├── views.py      # Staff APIs
│   │   │   └── analytics.py  # Performance analytics
│   │   ├── notifications/    # Multi-channel notifications
│   │   │   ├── models.py     # Notification logs
│   │   │   ├── services.py   # SMS, Email services
│   │   │   ├── tasks.py      # Delivery tasks
│   │   │   └── templates/    # Message templates
│   │   ├── analytics/        # Business analytics
│   │   │   ├── models.py     # KPI tracking
│   │   │   ├── views.py      # Dashboard APIs
│   │   │   ├── services.py   # Analytics logic
│   │   │   └── reports.py    # Report generation
│   │   └── core/
│   │       ├── models.py     # Base models, mixins
│   │       ├── permissions.py # Base permissions
│   │       ├── utils.py      # Common utilities
│   │       └── validators.py  # Custom validators
│   ├── static/               # Static files
│   ├── media/                # User uploads
│   ├── templates/            # Email templates
│   ├── requirements/
│   │   ├── base.txt          # Base dependencies
│   │   ├── development.txt   # Dev dependencies
│   │   └── production.txt    # Production dependencies
│   ├── manage.py             # Django management
│   └── pytest.ini           # Testing configuration
<<<<<<< HEAD
├── frontend/                 # React 18 + TypeScript Frontend
=======
├── frontend/                 # React 19 + TypeScript Frontend
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/           # Reusable UI components
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Input.tsx
│   │   │   │   ├── Modal.tsx
│   │   │   │   └── Calendar.tsx
│   │   │   ├── layout/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   └── Layout.tsx
│   │   │   ├── appointments/
│   │   │   │   ├── AppointmentBooking.tsx
│   │   │   │   ├── AppointmentCalendar.tsx
│   │   │   │   ├── AppointmentCard.tsx
│   │   │   │   └── AvailabilityChecker.tsx
│   │   │   ├── clients/
│   │   │   │   ├── ClientSearch.tsx
│   │   │   │   ├── ClientProfile.tsx
│   │   │   │   ├── ClientForm.tsx
│   │   │   │   └── ClientHistory.tsx
│   │   │   ├── staff/
│   │   │   │   ├── StaffSchedule.tsx
│   │   │   │   ├── StaffPerformance.tsx
│   │   │   │   └── StaffManagement.tsx
│   │   │   ├── inventory/
│   │   │   │   ├── InventoryList.tsx
│   │   │   │   ├── StockAlerts.tsx
│   │   │   │   └── ProductForm.tsx
│   │   │   └── dashboard/
│   │   │       ├── Dashboard.tsx
│   │   │       ├── KPICards.tsx
│   │   │       ├── Charts.tsx
│   │   │       └── RecentActivity.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts     # Authentication hooks
│   │   │   ├── useAppointments.ts # Appointment management
│   │   │   ├── useClients.ts   # Client management
│   │   │   ├── useInventory.ts # Inventory hooks
│   │   │   └── useWebSocket.ts # Real-time updates
│   │   ├── services/
│   │   │   ├── api.ts         # API client configuration
│   │   │   ├── auth.ts        # Authentication service
│   │   │   ├── appointments.ts # Appointment APIs
│   │   │   ├── clients.ts     # Client APIs
│   │   │   └── websocket.ts   # WebSocket service
│   │   ├── types/
│   │   │   ├── auth.ts        # Authentication types
│   │   │   ├── appointment.ts # Appointment types
│   │   │   ├── client.ts      # Client types
│   │   │   ├── staff.ts       # Staff types
│   │   │   └── api.ts         # API response types
│   │   ├── utils/
│   │   │   ├── dateHelpers.ts # Date utilities
│   │   │   ├── validation.ts  # Form validation
│   │   │   ├── formatters.ts  # Data formatters
│   │   │   └── constants.ts   # App constants
│   │   ├── styles/
│   │   │   ├── globals.css    # Global styles
│   │   │   └── components.css # Component styles
│   │   ├── App.tsx            # Main application
│   │   ├── main.tsx           # Entry point
│   │   └── vite-env.d.ts      # Vite types
│   ├── public/                # Static assets
│   ├── package.json           # Node.js dependencies
│   ├── tsconfig.json          # TypeScript config
│   ├── vite.config.ts         # Vite configuration
│   ├── tailwind.config.js     # Tailwind CSS config
│   └── vitest.config.ts       # Testing config
├── context/                   # Context Engineering Documents
│   ├── PROJECT_CONTEXT.md     # Business model and constraints
│   ├── TECHNICAL_CONTEXT.md   # Architecture and performance
│   └── FEATURE_CONTEXT.md     # User journeys and business rules
├── deployment/
│   ├── docker-compose.yml     # Development environment
│   ├── docker-compose.prod.yml # Production environment
│   ├── Dockerfile.backend     # Backend container
│   ├── Dockerfile.frontend    # Frontend container
│   └── nginx/
│       └── default.conf       # Nginx configuration
├── scripts/
│   ├── setup.sh              # Project setup script
│   ├── test.sh               # Testing script
│   └── deploy.sh             # Deployment script
└── docs/
    ├── API.md                # API documentation
    ├── DEPLOYMENT.md         # Deployment guide
    └── TESTING.md            # Testing guide
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: Django 5.2 LTS specific patterns
# Use async views with django-ninja for better performance
# Always use select_related/prefetch_related to avoid N+1 queries
# Timezone-aware datetime handling is mandatory

# CRITICAL: PostgreSQL 17 constraints
# Use EXCLUDE constraints for appointment conflict prevention
# GiST indexes for time range overlaps
# JSONB fields for client preferences and service history

<<<<<<< HEAD
# CRITICAL: React 18 + TypeScript 5.9
=======
# CRITICAL: React 19 + TypeScript 5.9
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504
# Use React Query v5 for server state management
# Implement optimistic updates for better UX
# TypeScript strict mode for type safety

# CRITICAL: Celery + Redis configuration
# All notification tasks must be idempotent
# Use unique task IDs to prevent duplicate notifications
# Implement proper retry mechanisms with exponential backoff

# CRITICAL: Production considerations
# Redis connection pooling for high concurrency
# Database connection pooling with pgbouncer
# Proper error handling and logging with Sentry
# CORS configuration for cross-origin requests
```

## Implementation Blueprint

<<<<<<< HEAD
### Atomic Micro-Tasks (Implementation Order)

```yaml
# Phase 1: Environment Setup
Task 1.1 - Backend Virtual Environment:
  CREATE: Python virtual environment in backend/venv
  ACTIVATE: Virtual environment
  VALIDATE: Python 3.11+ available

Task 1.2 - Backend Dependencies Installation:
  INSTALL: pip install -r requirements/development.txt
  VALIDATE: All packages installed without errors
  TEST: python -c "import django; print(django.VERSION)"

Task 1.3 - Frontend Dependencies Installation:
  INSTALL: npm install in frontend directory
  VALIDATE: All packages installed without errors
  TEST: npm run type-check

Task 1.4 - Environment Configuration:
  COPY: .env.example to .env (backend and frontend)
  CONFIGURE: Basic environment variables
  VALIDATE: Environment files exist and readable

Task 1.5 - Django Initial Validation:
  RUN: python manage.py check
  VALIDATE: No Django configuration errors
  FIX: Any import or configuration issues

Task 1.6 - Frontend Build Validation:
  RUN: npm run build
  VALIDATE: TypeScript compilation successful
  FIX: Any TypeScript or Vite configuration issues

# Phase 2: Database Foundation
Task 2.1 - Django Initial Migration:
  RUN: python manage.py makemigrations
  RUN: python manage.py migrate
  VALIDATE: SQLite database created successfully

Task 2.2 - Django Superuser Creation:
  RUN: python manage.py createsuperuser
  VALIDATE: Admin user created
  TEST: Admin login at /admin/

Task 2.3 - Django Server Test:
  RUN: python manage.py runserver
  VALIDATE: Server starts without errors
  TEST: Health check endpoint responds

Task 2.4 - Frontend Development Server Test:
  RUN: npm run dev
  VALIDATE: Vite server starts without errors
  TEST: Frontend loads in browser

# Phase 3: Core App Structure
Task 3.1 - Core App Models:
  CREATE: apps/core/models.py with BaseModel
  IMPLEMENT: TimestampedModel and SoftDeleteModel
  VALIDATE: Models inherit correctly

Task 3.2 - Authentication App Setup:
  CREATE: apps/authentication/models.py
  IMPLEMENT: SalonUser model with roles
  MAKEMIGRATIONS: Authentication app migrations

Task 3.3 - Authentication Migration:
  RUN: python manage.py makemigrations authentication
  RUN: python manage.py migrate
  VALIDATE: Custom user model works

Task 3.4 - Basic API Endpoints:
  IMPLEMENT: Health check endpoints for each app
  TEST: /api/docs/ shows API documentation
  VALIDATE: All app routers load without errors

# Phase 4: Client Management Foundation
Task 4.1 - Client Models:
  CREATE: apps/clients/models.py
  IMPLEMENT: Client model with preferences
  MAKEMIGRATIONS: Client app migrations

Task 4.2 - Client API Schemas:
  CREATE: apps/clients/schemas.py
  IMPLEMENT: Pydantic schemas for validation
  VALIDATE: Schema validation works

Task 4.3 - Client CRUD APIs:
  CREATE: apps/clients/views.py
  IMPLEMENT: Basic CRUD operations
  TEST: Client creation, read, update, delete

Task 4.4 - Client API Integration:
  UPDATE: config/urls.py with client routes
  TEST: Client APIs via /api/docs/
  VALIDATE: All CRUD operations work

# Phase 5: Service Catalog
Task 5.1 - Service Models:
  CREATE: apps/services/models.py
  IMPLEMENT: Service, Category models
  MAKEMIGRATIONS: Services app migrations

Task 5.2 - Service APIs:
  CREATE: apps/services/views.py
  IMPLEMENT: Service CRUD operations
  TEST: Service management endpoints

Task 5.3 - Service Data Seeding:
  CREATE: Management command for sample services
  RUN: python manage.py seed_services
  VALIDATE: Sample services created

# Phase 6: Staff Management
Task 6.1 - Staff Models:
  CREATE: apps/staff/models.py
  IMPLEMENT: Staff profile and schedule models
  MAKEMIGRATIONS: Staff app migrations

Task 6.2 - Staff APIs:
  CREATE: apps/staff/views.py
  IMPLEMENT: Staff CRUD and availability
  TEST: Staff management endpoints

Task 6.3 - Staff Schedule Logic:
  IMPLEMENT: Availability calculation logic
  CREATE: Working hours management
  TEST: Staff availability queries

# Phase 7: Appointment System Core
Task 7.1 - Appointment Models:
  CREATE: apps/appointments/models.py
  IMPLEMENT: Appointment with constraints
  MAKEMIGRATIONS: Appointments app migrations

Task 7.2 - Appointment Validation:
  IMPLEMENT: Conflict detection logic
  CREATE: Business rule validation
  TEST: Overlap prevention works

Task 7.3 - Appointment APIs:
  CREATE: apps/appointments/views.py
  IMPLEMENT: Booking and management APIs
  TEST: Appointment CRUD operations

Task 7.4 - Availability Checker:
  IMPLEMENT: Real-time availability API
  CREATE: Time slot calculation logic
  TEST: Available slots return correctly

# Phase 8: Frontend Foundation
Task 8.1 - React Router Setup:
  CREATE: src/main.tsx with routing
  IMPLEMENT: Basic route structure
  TEST: Navigation between routes

Task 8.2 - API Client Setup:
  CREATE: src/api/client.ts
  IMPLEMENT: Axios configuration with auth
  TEST: API connection works

Task 8.3 - React Query Setup:
  CREATE: src/hooks/queries/
  IMPLEMENT: Client and service queries
  TEST: Data fetching works

Task 8.4 - UI Components Library:
  CREATE: src/components/ui/
  IMPLEMENT: Button, Input, Card components
  TEST: Components render correctly

# Phase 9: Appointment Booking UI
Task 9.1 - Service Selection:
  CREATE: ServiceSelector component
  IMPLEMENT: Service list with pricing
  TEST: Service selection works

Task 9.2 - Staff Selection:
  CREATE: StaffSelector component
  IMPLEMENT: Staff list with availability
  TEST: Staff selection works

Task 9.3 - Date/Time Picker:
  CREATE: AppointmentCalendar component
  IMPLEMENT: Available slots display
  TEST: Time slot selection works

Task 9.4 - Booking Form:
  CREATE: AppointmentBooking component
  IMPLEMENT: Complete booking flow
  TEST: End-to-end booking process

# Phase 10: Client Management UI
Task 10.1 - Client List:
  CREATE: ClientList component
  IMPLEMENT: Client search and pagination
  TEST: Client browsing works

Task 10.2 - Client Profile:
  CREATE: ClientProfile component
  IMPLEMENT: Client details and history
  TEST: Client information display

Task 10.3 - Client Form:
  CREATE: ClientForm component
  IMPLEMENT: Client creation and editing
  TEST: Client CRUD via UI

# Phase 11: Notifications
Task 11.1 - Notification Models:
  CREATE: apps/notifications/models.py
  IMPLEMENT: Notification tracking
  MAKEMIGRATIONS: Notifications app

Task 11.2 - Email Service:
  CREATE: Email notification service
  IMPLEMENT: SendGrid integration
  TEST: Email sending works

Task 11.3 - SMS Service:
  CREATE: SMS notification service
  IMPLEMENT: Twilio integration
  TEST: SMS sending works

Task 11.4 - Celery Tasks:
  CREATE: Celery task configuration
  IMPLEMENT: Background notification tasks
  TEST: Async notifications work

# Phase 12: Admin Dashboard
Task 12.1 - Dashboard Layout:
  CREATE: Admin dashboard component
  IMPLEMENT: Navigation and layout
  TEST: Dashboard loads correctly

Task 12.2 - Analytics Widgets:
  CREATE: Revenue and booking widgets
  IMPLEMENT: Real-time data display
  TEST: Widgets show correct data

Task 12.3 - Staff Management UI:
  CREATE: Staff management interface
  IMPLEMENT: Schedule and performance views
  TEST: Staff management works

# Phase 13: Testing & Quality
Task 13.1 - Backend Test Suite:
  CREATE: Unit tests for models and APIs
  IMPLEMENT: Test coverage for core functionality
  RUN: pytest with coverage report

Task 13.2 - Frontend Test Suite:
  CREATE: Component and integration tests
  IMPLEMENT: Test coverage for UI components
  RUN: npm test with coverage

Task 13.3 - End-to-End Tests:
  CREATE: E2E test scenarios
  IMPLEMENT: Critical user journey tests
  RUN: E2E test suite

Task 13.4 - Performance Optimization:
  ANALYZE: Database query performance
  OPTIMIZE: Slow queries and N+1 problems
  VALIDATE: Response times <200ms

# Phase 14: Production Setup
Task 14.1 - Production Settings:
  CREATE: Production configuration
  IMPLEMENT: Security and performance settings
  VALIDATE: Production settings work

Task 14.2 - Deployment Scripts:
  CREATE: Deployment automation
  IMPLEMENT: CI/CD pipeline
  TEST: Deployment process works

Task 14.3 - Monitoring Setup:
  IMPLEMENT: Error tracking with Sentry
  CREATE: Performance monitoring
  TEST: Monitoring alerts work
=======
### List of Tasks (Implementation Order)

```yaml
Task 1 - Project Foundation Setup:
  CREATE: Project structure and development environment
  EXECUTE: Docker Compose configuration with PostgreSQL 17, Redis 7, Django, React
  CREATE: Backend requirements.txt with Django 5.2, django-ninja, celery dependencies
  CREATE: Frontend package.json with React 19, TypeScript 5.9, Vite 5
  CONFIGURE: Environment variables and settings structure
  VALIDATE: All services start successfully and communicate

Task 2 - Context Engineering Documentation:
  CREATE: context/PROJECT_CONTEXT.md with Mario's business model and success metrics
  CREATE: context/TECHNICAL_CONTEXT.md with architecture decisions and performance requirements
  CREATE: context/FEATURE_CONTEXT.md with user journeys and business rules
  DOCUMENT: All enterprise quality requirements and constraints

Task 3 - Django Backend Foundation:
  CREATE: config/settings/ with base, development, production configurations
  CREATE: apps/core/ with base models, utilities, and common patterns
  CREATE: apps/authentication/ with SalonUser model and role-based permissions
  CONFIGURE: Database settings with connection pooling and timezone handling
  MIGRATE: Initial database schema with proper indexes

Task 4 - Client Management System:
  CREATE: apps/clients/models.py with AI-enhanced client profiles
  CREATE: apps/clients/schemas.py with Pydantic validation schemas
  CREATE: apps/clients/views.py with Django-Ninja CRUD APIs
  CREATE: apps/clients/services.py with business logic and preference tracking
  IMPLEMENT: Intelligent client search with autocomplete functionality
  TEST: Client CRUD operations with comprehensive test coverage

Task 5 - Service and Staff Management:
  CREATE: apps/services/models.py with service categories and pricing
  CREATE: apps/staff/models.py with staff profiles, schedules, and specialties
  IMPLEMENT: Staff availability calculation and working hours management
  CREATE: Service assignment and staff specialization logic
  TEST: Service and staff management functionality

Task 6 - Advanced Appointment System:
  CREATE: apps/appointments/models.py with conflict prevention constraints
  IMPLEMENT: Real-time availability checking with buffer time calculation
  CREATE: Appointment scheduling logic with business rule validation
  IMPLEMENT: Google Calendar bi-directional synchronization
  CREATE: Appointment status management and lifecycle tracking
  TEST: Comprehensive appointment scenarios including edge cases

Task 7 - Multi-Channel Notification System:
  CREATE: apps/notifications/models.py with delivery tracking
  IMPLEMENT: SMS notification service via Twilio integration
  IMPLEMENT: Email notification service via SendGrid integration
  CREATE: Celery background tasks with retry mechanisms
  IMPLEMENT: Notification templates and personalization
  TEST: Notification delivery with failure handling

Task 8 - Inventory Management:
  CREATE: apps/inventory/models.py with predictive analytics fields
  IMPLEMENT: Stock level monitoring and auto-reorder alerts
  CREATE: Usage tracking and consumption analytics
  IMPLEMENT: Supplier management and purchase order generation
  TEST: Inventory workflows and alert systems

Task 9 - React Frontend Foundation:
  CREATE: TypeScript interfaces matching Django models
  SETUP: React Query for server state management
  CREATE: API client with authentication and error handling
  IMPLEMENT: Routing and layout components
  CREATE: Reusable UI components with Tailwind CSS

Task 10 - Appointment Booking Interface:
  CREATE: AppointmentBooking.tsx with step-by-step wizard
  IMPLEMENT: Real-time availability checking with debounced API calls
  CREATE: Drag-and-drop calendar interface
  IMPLEMENT: Service selection with duration and pricing display
  CREATE: Staff selection with specialty matching
  TEST: Complete booking flow with validation

Task 11 - Client Management Interface:
  CREATE: ClientSearch.tsx with intelligent autocomplete
  IMPLEMENT: Client profile management with preference history
  CREATE: Client history view with service tracking
  IMPLEMENT: Quick client creation during booking process
  TEST: Client management workflows

Task 12 - Staff and Admin Dashboards:
  CREATE: Staff schedule management interface
  IMPLEMENT: Performance analytics and KPI tracking
  CREATE: Inventory management interface with alerts
  IMPLEMENT: Real-time dashboard with live updates
  CREATE: Reporting and analytics views
  TEST: Administrative functionality

Task 13 - Security and Performance Optimization:
  IMPLEMENT: GDPR compliance features (data export, deletion)
  CREATE: Rate limiting and input validation
  OPTIMIZE: Database queries and API performance
  IMPLEMENT: Caching strategy with Redis
  CREATE: Security headers and HTTPS enforcement
  TEST: Security and performance requirements

Task 14 - Production Deployment Setup:
  CREATE: Production Docker configurations
  SETUP: Nginx reverse proxy with SSL termination
  CONFIGURE: Environment-specific settings and secrets
  IMPLEMENT: Database backup and monitoring
  CREATE: CI/CD pipeline with quality gates
  TEST: Production deployment and scaling

Task 15 - AI Integration Foundation:
  IMPLEMENT: Client preference learning algorithms
  CREATE: Service recommendation engine
  IMPLEMENT: Optimal scheduling suggestions
  CREATE: Predictive analytics for inventory
  SETUP: Data collection for future AI enhancements
  TEST: AI features and recommendation accuracy
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504
```

### Per Task Pseudocode Examples

```python
<<<<<<< HEAD
# Task 1.1: Backend Virtual Environment Setup
def setup_backend_virtual_environment():
    """Create isolated Python environment for Django backend"""
    # PATTERN: Python virtual environment isolation
    import subprocess
    import os
    
    backend_path = "backend/"
    venv_path = os.path.join(backend_path, "venv")
    
    # Create virtual environment
    subprocess.run(["python3.11", "-m", "venv", venv_path], check=True)
    
    # Activate and upgrade pip
    pip_cmd = os.path.join(venv_path, "bin", "pip")
    subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
    
    return venv_path

# Task 1.2: Install Backend Base Dependencies
def install_backend_dependencies():
    """Install Django and core packages from requirements/base.txt"""
    # PATTERN: Requirements file dependency management
    requirements_files = [
        "requirements/base.txt",
        "requirements/development.txt"
    ]
    
    for req_file in requirements_files:
        subprocess.run([
            "pip", "install", "-r", req_file
        ], check=True, cwd="backend")
    
    # Validate critical imports
    try:
        import django
        import ninja
        from decouple import config
        print(f"✓ Django {django.get_version()} installed")
        print("✓ All base dependencies verified")
    except ImportError as e:
        raise Exception(f"Critical dependency missing: {e}")

# Task 2.1: Core Django App Structure
def create_core_app_structure():
    """Create core app with base models and utilities"""
    # PATTERN: Django app structure with enterprise patterns
    
    # Create core app
    subprocess.run([
        "python", "manage.py", "startapp", "core"
    ], cwd="backend", check=True)
    
    # Core models.py with base mixins
    core_models = '''
from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    """Base model with creation and modification timestamps"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    """Base model with soft delete functionality"""
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
'''
    
    with open("backend/apps/core/models.py", "w") as f:
        f.write(core_models)

# Task 3.1: Authentication App Models
def create_authentication_models():
    """Create custom user model with salon-specific fields"""
    # PATTERN: Custom user model with role-based access
    
    auth_models = '''
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import TimeStampedModel

class SalonUser(AbstractUser, TimeStampedModel):
    """Custom user model for salon staff and clients"""
    
    class UserRole(models.TextChoices):
        OWNER = 'owner', 'Salon Owner'
        MANAGER = 'manager', 'Manager'
        STYLIST = 'stylist', 'Hair Stylist'
        RECEPTIONIST = 'receptionist', 'Receptionist'
        CLIENT = 'client', 'Client'
    
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CLIENT
    )
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    is_active_staff = models.BooleanField(default=True)
    
    # Client-specific fields
    date_of_birth = models.DateField(null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    
    class Meta:
        db_table = 'salon_users'
        indexes = [
            models.Index(fields=['role', 'is_active']),
            models.Index(fields=['email']),
        ]
'''
    
    with open("backend/apps/authentication/models.py", "w") as f:
        f.write(auth_models)

# Task 5.1: Appointment Models with Conflict Prevention
def create_appointment_models():
    """Create appointment model with database-level conflict prevention"""
    # CRITICAL: Database constraints prevent double-booking
    
    appointment_models = '''
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.constraints import ExcludeConstraint
from django.contrib.postgres.fields import DateTimeRangeField
from psycopg2.extras import DateTimeTZRange
from apps.core.models import TimeStampedModel

class Appointment(TimeStampedModel):
    """Appointment with conflict prevention constraints"""
    
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending Confirmation'
        CONFIRMED = 'confirmed', 'Confirmed'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
        NO_SHOW = 'no_show', 'No Show'
    
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    stylist = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    
    # Time management
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    
    # Business fields
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True)
    
    # Tracking
    reminder_sent = models.BooleanField(default=False)
    calendar_synced = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'appointments'
        constraints = [
            # Prevent overlapping appointments for same stylist
            ExcludeConstraint(
                name='prevent_stylist_conflicts',
                expressions=[
                    ('stylist', '='),
                    (DateTimeRangeField('start_time', 'end_time', inclusive='[)'), '&&'),
                ],
                condition=models.Q(status__in=['pending', 'confirmed'])
            ),
        ]
        indexes = [
            models.Index(fields=['stylist', 'start_time']),
            models.Index(fields=['client', 'start_time']),
            models.Index(fields=['start_time', 'end_time']),
            models.Index(fields=['status']),
        ]
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time")
        
        if self.duration_minutes != (self.end_time - self.start_time).total_seconds() / 60:
            raise ValidationError("Duration must match time difference")
'''
    
    with open("backend/apps/appointments/models.py", "w") as f:
        f.write(appointment_models)

# Task 8.1: React Project Structure Setup
def setup_react_project_structure():
    """Create React TypeScript project with Vite and proper folder structure"""
    # PATTERN: Modern React development setup
    
    import subprocess
    import json
    import os
    
    # Initialize Vite React TypeScript project
    subprocess.run([
        "npm", "create", "vite@latest", "frontend", "--", 
        "--template", "react-ts"
    ], check=True)
    
    # Create folder structure
    frontend_structure = [
        "src/components/ui",
        "src/components/layout", 
        "src/components/appointments",
        "src/components/clients",
        "src/hooks",
        "src/services",
        "src/types",
        "src/utils",
        "src/contexts",
        "src/pages",
        "public/images"
    ]
    
    for folder in frontend_structure:
        os.makedirs(f"frontend/{folder}", exist_ok=True)

# Task 8.2: Install Frontend Dependencies
def install_frontend_dependencies():
    """Install React, TypeScript, and beauty salon specific packages"""
    # PATTERN: Modern React ecosystem setup
    
    dependencies = [
        "@tanstack/react-query@^5.0.0",
        "@tanstack/react-router@^1.0.0",
        "axios@^1.6.0",
        "react-hook-form@^7.48.0",
        "@hookform/resolvers@^3.3.0",
        "zod@^3.22.0",
        "date-fns@^2.30.0",
        "lucide-react@^0.294.0",
        "react-hot-toast@^2.4.0"
    ]
    
    dev_dependencies = [
        "@types/node@^20.0.0",
        "autoprefixer@^10.4.0",
        "postcss@^8.4.0",
        "tailwindcss@^3.4.0",
        "@tailwindcss/forms@^0.5.0",
        "@tailwindcss/typography@^0.5.0"
    ]
    
    # Install dependencies
    subprocess.run(["npm", "install"] + dependencies, cwd="frontend", check=True)
    subprocess.run(["npm", "install", "--save-dev"] + dev_dependencies, cwd="frontend", check=True)

# Task 10.1: Appointment Booking Component
def create_appointment_booking_component():
    """Create React component for appointment booking with form validation"""
    # PATTERN: React Query for server state + React Hook Form for client state
    
    component_code = '''
import React from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import toast from 'react-hot-toast';
import { api } from '../services/api';

const appointmentSchema = z.object({
  clientId: z.number().positive(),
  stylistId: z.number().positive(),
  serviceId: z.number().positive(),
  startTime: z.string().datetime(),
  notes: z.string().optional()
});

type AppointmentForm = z.infer<typeof appointmentSchema>;

export function AppointmentBooking() {
  const queryClient = useQueryClient();
  
  // Server state management
  const { data: services } = useQuery({
    queryKey: ['services'],
    queryFn: api.services.getAll,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
  
  const { data: stylists } = useQuery({
    queryKey: ['stylists'],
    queryFn: api.staff.getStylists,
    staleTime: 10 * 60 * 1000, // 10 minutes
  });
  
  // Form management
  const { register, handleSubmit, formState: { errors }, reset } = useForm<AppointmentForm>({
    resolver: zodResolver(appointmentSchema)
  });
  
  // Optimistic updates for better UX
  const createAppointment = useMutation({
    mutationFn: api.appointments.create,
    onMutate: async (newAppointment) => {
      await queryClient.cancelQueries({ queryKey: ['appointments'] });
      const previousAppointments = queryClient.getQueryData(['appointments']);
      
      // Optimistically update UI
      queryClient.setQueryData(['appointments'], (old: any[]) => [
        ...old,
        { ...newAppointment, id: `temp-${Date.now()}`, status: 'pending' }
      ]);
      
      return { previousAppointments };
    },
    onError: (err, variables, context) => {
      queryClient.setQueryData(['appointments'], context?.previousAppointments);
      toast.error('Booking failed. Please try again.');
    },
    onSuccess: () => {
      toast.success('Appointment booked successfully!');
      queryClient.invalidateQueries({ queryKey: ['appointments'] });
      reset();
    }
  });
  
  const onSubmit = (data: AppointmentForm) => {
    createAppointment.mutate(data);
  };
  
  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-soft p-6">
      <h2 className="text-2xl font-semibold text-primary-800 mb-6">Book Appointment</h2>
      
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {/* Service Selection */}
        <div>
          <label className="block text-sm font-medium text-primary-700 mb-1">
            Service
          </label>
          <select 
            {...register('serviceId', { valueAsNumber: true })}
            className="input-field w-full"
          >
            <option value="">Select a service</option>
            {services?.map((service) => (
              <option key={service.id} value={service.id}>
                {service.name} - ${service.price}
              </option>
            ))}
          </select>
          {errors.serviceId && (
            <p className="text-error text-sm mt-1">{errors.serviceId.message}</p>
          )}
        </div>
        
        {/* Form continues with stylist selection, date/time picker, etc. */}
        
        <button 
          type="submit" 
          disabled={createAppointment.isPending}
          className="btn-primary w-full"
        >
          {createAppointment.isPending ? 'Booking...' : 'Book Appointment'}
        </button>
      </form>
    </div>
  );
}
'''
    
    with open("frontend/src/components/appointments/AppointmentBooking.tsx", "w") as f:
        f.write(component_code)
=======
# Task 3: Django Backend Foundation
def setup_django_backend():
    # PATTERN: Environment-specific settings
    # base.py - Common settings
    BASE_SETTINGS = {
        'INSTALLED_APPS': [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'ninja',
            'corsheaders',
            'apps.core',
            'apps.authentication',
            'apps.clients',
            'apps.appointments',
        ],
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'CONN_MAX_AGE': 600,
                'OPTIONS': {'MAX_CONNS': 20}
            }
        },
        'USE_TZ': True,
        'TIME_ZONE': 'Europe/Warsaw',
    }

# Task 6: Advanced Appointment System
async def create_appointment_with_validation():
    # CRITICAL: Atomic transaction for conflict prevention
    async with transaction.atomic():
        # Validate availability with buffer time
        is_available = await check_availability_with_buffer(
            stylist_id=data.stylist_id,
            start_time=data.start_time,
            duration=service.duration,
            buffer_minutes=15
        )
        
        if not is_available:
            raise ConflictError("Time slot not available")
        
        # Create appointment with business rules
        appointment = await Appointment.objects.acreate(
            client=client,
            stylist=stylist,
            service=service,
            start_time=data.start_time,
            end_time=data.start_time + service.duration,
            total_price=calculate_price(service, client),
            status='pending'
        )
        
        # Trigger background tasks
        send_appointment_confirmation.delay(appointment.id)
        sync_google_calendar.delay(appointment.id)
        
        return appointment

# Task 10: React Appointment Booking
function AppointmentBooking() {
    // PATTERN: React Query for server state
    const { data: services } = useQuery({
        queryKey: ['services'],
        queryFn: api.services.getAll,
        staleTime: 5 * 60 * 1000, // 5 minutes
    });
    
    // PATTERN: Optimistic updates
    const createAppointment = useMutation({
        mutationFn: api.appointments.create,
        onMutate: async (newAppointment) => {
            await queryClient.cancelQueries(['appointments']);
            const previous = queryClient.getQueryData(['appointments']);
            
            // Optimistically update
            queryClient.setQueryData(['appointments'], old => [
                ...old,
                { ...newAppointment, id: 'temp-' + Date.now() }
            ]);
            
            return { previous };
        },
        onError: (err, vars, context) => {
            queryClient.setQueryData(['appointments'], context.previous);
            toast.error('Booking failed. Please try again.');
        },
        onSuccess: () => {
            toast.success('Appointment booked successfully!');
            queryClient.invalidateQueries(['appointments']);
        }
    });
}
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504
```

### Integration Points
```yaml
DATABASE:
  - migrations: "Complete schema with constraints and indexes"
  - constraints: 
    - "EXCLUDE constraint for appointment conflicts"
    - "CHECK constraints for business rules"
    - "UNIQUE constraints for data integrity"
  - indexes:
    - "GiST index for time range queries"
    - "B-tree indexes for frequent lookups"
    - "Full-text search indexes for client search"

EXTERNAL_SERVICES:
  - google_calendar: "Bi-directional synchronization"
  - twilio_sms: "Reliable SMS delivery with webhooks"
  - sendgrid_email: "Professional email notifications"
  - stripe_payments: "Future payment processing integration"

CACHING:
  - redis_sessions: "User session management"
  - api_cache: "Frequently accessed data caching"
  - availability_cache: "Real-time availability caching"

MONITORING:
  - sentry: "Error tracking and performance monitoring"
  - prometheus: "Application metrics collection"
  - grafana: "Dashboard and alerting"
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Backend validation
cd backend
ruff check apps/ --fix
mypy apps/ --strict
python manage.py check
python manage.py makemigrations --dry-run

# Frontend validation
cd frontend
npm run lint
npm run type-check
npm run build

# Expected: Zero errors, zero warnings
```

### Level 2: Unit Tests (95% Coverage Requirement)
```bash
# Backend comprehensive testing
cd backend
python -m pytest apps/ -v --cov=apps --cov-report=html --cov-fail-under=95
python -m pytest apps/appointments/tests/test_conflict_prevention.py -v
python -m pytest apps/clients/tests/test_preference_learning.py -v

# Frontend testing
cd frontend
npm test -- --coverage --watchAll=false --coverageThreshold='{"global":{"branches":95,"functions":95,"lines":95,"statements":95}}'

# Performance testing
python -m pytest apps/appointments/tests/test_performance.py::test_booking_response_time
# Target: <200ms response time for appointment creation
```

### Level 3: Integration Testing
```bash
# Start complete system
docker-compose up -d
sleep 60  # Wait for all services

# Test complete booking flow
curl -X POST http://localhost:8000/api/v1/appointments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -d '{
    "client_id": 1,
    "stylist_id": 1,
    "service_id": 1,
    "start_time": "2024-03-15T14:00:00Z",
    "notes": "First time client"
  }'

# Expected: 201 Created, notification sent within 30s, calendar synced

# Test frontend booking flow
npx playwright test tests/booking-flow.spec.ts --headed
# Target: Complete end-to-end booking in <30 seconds
```

### Level 4: Performance & Enterprise Validation
```bash
# Load testing (Netflix standard)
artillery run tests/load-booking-system.yml
# Target: 1000 concurrent users, <200ms P95 response time

# Security testing
bandit -r backend/apps/
safety check
npm audit

# GDPR compliance testing
python manage.py test apps.clients.tests.test_gdpr_compliance
# Target: Data export, anonymization, deletion workflows
```

## Final Validation Checklist
- [ ] All unit tests pass with 95%+ coverage
- [ ] Integration tests validate complete workflows
- [ ] Performance requirements met: <200ms API responses
- [ ] Load testing passes: 1000+ concurrent users
- [ ] Security scans show zero critical vulnerabilities
- [ ] GDPR compliance features working
- [ ] Real-time notifications delivered within 30 seconds
- [ ] Calendar synchronization working bi-directionally
- [ ] Mobile responsive design validated
- [ ] Accessibility standards met (WCAG 2.1 AA)
- [ ] Production deployment successful
- [ ] Monitoring and alerting configured
- [ ] Database backups and recovery tested
- [ ] AI foundation ready for future enhancements

---

## Anti-Patterns to Avoid
- ❌ Don't allow appointment conflicts - use database constraints
- ❌ Don't ignore timezone handling - always use timezone-aware datetime
- ❌ Don't skip input validation - sanitize all user inputs
- ❌ Don't use synchronous code in async context
- ❌ Don't hardcode business rules - make them configurable
- ❌ Don't skip error handling - handle all edge cases gracefully
- ❌ Don't compromise on test coverage - maintain 95% minimum
- ❌ Don't ignore performance - validate response times continuously
- ❌ Don't skip security scans - run automated security checks
- ❌ Don't ignore GDPR - implement proper data protection

## Confidence Score: 9/10
This PRP provides comprehensive implementation guidance with detailed task breakdown, extensive validation procedures, and addresses all enterprise requirements. The structured approach with context engineering integration and quality gates ensures high confidence for successful implementation of the complete Mario Beauty Salon management system.
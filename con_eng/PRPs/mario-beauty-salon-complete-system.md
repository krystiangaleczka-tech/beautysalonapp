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
6. **Mandatory Git Workflow**: Every completed micro-task MUST be committed to Git with descriptive message following pattern 'feat: Task X.Y - [Micro-Task Description]'

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

**🔸 MANDATORY GIT WORKFLOW 🔸**
**After completing EVERY micro-task below, you MUST:**
1. `git add .`
2. `git commit -m "feat: Task X.Y - [Micro-Task Description]"`  
3. `git push origin main`

**Example:** `git commit -m "feat: Task 4.1 - Create Client Model Structure"`

**This ensures:**
- Granular version control for each atomic change
- Easy rollback to any micro-task completion state
- Professional development workflow with detailed commit history
- Compliance with enterprise Git standards

---

```yaml
# Phase 1: Project Foundation Setup (COMPLETED)
Task 1.1 - Create Backend Virtual Environment:
  CREATE: Python virtual environment in backend/venv
  ACTIVATE: Virtual environment
  VALIDATE: Python 3.11+ available

Task 1.2 - Install Backend Dependencies:
  INSTALL: pip install -r requirements/development.txt
  VALIDATE: All packages installed without errors
  TEST: python -c "import django; print(django.VERSION)"

Task 1.3 - Install Frontend Dependencies:
  INSTALL: npm install in frontend directory
  VALIDATE: All packages installed without errors
  TEST: npm run type-check

Task 1.4 - Configure Environment Variables:
  COPY: .env.example to .env (backend and frontend)
  CONFIGURE: Basic environment variables
  VALIDATE: Environment files exist and readable

Task 1.5 - Validate Django Configuration:
  RUN: python manage.py check
  VALIDATE: No Django configuration errors
  FIX: Any import or configuration issues

Task 1.6 - Validate Frontend Build:
  RUN: npm run build
  VALIDATE: TypeScript compilation successful
  FIX: Any TypeScript or Vite configuration issues

# Phase 2: Context Engineering Documentation (COMPLETED)
Task 2.1 - Create Project Context:
  CREATE: context/PROJECT_CONTEXT.md
  DOCUMENT: Business model and success metrics
  VALIDATE: Context documentation complete

Task 2.2 - Create Technical Context:
  CREATE: context/TECHNICAL_CONTEXT.md
  DOCUMENT: Architecture decisions and performance requirements
  VALIDATE: Technical specifications complete

Task 2.3 - Create Feature Context:
  CREATE: context/FEATURE_CONTEXT.md
  DOCUMENT: User journeys and business rules
  VALIDATE: Feature specifications complete

# Phase 3: Django Backend Foundation (COMPLETED)
Task 3.1 - Create Core Base Models:
  CREATE: apps/core/models.py
  IMPLEMENT: TimeStampedModel class
  IMPLEMENT: SoftDeleteModel class
  IMPLEMENT: BaseModel class combining both
  VALIDATE: Abstract models work correctly

Task 3.2 - Create Authentication Models:
  CREATE: apps/authentication/models.py
  IMPLEMENT: SalonUser model with roles
  IMPLEMENT: UserProfile model
  IMPLEMENT: Role-based permissions
  VALIDATE: Custom user model structure

Task 3.3 - Configure Custom User Model:
  UPDATE: config/settings/base.py
  SET: AUTH_USER_MODEL = 'authentication.SalonUser'
  VALIDATE: Django recognizes custom user model

Task 3.4 - Create Authentication Migrations:
  RUN: python manage.py makemigrations authentication
  VALIDATE: Migration files created successfully

Task 3.5 - Apply Database Migrations:
  RUN: python manage.py migrate
  VALIDATE: Database tables created
  TEST: Custom user model works

Task 3.6 - Test Authentication System:
  CREATE: Superuser with custom model
  TEST: User creation and authentication
  VALIDATE: All authentication features work

# Phase 4: Client Management System
Task 4.1 - Create Client Model Structure:
  CREATE: apps/clients/models.py
  IMPLEMENT: Client model extending BaseModel
  IMPLEMENT: Client preference fields
  IMPLEMENT: Contact information fields
  VALIDATE: Model structure correct

Task 4.2 - Add Client Business Logic:
  IMPLEMENT: Client search methods
  IMPLEMENT: Preference tracking methods
  IMPLEMENT: Contact validation
  VALIDATE: Business logic functions

Task 4.3 - Create Client Migrations:
  RUN: python manage.py makemigrations clients
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Client tables created

Task 4.4 - Create Client API Schemas:
  CREATE: apps/clients/schemas.py
  IMPLEMENT: ClientCreateSchema
  IMPLEMENT: ClientUpdateSchema
  IMPLEMENT: ClientResponseSchema
  VALIDATE: Schema validation works

Task 4.5 - Implement Client CRUD APIs:
  CREATE: apps/clients/api.py
  IMPLEMENT: create_client endpoint
  IMPLEMENT: get_client endpoint
  IMPLEMENT: update_client endpoint
  IMPLEMENT: delete_client endpoint
  VALIDATE: CRUD operations work

Task 4.6 - Add Client Search API:
  IMPLEMENT: search_clients endpoint
  IMPLEMENT: Client filtering logic
  IMPLEMENT: Pagination support
  VALIDATE: Search functionality works

Task 4.7 - Integrate Client APIs:
  UPDATE: config/urls.py
  ADD: Client router to main API
  TEST: All endpoints via /api/docs/
  VALIDATE: API documentation shows correctly

Task 4.8 - Test Client Management System:
  TEST: Client creation via API
  TEST: Client retrieval and search
  TEST: Client updates and deletion
  VALIDATE: Complete CRUD workflow

# Phase 5: Service Catalog Management
Task 5.1 - Create Service Category Model:
  CREATE: apps/services/models.py
  IMPLEMENT: ServiceCategory model
  IMPLEMENT: Category hierarchy support
  VALIDATE: Category model structure

Task 5.2 - Create Service Model:
  IMPLEMENT: Service model with pricing
  IMPLEMENT: Service duration and details
  IMPLEMENT: Service-category relationships
  VALIDATE: Service model relationships

Task 5.3 - Create Service Migrations:
  RUN: python manage.py makemigrations services
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Service tables created

Task 5.4 - Create Service API Schemas:
  CREATE: apps/services/schemas.py
  IMPLEMENT: ServiceCreateSchema
  IMPLEMENT: ServiceUpdateSchema
  IMPLEMENT: CategoryCreateSchema
  VALIDATE: Service schemas work

Task 5.5 - Implement Service CRUD APIs:
  CREATE: apps/services/api.py
  IMPLEMENT: Service CRUD endpoints
  IMPLEMENT: Category CRUD endpoints
  VALIDATE: Service API operations

Task 5.6 - Create Service Data Seeding:
  CREATE: Management command for sample services
  IMPLEMENT: Seed beauty salon services
  RUN: python manage.py seed_services
  VALIDATE: Sample services created

Task 5.7 - Integrate Service APIs:
  UPDATE: config/urls.py with service routes
  TEST: Service APIs via /api/docs/
  VALIDATE: Service management works

# Phase 6: Staff Management System
Task 6.1 - Create Staff Profile Model:
  CREATE: apps/staff/models.py
  IMPLEMENT: StaffProfile model
  IMPLEMENT: Staff specializations
  IMPLEMENT: Commission tracking
  VALIDATE: Staff model structure

Task 6.2 - Create Staff Schedule Model:
  IMPLEMENT: WorkingHours model
  IMPLEMENT: Staff availability tracking
  IMPLEMENT: Schedule conflict prevention
  VALIDATE: Schedule model relationships

Task 6.3 - Create Staff Migrations:
  RUN: python manage.py makemigrations staff
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Staff tables created

Task 6.4 - Implement Staff Business Logic:
  IMPLEMENT: Availability calculation methods
  IMPLEMENT: Working hours management
  IMPLEMENT: Staff performance tracking
  VALIDATE: Staff logic functions

Task 6.5 - Create Staff API Schemas:
  CREATE: apps/staff/schemas.py
  IMPLEMENT: StaffCreateSchema
  IMPLEMENT: ScheduleUpdateSchema
  VALIDATE: Staff API schemas

Task 6.6 - Implement Staff APIs:
  CREATE: apps/staff/api.py
  IMPLEMENT: Staff CRUD endpoints
  IMPLEMENT: Schedule management APIs
  IMPLEMENT: Availability checker API
  VALIDATE: Staff API operations

Task 6.7 - Integrate Staff APIs:
  UPDATE: config/urls.py with staff routes
  TEST: Staff APIs via /api/docs/
  VALIDATE: Staff management system

# Phase 7: Appointment System Core
Task 7.1 - Create Appointment Model:
  CREATE: apps/appointments/models.py
  IMPLEMENT: Appointment model with constraints
  IMPLEMENT: Appointment status tracking
  IMPLEMENT: Database-level conflict prevention
  VALIDATE: Appointment model structure

Task 7.2 - Implement Appointment Validation:
  IMPLEMENT: Conflict detection logic
  IMPLEMENT: Business rule validation
  IMPLEMENT: Time slot validation
  VALIDATE: Overlap prevention works

Task 7.3 - Create Appointment Migrations:
  RUN: python manage.py makemigrations appointments
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Appointment tables with constraints

Task 7.4 - Create Appointment API Schemas:
  CREATE: apps/appointments/schemas.py
  IMPLEMENT: AppointmentCreateSchema
  IMPLEMENT: AppointmentUpdateSchema
  VALIDATE: Appointment schemas

Task 7.5 - Implement Appointment APIs:
  CREATE: apps/appointments/api.py
  IMPLEMENT: Appointment booking API
  IMPLEMENT: Appointment management APIs
  VALIDATE: Appointment CRUD operations

Task 7.6 - Create Availability Checker:
  IMPLEMENT: Real-time availability API
  IMPLEMENT: Time slot calculation logic
  IMPLEMENT: Staff availability integration
  VALIDATE: Available slots return correctly

Task 7.7 - Integrate Appointment APIs:
  UPDATE: config/urls.py with appointment routes
  TEST: Appointment APIs via /api/docs/
  VALIDATE: Complete appointment system

# Phase 8: Frontend Foundation
Task 8.1 - Setup React Router:
  CREATE: src/main.tsx with routing configuration
  IMPLEMENT: Basic route structure
  IMPLEMENT: Route protection for authenticated areas
  TEST: Navigation between routes works

Task 8.2 - Create API Client Configuration:
  CREATE: src/api/client.ts
  IMPLEMENT: Axios configuration with authentication
  IMPLEMENT: Request/response interceptors
  TEST: API connection and error handling

Task 8.3 - Setup React Query:
  CREATE: src/hooks/queries/ directory
  IMPLEMENT: Client and service queries
  IMPLEMENT: Mutation hooks for CRUD operations
  TEST: Data fetching and caching works

Task 8.4 - Create Base UI Components:
  CREATE: src/components/ui/ directory
  IMPLEMENT: Button, Input, Card components
  IMPLEMENT: Loading and error components
  TEST: Components render correctly

Task 8.5 - Setup Authentication Context:
  CREATE: src/contexts/AuthContext.tsx
  IMPLEMENT: Authentication state management
  IMPLEMENT: Login/logout functionality
  TEST: Authentication flow works

Task 8.6 - Create Layout Components:
  CREATE: src/components/layout/
  IMPLEMENT: Header, Sidebar, Layout components
  IMPLEMENT: Responsive design patterns
  TEST: Layout renders on different screen sizes

# Phase 9: Appointment Booking Interface
Task 9.1 - Create Service Selection Component:
  CREATE: src/components/appointments/ServiceSelector.tsx
  IMPLEMENT: Service list with pricing display
  IMPLEMENT: Service filtering and search
  TEST: Service selection works correctly

Task 9.2 - Create Staff Selection Component:
  CREATE: src/components/appointments/StaffSelector.tsx
  IMPLEMENT: Staff list with availability display
  IMPLEMENT: Staff specialization filtering
  TEST: Staff selection works correctly

Task 9.3 - Create Date/Time Picker:
  CREATE: src/components/appointments/AppointmentCalendar.tsx
  IMPLEMENT: Calendar with available slots
  IMPLEMENT: Time slot selection interface
  TEST: Date/time selection works

Task 9.4 - Create Booking Form:
  CREATE: src/components/appointments/AppointmentBooking.tsx
  IMPLEMENT: Complete booking flow
  IMPLEMENT: Form validation and submission
  TEST: End-to-end booking process

Task 9.5 - Integrate Booking Components:
  CREATE: src/pages/BookingPage.tsx
  IMPLEMENT: Multi-step booking wizard
  IMPLEMENT: Booking confirmation flow
  TEST: Complete booking user journey

# Phase 10: Client Management Interface
Task 10.1 - Create Client List Component:
  CREATE: src/components/clients/ClientList.tsx
  IMPLEMENT: Client search and pagination
  IMPLEMENT: Client filtering options
  TEST: Client browsing functionality

Task 10.2 - Create Client Profile Component:
  CREATE: src/components/clients/ClientProfile.tsx
  IMPLEMENT: Client details and history display
  IMPLEMENT: Appointment history view
  TEST: Client information display

Task 10.3 - Create Client Form Component:
  CREATE: src/components/clients/ClientForm.tsx
  IMPLEMENT: Client creation and editing
  IMPLEMENT: Form validation and submission
  TEST: Client CRUD operations via UI

Task 10.4 - Integrate Client Management:
  CREATE: src/pages/ClientsPage.tsx
  IMPLEMENT: Client management interface
  IMPLEMENT: Client workflow navigation
  TEST: Complete client management system

# Phase 11: Notification System
Task 11.1 - Create Notification Models:
  CREATE: apps/notifications/models.py
  IMPLEMENT: Notification tracking model
  IMPLEMENT: Delivery status tracking
  VALIDATE: Notification model structure

Task 11.2 - Create Notification Migrations:
  RUN: python manage.py makemigrations notifications
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Notification tables created

Task 11.3 - Implement Email Service:
  CREATE: apps/notifications/services/email.py
  IMPLEMENT: SendGrid integration
  IMPLEMENT: Email template system
  TEST: Email sending functionality

Task 11.4 - Implement SMS Service:
  CREATE: apps/notifications/services/sms.py
  IMPLEMENT: Twilio integration
  IMPLEMENT: SMS template system
  TEST: SMS sending functionality

Task 11.5 - Create Celery Task Configuration:
  CREATE: Backend Celery configuration
  IMPLEMENT: Background notification tasks
  IMPLEMENT: Task retry mechanisms
  TEST: Async notification processing

Task 11.6 - Integrate Notification APIs:
  CREATE: apps/notifications/api.py
  IMPLEMENT: Notification management endpoints
  UPDATE: config/urls.py with notification routes
  TEST: Notification system integration

# Phase 12: Admin Dashboard
Task 12.1 - Create Dashboard Layout:
  CREATE: src/components/dashboard/DashboardLayout.tsx
  IMPLEMENT: Admin navigation and layout
  IMPLEMENT: Role-based access control
  TEST: Dashboard loads correctly

Task 12.2 - Create Analytics Widgets:
  CREATE: src/components/dashboard/widgets/
  IMPLEMENT: Revenue and booking widgets
  IMPLEMENT: Real-time data display
  TEST: Widgets show correct data

Task 12.3 - Create Staff Management Interface:
  CREATE: src/components/dashboard/StaffManagement.tsx
  IMPLEMENT: Staff schedule and performance views
  IMPLEMENT: Staff administration tools
  TEST: Staff management functionality

Task 12.4 - Integrate Dashboard Components:
  CREATE: src/pages/AdminDashboard.tsx
  IMPLEMENT: Complete admin interface
  IMPLEMENT: Dashboard navigation
  TEST: Full admin dashboard functionality

# Phase 13: Testing & Quality Assurance
Task 13.1 - Create Backend Test Structure:
  CREATE: Backend test configuration
  IMPLEMENT: Test database setup
  IMPLEMENT: Test fixtures and factories
  VALIDATE: Test environment works

Task 13.2 - Implement Model Tests:
  CREATE: Unit tests for all models
  IMPLEMENT: Model validation tests
  IMPLEMENT: Relationship constraint tests
  RUN: pytest with coverage report

Task 13.3 - Implement API Tests:
  CREATE: API endpoint tests
  IMPLEMENT: Authentication and authorization tests
  IMPLEMENT: Business logic tests
  VALIDATE: API test coverage

Task 13.4 - Create Frontend Test Structure:
  CREATE: Frontend test configuration
  IMPLEMENT: Component testing setup
  IMPLEMENT: Mock API responses
  VALIDATE: Frontend test environment

Task 13.5 - Implement Component Tests:
  CREATE: Component and integration tests
  IMPLEMENT: User interaction tests
  IMPLEMENT: UI component tests
  RUN: npm test with coverage

Task 13.6 - Create End-to-End Tests:
  CREATE: E2E test scenarios
  IMPLEMENT: Critical user journey tests
  IMPLEMENT: Cross-browser testing
  RUN: Complete E2E test suite

Task 13.7 - Performance Optimization:
  ANALYZE: Database query performance
  OPTIMIZE: Slow queries and N+1 problems
  IMPLEMENT: Caching strategies
  VALIDATE: Response times <200ms

# Phase 14: Production Deployment
Task 14.1 - Create Production Settings:
  CREATE: Production configuration files
  IMPLEMENT: Security and performance settings
  IMPLEMENT: Environment variable management
  VALIDATE: Production settings work

Task 14.2 - Create Docker Configuration:
  CREATE: Production Docker configurations
  IMPLEMENT: Multi-stage builds
  IMPLEMENT: Container optimization
  TEST: Docker build and run

Task 14.3 - Setup Nginx Configuration:
  CREATE: Nginx reverse proxy configuration
  IMPLEMENT: SSL termination setup
  IMPLEMENT: Static file serving
  TEST: Nginx configuration

Task 14.4 - Create Deployment Scripts:
  CREATE: Deployment automation scripts
  IMPLEMENT: Database migration automation
  IMPLEMENT: Zero-downtime deployment
  TEST: Deployment process

Task 14.5 - Setup CI/CD Pipeline:
  CREATE: GitHub Actions workflow
  IMPLEMENT: Automated testing and deployment
  IMPLEMENT: Quality gates and checks
  TEST: CI/CD pipeline functionality

Task 14.6 - Configure Monitoring:
  IMPLEMENT: Error tracking with Sentry
  IMPLEMENT: Performance monitoring
  IMPLEMENT: Health check endpoints
  TEST: Monitoring and alerting

# Phase 15: AI Integration Foundation
Task 15.1 - Create AI Model Structure:
  CREATE: AI model configuration
  IMPLEMENT: Client preference learning setup
  IMPLEMENT: Data collection framework
  VALIDATE: AI foundation structure

Task 15.2 - Implement Recommendation Engine:
  CREATE: Service recommendation algorithms
  IMPLEMENT: Preference-based suggestions
  IMPLEMENT: Learning from booking patterns
  TEST: Recommendation accuracy

Task 15.3 - Create Scheduling Optimization:
  IMPLEMENT: Optimal scheduling suggestions
  IMPLEMENT: Staff efficiency optimization
  IMPLEMENT: Revenue optimization algorithms
  TEST: Scheduling optimization

Task 15.4 - Implement Predictive Analytics:
  CREATE: Inventory prediction models
  IMPLEMENT: Demand forecasting
  IMPLEMENT: Business intelligence features
  TEST: Predictive analytics accuracy

Task 15.5 - Integrate AI Features:
  IMPLEMENT: AI API endpoints
  IMPLEMENT: Frontend AI components
  IMPLEMENT: Real-time learning updates
  TEST: Complete AI integration
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
# Task 4.1: Client Model Structure Creation
def create_client_model():
    """Create Client model with preference tracking and business logic"""
    # PATTERN: Django model with JSON fields for flexibility
    
    client_model = '''
from django.db import models
from django.core.validators import RegexValidator
from apps.core.models import BaseModel
from apps.authentication.models import SalonUser

class Client(BaseModel):
    """Client model with comprehensive tracking and preferences"""
    
    # Basic Information
    user = models.OneToOneField(
        SalonUser, 
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    
    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in format: '+999999999'"
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )
    
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )
    
    # Preferences and History
    service_preferences = models.JSONField(
        default=dict,
        help_text="Client service preferences and notes"
    )
    
    allergies = models.TextField(
        blank=True,
        help_text="Known allergies and sensitivities"
    )
    
    skin_type = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Skin type for facial services"
    )
    
    hair_type = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Hair type and condition notes"
    )
    
    # Business Tracking
    total_visits = models.PositiveIntegerField(default=0)
    total_spent = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )
    
    last_visit = models.DateTimeField(null=True, blank=True)
    loyalty_points = models.PositiveIntegerField(default=0)
    
    # Communication Preferences
    preferred_contact_method = models.CharField(
        max_length=20,
        choices=[
            ('email', 'Email'),
            ('sms', 'SMS'),
            ('phone', 'Phone'),
            ('app', 'App Notification'),
        ],
        default='email'
    )
    
    marketing_consent = models.BooleanField(default=False)
    reminder_consent = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'clients'
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['last_visit']),
            models.Index(fields=['total_visits']),
        ]
        
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.phone_number}"
    
    def get_preferences_summary(self):
        """Return formatted summary of client preferences"""
        return {
            'services': self.service_preferences.get('favorite_services', []),
            'staff': self.service_preferences.get('preferred_staff', []),
            'times': self.service_preferences.get('preferred_times', []),
            'special_notes': self.allergies or 'None'
        }
    
    def add_loyalty_points(self, points):
        """Add loyalty points and save"""
        self.loyalty_points += points
        self.save(update_fields=['loyalty_points'])
    
    def update_visit_stats(self, amount_spent):
        """Update visit statistics after appointment"""
        from django.utils import timezone
        
        self.total_visits += 1
        self.total_spent += amount_spent
        self.last_visit = timezone.now()
        self.save(update_fields=['total_visits', 'total_spent', 'last_visit'])
'''
    
    with open("backend/apps/clients/models.py", "w") as f:
        f.write(client_model)
    
    print("✓ Client model created with preference tracking")
    return True

# Task 4.4: Client API Schema Creation  
def create_client_schemas():
    """Create Pydantic schemas for Client API validation"""
    # PATTERN: Pydantic schemas with Django-Ninja integration
    
    schemas = '''
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, Dict, List
from datetime import datetime

class ClientCreateSchema(BaseModel):
    """Schema for creating new clients"""
    
    # User Information
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)
    
    # Contact Information
    phone_number: Optional[str] = Field(None, regex=r"^\+?1?\d{9,15}$")
    emergency_contact_name: Optional[str] = Field(None, max_length=100)
    emergency_contact_phone: Optional[str] = Field(None, regex=r"^\+?1?\d{9,15}$")
    
    # Preferences
    allergies: Optional[str] = None
    skin_type: Optional[str] = Field(None, max_length=50)
    hair_type: Optional[str] = Field(None, max_length=50)
    
    # Communication Preferences
    preferred_contact_method: str = Field(default="email")
    marketing_consent: bool = False
    reminder_consent: bool = True
    
    @validator('preferred_contact_method')
    def validate_contact_method(cls, v):
        valid_methods = ['email', 'sms', 'phone', 'app']
        if v not in valid_methods:
            raise ValueError(f'Must be one of: {valid_methods}')
        return v

class ClientUpdateSchema(BaseModel):
    """Schema for updating existing clients"""
    
    first_name: Optional[str] = Field(None, min_length=1, max_length=30)
    last_name: Optional[str] = Field(None, min_length=1, max_length=30)
    phone_number: Optional[str] = Field(None, regex=r"^\+?1?\d{9,15}$")
    emergency_contact_name: Optional[str] = Field(None, max_length=100)
    emergency_contact_phone: Optional[str] = Field(None, regex=r"^\+?1?\d{9,15}$")
    
    allergies: Optional[str] = None
    skin_type: Optional[str] = Field(None, max_length=50)
    hair_type: Optional[str] = Field(None, max_length=50)
    
    preferred_contact_method: Optional[str] = None
    marketing_consent: Optional[bool] = None
    reminder_consent: Optional[bool] = None
    
    service_preferences: Optional[Dict] = None
    
    @validator('preferred_contact_method')
    def validate_contact_method(cls, v):
        if v is not None:
            valid_methods = ['email', 'sms', 'phone', 'app']
            if v not in valid_methods:
                raise ValueError(f'Must be one of: {valid_methods}')
        return v

class ClientResponseSchema(BaseModel):
    """Schema for client API responses"""
    
    id: int
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[str]
    
    total_visits: int
    total_spent: float
    last_visit: Optional[datetime]
    loyalty_points: int
    
    allergies: Optional[str]
    skin_type: Optional[str]
    hair_type: Optional[str]
    
    preferred_contact_method: str
    marketing_consent: bool
    reminder_consent: bool
    
    service_preferences: Dict
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ClientSearchSchema(BaseModel):
    """Schema for client search parameters"""
    
    query: Optional[str] = Field(None, min_length=1)
    phone: Optional[str] = None
    email: Optional[str] = None
    
    # Pagination
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    
    # Sorting
    sort_by: str = Field(default="last_name")
    sort_order: str = Field(default="asc")
    
    @validator('sort_by')
    def validate_sort_field(cls, v):
        valid_fields = ['first_name', 'last_name', 'email', 'total_visits', 'last_visit', 'created_at']
        if v not in valid_fields:
            raise ValueError(f'Must be one of: {valid_fields}')
        return v
    
    @validator('sort_order')
    def validate_sort_order(cls, v):
        if v not in ['asc', 'desc']:
            raise ValueError('Must be "asc" or "desc"')
        return v

class ClientStatsSchema(BaseModel):
    """Schema for client statistics response"""
    
    total_clients: int
    new_clients_this_month: int
    active_clients: int
    avg_visits_per_client: float
    avg_spending_per_client: float
    top_spending_clients: List[Dict]
'''
    
    with open("backend/apps/clients/schemas.py", "w") as f:
        f.write(schemas)
    
    print("✓ Client API schemas created with validation")
    return True

# Task 4.5: Client CRUD API Implementation
def create_client_apis():
    """Implement Client CRUD APIs with Django-Ninja"""
    # PATTERN: Django-Ninja APIs with proper error handling
    
    api_code = '''
from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q

from .models import Client
from .schemas import (
    ClientCreateSchema,
    ClientUpdateSchema, 
    ClientResponseSchema,
    ClientSearchSchema,
    ClientStatsSchema
)

User = get_user_model()
router = Router()

@router.post("/", response=ClientResponseSchema)
def create_client(request, data: ClientCreateSchema):
    """Create a new client with user account"""
    
    try:
        with transaction.atomic():
            # Create user account
            user = User.objects.create_user(
                username=data.email,
                email=data.email,
                first_name=data.first_name,
                last_name=data.last_name,
                role=User.UserRole.CLIENT
            )
            
            # Create client profile
            client = Client.objects.create(
                user=user,
                phone_number=data.phone_number or "",
                emergency_contact_name=data.emergency_contact_name or "",
                emergency_contact_phone=data.emergency_contact_phone or "",
                allergies=data.allergies or "",
                skin_type=data.skin_type or "",
                hair_type=data.hair_type or "",
                preferred_contact_method=data.preferred_contact_method,
                marketing_consent=data.marketing_consent,
                reminder_consent=data.reminder_consent
            )
            
            return client
            
    except Exception as e:
        raise ValueError(f"Failed to create client: {str(e)}")

@router.get("/{client_id}", response=ClientResponseSchema)
def get_client(request, client_id: int):
    """Get client by ID"""
    
    client = get_object_or_404(
        Client.objects.select_related('user'),
        id=client_id
    )
    return client

@router.put("/{client_id}", response=ClientResponseSchema)
def update_client(request, client_id: int, data: ClientUpdateSchema):
    """Update client information"""
    
    client = get_object_or_404(Client, id=client_id)
    
    # Update user fields if provided
    user_updated = False
    if data.first_name:
        client.user.first_name = data.first_name
        user_updated = True
    if data.last_name:
        client.user.last_name = data.last_name
        user_updated = True
    
    if user_updated:
        client.user.save()
    
    # Update client fields
    update_fields = []
    for field_name, value in data.dict(exclude_unset=True).items():
        if hasattr(client, field_name) and value is not None:
            setattr(client, field_name, value)
            update_fields.append(field_name)
    
    if update_fields:
        client.save(update_fields=update_fields)
    
    return client

@router.delete("/{client_id}")
def delete_client(request, client_id: int):
    """Soft delete client"""
    
    client = get_object_or_404(Client, id=client_id)
    client.delete()  # Uses soft delete from BaseModel
    
    return {"message": "Client deleted successfully"}

@router.get("/", response=List[ClientResponseSchema])
def search_clients(request, filters: ClientSearchSchema = None):
    """Search and list clients with filtering"""
    
    queryset = Client.objects.select_related('user')
    
    if filters:
        # Apply search filters
        if filters.query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=filters.query) |
                Q(user__last_name__icontains=filters.query) |
                Q(user__email__icontains=filters.query) |
                Q(phone_number__icontains=filters.query)
            )
        
        if filters.phone:
            queryset = queryset.filter(phone_number__icontains=filters.phone)
        
        if filters.email:
            queryset = queryset.filter(user__email__icontains=filters.email)
        
        # Apply sorting
        sort_field = filters.sort_by
        if sort_field in ['first_name', 'last_name', 'email']:
            sort_field = f'user__{sort_field}'
        
        if filters.sort_order == 'desc':
            sort_field = f'-{sort_field}'
        
        queryset = queryset.order_by(sort_field)
        
        # Apply pagination
        start = (filters.page - 1) * filters.page_size
        end = start + filters.page_size
        queryset = queryset[start:end]
    
    return list(queryset)

@router.get("/stats/summary", response=ClientStatsSchema)
def get_client_stats(request):
    """Get client statistics for dashboard"""
    from django.db.models import Count, Avg, Sum
    from django.utils import timezone
    from datetime import datetime, timedelta
    
    # Calculate statistics
    total_clients = Client.objects.count()
    
    current_month = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    new_clients_this_month = Client.objects.filter(
        created_at__gte=current_month
    ).count()
    
    # Active clients (visited in last 6 months)
    six_months_ago = timezone.now() - timedelta(days=180)
    active_clients = Client.objects.filter(
        last_visit__gte=six_months_ago
    ).count()
    
    # Average statistics
    avg_stats = Client.objects.aggregate(
        avg_visits=Avg('total_visits'),
        avg_spending=Avg('total_spent')
    )
    
    # Top spending clients
    top_clients = Client.objects.select_related('user').order_by(
        '-total_spent'
    )[:5]
    
    top_spending_clients = [
        {
            'name': f"{client.user.first_name} {client.user.last_name}",
            'total_spent': float(client.total_spent),
            'total_visits': client.total_visits
        }
        for client in top_clients
    ]
    
    return {
        'total_clients': total_clients,
        'new_clients_this_month': new_clients_this_month,
        'active_clients': active_clients,
        'avg_visits_per_client': avg_stats['avg_visits'] or 0,
        'avg_spending_per_client': avg_stats['avg_spending'] or 0,
        'top_spending_clients': top_spending_clients
    }
'''
    
    with open("backend/apps/clients/api.py", "w") as f:
        f.write(api_code)
    
    print("✓ Client CRUD APIs implemented")
    return True
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
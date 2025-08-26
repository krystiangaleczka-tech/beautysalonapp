name: "Mario Beauty Salon Complete System PRP v1 - Enterprise Implementation"
description: |
  Complete enterprise-grade beauty salon management system implementation for Mario's 4-person salon team 
  following Django 5.2 LTS + React 19 + PostgreSQL 17 architecture with AI-ready foundation.

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
  why: React 19 concurrent features and modern patterns
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
├── agentos/                    # Agent OS development system
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
├── frontend/                 # React 19 + TypeScript Frontend
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

# CRITICAL: React 19 + TypeScript 5.9
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
```

### Per Task Pseudocode Examples

```python
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
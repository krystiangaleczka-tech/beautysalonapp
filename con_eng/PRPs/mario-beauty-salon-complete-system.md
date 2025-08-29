# Mario Beauty Salon Core System PRP v2 - MVP Implementation

**🔍 CONTEXT7 INTEGRATION ENABLED**
API Key: ctx7sk-704c26ad-7bf3-4e2b-96df-20dcadcdcf4c
For up-to-date code documentation and examples, use Context7 API when available:
- Search: `curl -X GET "https://context7.com/api/v1/search?query={library}" -H "Authorization: Bearer ctx7sk-704c26ad-7bf3-4e2b-96df-20dcadcdcf4c"`
- Get docs: `curl -X GET "https://context7.com/api/v1/{library}?type=json&topic={topic}&tokens=500" -H "Authorization: Bearer ctx7sk-704c26ad-7bf3-4e2b-96df-20dcadcdcf4c"`

**IMPORTANT**: Limit Context7 queries to maximum 500 tokens per request to conserve usage.

name: "Mario Beauty Salon Core System PRP v2 - MVP Implementation"
description: |
  Core MVP beauty salon management system implementation for Mario's 4-person salon team 
  following Django 5.2 LTS + React 18 + PostgreSQL 17 architecture with modular foundation for future extensions.

## Purpose
Implement a production-ready MVP beauty salon management application that handles essential operations: client management, service catalog, staff management, appointment scheduling, and basic notifications. Focus on core functionality to reduce manual work by 60% and enable online booking, with a foundation for future enhancements like analytics and AI.

## Core Principles
1. **Context is King**: Incorporate all business rules from Mario's salon operations.
2. **MVP Standards**: Prioritize reliability, security, and usability over advanced features.
3. **Validation Loops**: Aim for 90% test coverage with quality gates.
4. **Progressive Success**: Iterative development with continuous validation.
5. **Global Rules**: Follow enterprise development system principles, but simplified for MVP.
6. **DO NOT COMMIT TO GITHUB ANYTHING**

---

## Goal
Build an MVP salon management system enabling Mario's 4-person team to manage clients, services, staff, appointments, and notifications, with a focus on intelligent scheduling and automation.

## Why
- **Business Impact**: Enable basic automation for salon operations.
- **User Experience**: Support online booking and client profiles.
- **Staff Efficiency**: Automated scheduling and reminders.
- **Scalability**: Modular foundation for future AI and analytics.
- **Competitive Advantage**: Reliable system for small business.

## What
MVP platform with client management, service catalog, staff management, appointment scheduling, and notifications. Advanced features (inventory, analytics, AI preferences) deferred to post-MVP phases.

### Success Criteria
- [ ] Complete appointment booking system with conflict prevention.
- [ ] Client management with basic profiles.
- [ ] Automated email/SMS notifications.
- [ ] Staff management with schedules.
- [ ] <300ms API response times.
- [ ] 99% system availability.
- [ ] 90% code test coverage.
- [ ] GDPR compliant data handling.
- [ ] Mobile-responsive design.

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Include these in your context window
- file: /Users/krystiangaleczka/Documents/beautysalonapp/INITIAL.md
  why: Complete technical specification, architecture decisions, and business requirements

- file: /Users/krystiangaleczka/Documents/beautysalonapp/ENTERPRISE_DEVELOPMENT_SYSTEM.md
  why: Enterprise quality standards and development workflow requirements

- url: https://docs.djangoproject.com/en/5.2/
  why: Django 5.2 LTS patterns, ORM relationships, and best practices
  section: Models, Views, Authentication, Performance optimization

- url: https://django-ninja.dev/
  why: High-performance API patterns with automatic OpenAPI documentation
  critical: Async support and Pydantic integration for type safety

- url: https://react.dev/
  why: React 18 stable features and modern patterns
  section: Hooks, State management, Performance optimization

- url: https://www.typescriptlang.org/docs/
  why: TypeScript 5.9 advanced type system and patterns
  critical: Interface design and type safety for salon domain models

- url: https://docs.celeryq.dev/en/stable/
  why: Background task processing for notifications
  section: Task routing, retry mechanisms

- url: https://redis.io/docs/
  why: Caching strategies and session management
  section: Data structures, performance optimization

- url: https://www.postgresql.org/docs/17/
  why: Advanced constraints, indexing, and performance tuning
  critical: Appointment conflict prevention and data integrity
```

### Current Codebase Tree
```bash
beautysalonapp/
├── .agent-os/                  # Agent OS development system (optional for MVP)
├── con_eng/                   # Context engineering framework (optional for MVP)
├── ENTERPRISE_DEVELOPMENT_SYSTEM.md  # Enterprise development framework
├── INITIAL.md                 # Complete technical specification
└── README.md                  # Project overview
```

### Desired Codebase Tree with MVP Implementation
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
│   │   │   ├── models.py     # Client profiles
│   │   │   ├── schemas.py    # Pydantic schemas
│   │   │   ├── api.py        # Client APIs (renamed from views.py for Ninja)
│   │   │   ├── services.py   # Business logic
│   │   │   └── tests.py      # Unit tests
│   │   ├── services/         # Salon services management
│   │   │   ├── models.py     # Service, Category models
│   │   │   ├── schemas.py    # Service schemas
│   │   │   ├── api.py        # Service APIs
│   │   │   └── tests.py      # Unit tests
│   │   ├── staff/            # Staff management
│   │   │   ├── models.py     # Staff profiles, schedules
│   │   │   ├── schemas.py    # Staff schemas
│   │   │   ├── api.py        # Staff APIs
│   │   │   └── tests.py      # Unit tests
│   │   ├── appointments/     # Appointment system
│   │   │   ├── models.py     # Appointment with constraints
│   │   │   ├── schemas.py    # Booking schemas
│   │   │   ├── api.py        # Booking APIs
│   │   │   ├── services.py   # Scheduling logic
│   │   │   ├── tasks.py      # Notification tasks
│   │   │   └── tests.py      # Unit tests
│   │   ├── notifications/    # Basic notifications
│   │   │   ├── models.py     # Notification logs
│   │   │   ├── services.py   # Email/SMS services
│   │   │   ├── tasks.py      # Delivery tasks
│   │   │   └── templates/    # Message templates
│   │   └── core/
│   │       ├── models.py     # Base models, mixins
│   │       ├── permissions.py # Base permissions
│   │       ├── utils.py      # Common utilities
│   │       ├── validators.py  # Custom validators
│   │       └── tests.py      # Unit tests
│   ├── static/               # Static files
│   ├── media/                # User uploads
│   ├── templates/            # Email templates
│   ├── requirements/
│   │   ├── base.txt          # Base dependencies
│   │   ├── development.txt   # Dev dependencies
│   │   └── production.txt    # Production dependencies
│   ├── manage.py             # Django management
│   ├── pytest.ini            # Testing configuration
│   └── tests/                # Integration tests
├── frontend/                 # React 18 + TypeScript Frontend
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
│   │   │   └── staff/
│   │   │       ├── StaffSchedule.tsx
│   │   │       └── StaffManagement.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts     # Authentication hooks
│   │   │   ├── useAppointments.ts # Appointment management
│   │   │   ├── useClients.ts   # Client management
│   │   │   └── useWebSocket.ts # Real-time updates (optional)
│   │   ├── services/
│   │   │   ├── api.ts         # API client configuration
│   │   │   ├── auth.ts        # Authentication service
│   │   │   ├── appointments.ts # Appointment APIs
│   │   │   ├── clients.ts     # Client APIs
│   │   │   └── websocket.ts   # WebSocket service (optional)
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
│   ├── vitest.config.ts       # Testing config
│   └── __tests__/             # Frontend tests
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
├── .github/
│   └── workflows/            # CI/CD pipelines
│       ├── ci.yml            # Continuous Integration
│       └── cd.yml            # Continuous Deployment
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

# CRITICAL: React 18 + TypeScript 5.9
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

# CONTEXT7 INTEGRATION: Use for latest documentation
# When implementing any library, first check Context7 for current best practices
# Especially useful for React hooks, Django patterns, and TypeScript examples
# Fall back to standard documentation only if Context7 limit exceeded
```

## Implementation Blueprint

### Atomic Micro-Tasks (Implementation Order)

**ðŸ”¸ MANDATORY GIT WORKFLOW ðŸ”¸**
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
 CHECK CONSOLE THEN RUN TESTS: Run `python --version` and check for errors in console. Fix if any (e.g., install Python if missing).

Task 1.2 - Install Backend Dependencies:
  INSTALL: pip install -r requirements/development.txt
  VALIDATE: All packages installed without errors
  TEST: python -c "import django; print(django.VERSION)"
 CHECK CONSOLE THEN RUN TESTS: Run the install command and monitor console for errors (e.g., dependency conflicts). Fix by updating requirements.txt if needed.

Task 1.3 - Install Frontend Dependencies:
  INSTALL: npm install in frontend directory
  VALIDATE: All packages installed without errors
  TEST: npm run type-check
 CHECK CONSOLE THEN RUN TESTS: Run `npm install` and TEST for errors (e.g., network issues or version mismatches). Fix by retrying or updating package.json.

Task 1.4 - Configure Environment Variables:
  COPY: .env.example to .env (backend and frontend)
  CONFIGURE: Basic environment variables
  VALIDATE: Environment files exist and readable
 CHECK CONSOLE THEN RUN TESTS: Run `cat .env` or open in editor; check for syntax errors. Fix invalid formats.

Task 1.5 - Validate Django Configuration:
  RUN: python manage.py check
  VALIDATE: No Django configuration errors
  FIX: Any import or configuration issues
 CHECK CONSOLE THEN RUN TESTS: Run the command and inspect console output for errors. Fix by correcting settings.py.

Task 1.6 - Validate Frontend Build:
  RUN: npm run build
  VALIDATE: TypeScript compilation successful
  FIX: Any TypeScript or Vite configuration issues
 CHECK CONSOLE THEN RUN TESTS: Run the build command and check for console errors (e.g., TS errors). Fix by resolving type issues.

# Phase 2: Context Engineering Documentation (COMPLETED)
Task 2.1 - Create Project Context:
  CREATE: context/PROJECT_CONTEXT.md
  DOCUMENT: Business model and success metrics
  VALIDATE: Context documentation complete
 CHECK CONSOLE THEN RUN TESTS: No console involvement; manually review file for completeness. Fix typos or missing sections.

Task 2.2 - Create Technical Context:
  CREATE: context/TECHNICAL_CONTEXT.md
  DOCUMENT: Architecture decisions and performance requirements
  VALIDATE: Technical specifications complete
 CHECK CONSOLE THEN RUN TESTS: No console; manual review. Fix inconsistencies.

Task 2.3 - Create Feature Context:
  CREATE: context/FEATURE_CONTEXT.md
  DOCUMENT: User journeys and business rules
  VALIDATE: Feature specifications complete
 CHECK CONSOLE THEN RUN TESTS: No console; manual review. Fix gaps.

# Phase 3: Django Backend Foundation (COMPLETED)
Task 3.1 - Create Core Base Models:
  CREATE: apps/core/models.py
  IMPLEMENT: TimeStampedModel class
  IMPLEMENT: SoftDeleteModel class
  IMPLEMENT: BaseModel class combining both
  VALIDATE: Abstract models work correctly
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py makemigrations --dry-run` and check for errors. Fix model definitions.

Task 3.2 - Create Authentication Models:
  CREATE: apps/authentication/models.py
  IMPLEMENT: SalonUser model with roles
  IMPLEMENT: UserProfile model
  IMPLEMENT: Role-based permissions
  VALIDATE: Custom user model structure
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py makemigrations --dry-run authentication` and fix console errors.

Task 3.3 - Configure Custom User Model:
  UPDATE: config/settings/base.py
  SET: AUTH_USER_MODEL = 'authentication.SalonUser'
  VALIDATE: Django recognizes custom user model
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py check` and fix errors.

Task 3.4 - Create Authentication Migrations:
  RUN: python manage.py makemigrations authentication
  VALIDATE: Migration files created successfully
 CHECK CONSOLE THEN RUN TESTS: Monitor makemigrations output for errors; fix model issues.

Task 3.5 - Apply Database Migrations:
  RUN: python manage.py migrate
  VALIDATE: Database tables created
  TEST: Custom user model works
 CHECK CONSOLE THEN RUN TESTS: Run migrate and fix any SQL errors.

Task 3.6 - Test Authentication System:
  CREATE: Superuser with custom model
  TEST: User creation and authentication
  VALIDATE: All authentication features work
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py createsuperuser` and check for errors; fix auth config.

# Phase 4: Client Management System
Task 4.1 - Create Client Model Structure:
  CREATE: apps/clients/models.py
  IMPLEMENT: Client model extending BaseModel
  IMPLEMENT: Contact information fields
  IMPLEMENT: Basic preference fields (e.g., allergies, preferred contact)
  VALIDATE: Model structure correct
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py makemigrations --dry-run clients` and fix errors.

Task 4.2 - Create Client Migrations:
  RUN: python manage.py makemigrations clients
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Client tables created
 CHECK CONSOLE THEN RUN TESTS: Monitor makemigrations and migrate for errors; fix model fields.

Task 4.3 - Add Client Business Logic:
  CREATE: apps/clients/services.py
  IMPLEMENT: Client search methods
  IMPLEMENT: Contact validation
  VALIDATE: Business logic functions
 CHECK CONSOLE THEN RUN TESTS: Run `python -m pytest apps/clients` (if tests exist) or manual import in shell; fix logic errors.

Task 4.4 - Create Client API Schemas:
  CREATE: apps/clients/schemas.py
  IMPLEMENT: ClientCreateSchema
  IMPLEMENT: ClientUpdateSchema
  IMPLEMENT: ClientResponseSchema
  VALIDATE: Schema validation works
 CHECK CONSOLE THEN RUN TESTS: Run Python shell import and test schemas; fix Pydantic errors.

Task 4.5 - Implement Client CRUD APIs:
  CREATE: apps/clients/api.py
  IMPLEMENT: create_client endpoint
  IMPLEMENT: get_client endpoint
  IMPLEMENT: update_client endpoint
  IMPLEMENT: delete_client endpoint
  VALIDATE: CRUD operations work
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py runserver` and test endpoints; fix API errors.

Task 4.6 - Add Client Search API:
  IMPLEMENT: search_clients endpoint in apps/clients/api.py
  IMPLEMENT: Client filtering logic
  IMPLEMENT: Pagination support
  VALIDATE: Search functionality works
 CHECK CONSOLE THEN RUN TESTS: Test API with curl/postman; fix query errors.

Task 4.7 - Integrate Client APIs:
  UPDATE: config/urls.py
  ADD: Client router to main API
  TEST: All endpoints via /api/docs/
  VALIDATE: API documentation shows correctly
 CHECK CONSOLE THEN RUN TESTS: Run server and access /api/docs/; fix routing errors.

Task 4.8 - Test Client Management System:
  CREATE: apps/clients/tests.py
  TEST: Client creation via API
  TEST: Client retrieval and search
  TEST: Client updates and deletion
  VALIDATE: Complete CRUD workflow with 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Run `python -m pytest apps/clients` and fix test failures.

# Phase 5: Service Catalog Management
Task 5.1 - Create Service Category Model:
  CREATE: apps/services/models.py
  IMPLEMENT: ServiceCategory model
  IMPLEMENT: Category hierarchy support
  VALIDATE: Category model structure
 CHECK CONSOLE THEN RUN TESTS: Run `python manage.py makemigrations --dry-run services` and fix errors.

Task 5.2 - Create Service Model:
  IMPLEMENT: Service model with pricing, duration, details
  IMPLEMENT: Service-category relationships
  VALIDATE: Service model relationships
 CHECK CONSOLE THEN RUN TESTS: Run makemigrations dry-run; fix relations.

Task 5.3 - Create Service Migrations:
  RUN: python manage.py makemigrations services
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Service tables created
 CHECK CONSOLE THEN RUN TESTS: Monitor for migration errors; fix.

Task 5.4 - Create Service API Schemas:
  CREATE: apps/services/schemas.py
  IMPLEMENT: ServiceCreateSchema
  IMPLEMENT: ServiceUpdateSchema
  IMPLEMENT: CategoryCreateSchema
  VALIDATE: Service schemas work
 CHECK CONSOLE THEN RUN TESTS: Test schemas in shell; fix.

Task 5.5 - Implement Service CRUD APIs:
  CREATE: apps/services/api.py
  IMPLEMENT: Service CRUD endpoints
  IMPLEMENT: Category CRUD endpoints
  VALIDATE: Service API operations
 CHECK CONSOLE THEN RUN TESTS: Run server and test; fix.

Task 5.6 - Create Service Data Seeding:
  CREATE: Management command for sample services in apps/services/management/commands/seed_services.py
  IMPLEMENT: Seed beauty salon services
  RUN: python manage.py seed_services
  VALIDATE: Sample services created
 CHECK CONSOLE THEN RUN TESTS: Run command; fix seeding errors.

Task 5.7 - Integrate Service APIs:
  UPDATE: config/urls.py with service routes
  TEST: Service APIs via /api/docs/
  VALIDATE: Service management works
 CHECK CONSOLE THEN RUN TESTS: Access docs; fix.

Task 5.8 - Test Service Catalog System:
  CREATE: apps/services/tests.py
  TEST: Service creation and retrieval
  TEST: Category management
  VALIDATE: Complete workflow with 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Run pytest; fix failures.

# Phase 6: Staff Management System
Task 6.1 - Create Staff Profile Model:
  CREATE: apps/staff/models.py
  IMPLEMENT: StaffProfile model
  IMPLEMENT: Specializations
  VALIDATE: Staff model structure
 CHECK CONSOLE THEN RUN TESTS: Dry-run makemigrations; fix.

Task 6.2 - Create Staff Schedule Model:
  IMPLEMENT: WorkingHours model
  IMPLEMENT: Staff availability tracking
  IMPLEMENT: Schedule conflict prevention
  VALIDATE: Schedule model relationships
 CHECK CONSOLE THEN RUN TESTS: Dry-run; fix.

Task 6.3 - Create Staff Migrations:
  RUN: python manage.py makemigrations staff
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Staff tables created
 CHECK CONSOLE THEN RUN TESTS: Monitor; fix.

Task 6.4 - Implement Staff Business Logic:
  CREATE: apps/staff/services.py
  IMPLEMENT: Availability calculation methods
  IMPLEMENT: Working hours management
  VALIDATE: Staff logic functions
 CHECK CONSOLE THEN RUN TESTS: Test in shell; fix.

Task 6.5 - Create Staff API Schemas:
  CREATE: apps/staff/schemas.py
  IMPLEMENT: StaffCreateSchema
  IMPLEMENT: ScheduleUpdateSchema
  VALIDATE: Staff API schemas
 CHECK CONSOLE THEN RUN TESTS: Shell test; fix.

Task 6.6 - Implement Staff APIs:
  CREATE: apps/staff/api.py
  IMPLEMENT: Staff CRUD endpoints
  IMPLEMENT: Schedule management APIs
  IMPLEMENT: Availability checker API
  VALIDATE: Staff API operations
 CHECK CONSOLE THEN RUN TESTS: Server test; fix.

Task 6.7 - Integrate Staff APIs:
  UPDATE: config/urls.py with staff routes
  TEST: Staff APIs via /api/docs/
  VALIDATE: Staff management system
 CHECK CONSOLE THEN RUN TESTS: Access docs; fix.

Task 6.8 - Test Staff Management System:
  CREATE: apps/staff/tests.py
  TEST: Staff creation and scheduling
  TEST: Availability checks
  VALIDATE: Complete workflow with 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Pytest; fix.

# Phase 7: Appointment System Core
Task 7.1 - Create Appointment Model:
  CREATE: apps/appointments/models.py
  IMPLEMENT: Appointment model with constraints
  IMPLEMENT: Appointment status tracking
  IMPLEMENT: Database-level conflict prevention (EXCLUDE constraints)
  VALIDATE: Appointment model structure
 CHECK CONSOLE THEN RUN TESTS: Dry-run makemigrations; fix.

Task 7.2 - Create Appointment Migrations:
  RUN: python manage.py makemigrations appointments
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Appointment tables with constraints
 CHECK CONSOLE THEN RUN TESTS: Monitor; fix.

Task 7.3 - Implement Appointment Validation:
  CREATE: apps/appointments/services.py
  IMPLEMENT: Conflict detection logic
  IMPLEMENT: Business rule validation
  IMPLEMENT: Time slot validation
  VALIDATE: Overlap prevention works
 CHECK CONSOLE THEN RUN TESTS: Shell test; fix.

Task 7.4 - Create Appointment API Schemas:
  CREATE: apps/appointments/schemas.py
  IMPLEMENT: AppointmentCreateSchema
  IMPLEMENT: AppointmentUpdateSchema
  VALIDATE: Appointment schemas
 CHECK CONSOLE THEN RUN TESTS: Shell; fix.

Task 7.5 - Implement Appointment APIs:
  CREATE: apps/appointments/api.py
  IMPLEMENT: Appointment booking API
  IMPLEMENT: Appointment management APIs
  VALIDATE: Appointment CRUD operations
 CHECK CONSOLE THEN RUN TESTS: Server test; fix.

Task 7.6 - Create Availability Checker:
  IMPLEMENT: Real-time availability API in apps/appointments/api.py
  IMPLEMENT: Time slot calculation logic
  IMPLEMENT: Staff availability integration
  VALIDATE: Available slots return correctly
 CHECK CONSOLE THEN RUN TESTS: API test; fix.

Task 7.7 - Integrate Appointment APIs:
  UPDATE: config/urls.py with appointment routes
  TEST: Appointment APIs via /api/docs/
  VALIDATE: Complete appointment system
 CHECK CONSOLE THEN RUN TESTS: Docs access; fix.

Task 7.8 - Test Appointment System:
  CREATE: apps/appointments/tests.py
  TEST: Booking with conflict prevention
  TEST: Availability checks
  VALIDATE: Complete workflow with 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Pytest; fix.

# Phase 8: Notification System (Basic)
Task 8.1 - Create Notification Models:
  CREATE: apps/notifications/models.py
  IMPLEMENT: Notification tracking model
  IMPLEMENT: Delivery status tracking
  VALIDATE: Notification model structure
 CHECK CONSOLE THEN RUN TESTS: Dry-run; fix.

Task 8.2 - Create Notification Migrations:
  RUN: python manage.py makemigrations notifications
  VALIDATE: Migration files created
  RUN: python manage.py migrate
  VALIDATE: Notification tables created
 CHECK CONSOLE THEN RUN TESTS: Monitor; fix.

Task 8.3 - Implement Notification Services:
  CREATE: apps/notifications/services.py
  IMPLEMENT: Email and SMS sending logic
  IMPLEMENT: Basic templates
  VALIDATE: Sending functions work
 CHECK CONSOLE THEN RUN TESTS: Shell test; fix.

Task 8.4 - Integrate Notifications with Appointments:
  UPDATE: apps/appointments/tasks.py
  IMPLEMENT: Celery tasks for appointment notifications
  INTEGRATE: Trigger notifications on booking/create/update
  VALIDATE: Notifications sent on events
 CHECK CONSOLE THEN RUN TESTS: Run Celery worker and test; fix.

Task 8.5 - Test Notification System:
  CREATE: apps/notifications/tests.py
  TEST: Email/SMS delivery
  TEST: Integration with appointments
  VALIDATE: Complete workflow with 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Pytest; fix.

# Phase 9: Frontend Foundation
Task 9.1 - Setup React Router:
  CREATE: src/main.tsx with routing configuration
  IMPLEMENT: Basic route structure
  IMPLEMENT: Route protection for authenticated areas
  TEST: Navigation between routes works
 CHECK CONSOLE THEN RUN TESTS: Run `npm run dev` and browser console; fix JS errors.

Task 9.2 - Create API Client Configuration:
  CREATE: src/services/api.ts
  IMPLEMENT: Axios configuration with authentication
  IMPLEMENT: Request/response interceptors
  TEST: API connection and error handling
 CHECK CONSOLE THEN RUN TESTS: Dev server; fix network errors.

Task 9.3 - Setup React Query:
  CREATE: src/hooks/ directory
  IMPLEMENT: Basic queries for auth and clients
  IMPLEMENT: Mutation hooks for CRUD operations
  TEST: Data fetching and caching works
 CHECK CONSOLE THEN RUN TESTS: Browser console; fix query errors.

Task 9.4 - Create Base UI Components:
  CREATE: src/components/ui/ directory
  IMPLEMENT: Button, Input, Card components
  IMPLEMENT: Loading and error components
  TEST: Components render correctly
 CHECK CONSOLE THEN RUN TESTS: Dev; fix render errors.

Task 9.5 - Setup Authentication Context:
  CREATE: src/hooks/useAuth.ts
  IMPLEMENT: Authentication state management
  IMPLEMENT: Login/logout functionality
  TEST: Authentication flow works
 CHECK CONSOLE THEN RUN TESTS: Test login; fix auth errors.

Task 9.6 - Create Layout Components:
  CREATE: src/components/layout/
  IMPLEMENT: Header, Sidebar, Layout components
  IMPLEMENT: Responsive design patterns
  TEST: Layout renders on different screen sizes
 CHECK CONSOLE THEN RUN TESTS: Resize browser; fix CSS/JS errors.

Task 9.7 - Test Frontend Foundation:
  CREATE: frontend/__tests__/foundation.test.tsx
  TEST: Routing, API client, auth
  VALIDATE: 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Run `npm test`; fix test errors.

# Phase 10: Appointment Booking Interface
Task 10.1 - Create Service Selection Component:
  CREATE: src/components/appointments/ServiceSelector.tsx
  IMPLEMENT: Service list with pricing display
  IMPLEMENT: Service filtering and search
  TEST: Service selection works correctly
 CHECK CONSOLE THEN RUN TESTS: Dev; fix component errors.

Task 10.2 - Create Staff Selection Component:
  CREATE: src/components/appointments/StaffSelector.tsx
  IMPLEMENT: Staff list with availability display
  IMPLEMENT: Staff specialization filtering
  TEST: Staff selection works correctly
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 10.3 - Create Date/Time Picker:
  CREATE: src/components/appointments/AppointmentCalendar.tsx
  IMPLEMENT: Calendar with available slots
  IMPLEMENT: Time slot selection interface
  TEST: Date/time selection works
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 10.4 - Create Booking Form:
  CREATE: src/components/appointments/AppointmentBooking.tsx
  IMPLEMENT: Complete booking flow
  IMPLEMENT: Form validation and submission
  TEST: End-to-end booking process
 CHECK CONSOLE THEN RUN TESTS: Dev; fix form errors.

Task 10.5 - Integrate Booking Components:
  CREATE: src/components/appointments/ directory integration
  IMPLEMENT: Multi-step booking wizard
  IMPLEMENT: Booking confirmation flow
  TEST: Complete booking user journey
 CHECK CONSOLE THEN RUN TESTS: Dev; fix integration errors.

Task 10.6 - Test Appointment Booking Interface:
  CREATE: frontend/__tests__/appointments.test.tsx
  TEST: Booking flow, validations
  VALIDATE: 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Npm test; fix.

# Phase 11: Client Management Interface
Task 11.1 - Create Client List Component:
  CREATE: src/components/clients/ClientList.tsx
  IMPLEMENT: Client search and pagination
  IMPLEMENT: Client filtering options
  TEST: Client browsing functionality
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 11.2 - Create Client Profile Component:
  CREATE: src/components/clients/ClientProfile.tsx
  IMPLEMENT: Client details and history display
  IMPLEMENT: Appointment history view
  TEST: Client information display
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 11.3 - Create Client Form Component:
  CREATE: src/components/clients/ClientForm.tsx
  IMPLEMENT: Client creation and editing
  IMPLEMENT: Form validation and submission
  TEST: Client CRUD operations via UI
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 11.4 - Integrate Client Management:
  CREATE: src/components/clients/ directory integration
  IMPLEMENT: Client management interface
  IMPLEMENT: Client workflow navigation
  TEST: Complete client management system
 CHECK CONSOLE THEN RUN TESTS: Dev; fix.

Task 11.5 - Test Client Management Interface:
  CREATE: frontend/__tests__/clients.test.tsx
  TEST: CRUD, search
  VALIDATE: 90% coverage
 CHECK CONSOLE THEN RUN TESTS: Npm test; fix.

# Phase 12: Integration and End-to-End Testing
Task 12.1 - Setup CI/CD Pipelines:
  CREATE: .github/workflows/ci.yml
  IMPLEMENT: Automated tests on push
  VALIDATE: Pipeline runs successfully
 CHECK CONSOLE THEN RUN TESTS: Git push and check GitHub Actions console; fix yaml errors.

Task 12.2 - Perform Integration Testing:
  RUN: docker-compose up -d
  TEST: Full booking flow via API and frontend
  VALIDATE: End-to-end workflows
 CHECK CONSOLE THEN RUN TESTS: Docker logs; fix container errors.

Task 12.3 - Optimize Performance:
  IMPLEMENT: Basic caching for availability checks
  TEST: API response times <300ms
  VALIDATE: Performance gates
 CHECK CONSOLE THEN RUN TESTS: Run performance tests; fix bottlenecks.

Task 12.4 - Deploy to Staging:
  RUN: scripts/deploy.sh staging
  VALIDATE: System available and functional
 CHECK CONSOLE THEN RUN TESTS: Monitor deploy script output; fix deployment errors.
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
  - twilio_sms: "Basic SMS delivery"
  - sendgrid_email: "Basic email notifications"

CACHING:
  - redis_sessions: "User session management"
  - api_cache: "Frequently accessed data caching"

MONITORING:
  - sentry: "Error tracking (optional for MVP)"
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

### Level 2: Unit Tests (90% Coverage Requirement)
```bash
# Backend comprehensive testing
cd backend
python -m pytest apps/ -v --cov=apps --cov-report=html --cov-fail-under=90

# Frontend testing
cd frontend
npm test -- --coverage --watchAll=false --coverageThreshold='{"global":{"branches":90,"functions":90,"lines":90,"statements":90}}'

# Performance testing
python -m pytest apps/appointments/tests/test_performance.py::test_booking_response_time
# Target: <300ms response time for appointment creation
```

### Level 3: Integration Testing
```bash
# Start complete system
docker-compose up -d
sleep 30  # Wait for services

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

# Expected: 201 Created, notification sent within 60s

# Test frontend booking flow
npx playwright test tests/booking-flow.spec.ts --headed
# Target: Complete end-to-end booking in <60 seconds
```

### Level 4: Performance & MVP Validation
```bash
# Load testing
artillery run tests/load-booking-system.yml
# Target: 500 concurrent users, <300ms P95 response time

# Security testing
bandit -r backend/apps/
safety check
npm audit

# GDPR compliance testing
python manage.py test apps.clients.tests.test_gdpr_compliance
# Target: Data export, anonymization, deletion workflows
```

## Final Validation Checklist
- [ ] All unit tests pass with 90%+ coverage
- [ ] Integration tests validate core workflows
- [ ] Performance requirements met: <300ms API responses
- [ ] Load testing passes: 500+ concurrent users
- [ ] Security scans show zero critical vulnerabilities
- [ ] GDPR compliance features working
- [ ] Basic notifications delivered within 60 seconds
- [ ] Mobile responsive design validated
- [ ] Production deployment successful
- [ ] Monitoring configured (optional)
- [ ] Database backups tested
- [ ] Foundation ready for post-MVP enhancements

---

## Anti-Patterns to Avoid
- ❌ Don't allow appointment conflicts - use database constraints
- ❌ Don't ignore timezone handling - always use timezone-aware datetime
- ❌ Don't skip input validation - sanitize all user inputs
- ❌ Don't use synchronous code in async context
- ❌ Don't hardcode business rules - make them configurable
- ❌ Don't skip error handling - handle all edge cases gracefully
- ❌ Don't compromise on test coverage - maintain 90% minimum
- ❌ Don't ignore performance - validate response times continuously
- ❌ Don't skip security scans - run automated security checks
- ❌ Don't ignore GDPR - implement proper data protection

## Confidence Score: 9/10
This revised PRP focuses on core MVP implementation with sequential tasks, deferred advanced features, and a streamlined stack (Django 5.2, React 18, PostgreSQL 17, Celery/Redis for basics). Tasks build logically, ensuring no forward dependencies, and align with your progress at Phase 4. Each task now includes explicit console error checks and fixes.
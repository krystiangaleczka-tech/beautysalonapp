# INITIAL_EXAMPLE.md - MarioBeautyApp

## FEATURE:
Build a comprehensive beauty salon management application using Django 5.2 LTS with Django-Ninja for API endpoints, React 18 with TypeScript 5.9 for the frontend, and PostgreSQL 17 for data persistence. The application should handle client management with detailed preference tracking, appointment scheduling with conflict prevention, automated SMS/email notifications via Celery background tasks, inventory management with auto-reorder alerts, staff management with performance analytics, and a real-time dashboard showing salon KPIs. The system must support multi-user authentication with role-based permissions (owner, manager, stylist, receptionist), integrate with Redis 7 for caching and session management, and be fully containerized with Docker Compose for easy deployment. The frontend should provide drag-and-drop appointment booking, client search with autocomplete, service customization with color formula tracking, and responsive design optimized for both desktop and tablet use in salon environments. Target: 4-person beauty salon team with future AI integration capabilities for client preference learning and intelligent scheduling recommendations.

## EXAMPLES:
### Backend Structure (Django + Django-Ninja)
- `salon/models.py` - Django ORM models for Client, Appointment, Service, Stylist, Product with proper relationships and constraints
- `salon/api.py` - Django-Ninja API endpoints with Pydantic schemas for type-safe JSON responses
- `salon/admin.py` - Django admin interface customization for salon management
- `salon/tasks.py` - Celery task definitions for SMS/email notifications and automated reports
- `salon/permissions.py` - Custom permission classes for role-based access control
- `requirements.txt` - Python dependencies including django-ninja, celery, redis, psycopg2-binary
- `docker-compose.yml` - Multi-container setup with web, db, cache, worker, scheduler, and frontend services

### Frontend Structure (React + TypeScript)
- `frontend/src/components/BookingCalendar.tsx` - Drag-and-drop calendar component with appointment management
- `frontend/src/components/ClientSearch.tsx` - Autocomplete client search with preference display
- `frontend/src/types/api.ts` - TypeScript interfaces matching Django-Ninja Pydantic schemas
- `frontend/src/hooks/useAppointments.ts` - React hooks for API state management
- `frontend/src/utils/dateHelpers.ts` - Utility functions for appointment scheduling logic
- `frontend/package.json` - Node.js dependencies including React 18, TypeScript 5.9, Tailwind CSS
- `frontend/Dockerfile` - React development and production build configuration

### Configuration Files
- `.env.example` - Environment variables template for database, Redis, email/SMS API keys
- `nginx/conf.d/default.conf` - Nginx configuration for static file serving and API routing
- `alembic.ini` - Database migration configuration
- `pytest.ini` - Testing configuration with coverage requirements

## DOCUMENTATION:
### Framework Documentation
- Django 5.2 LTS Documentation: https://docs.djangoproject.com/en/5.2/
- Django-Ninja Documentation: https://django-ninja.dev/
- React 18 Documentation: https://react.dev/
- TypeScript 5.9 Handbook: https://www.typescriptlang.org/docs/
- PostgreSQL 17 Documentation: https://www.postgresql.org/docs/17/

### Library Guides
- Celery Documentation: https://docs.celeryq.dev/en/stable/
- Redis Documentation: https://redis.io/docs/
- Pydantic V2 Documentation: https://docs.pydantic.dev/latest/
- Tailwind CSS Documentation: https://tailwindcss.com/docs
- pytest Documentation: https://docs.pytest.org/

### API Integration
- Google Calendar API v3: https://developers.google.com/calendar/api/v3/reference
- Twilio SMS API: https://www.twilio.com/docs/sms
- SendGrid Email API: https://docs.sendgrid.com/
- Stripe Payment API: https://stripe.com/docs/api (for future payment processing)

## SYSTEM ARCHITECTURE:

### 1. Authentication & Authorization
- Use Django's built-in authentication with custom user roles (extend AbstractUser)
- Implement JWT tokens for API authentication via Django-Ninja
- CORS configuration for React frontend communicating with Django backend
- Role-based access control (owner, manager, stylist, receptionist)
- GDPR-compliant user data management

### 2. Booking System
- Real-time availability checking with conflict prevention
- Appointment scheduling with service, staff, date and time selection
- Double-booking prevention with database-level constraints and optimistic locking
- 24-hour minimum cancellation policy
- Buffer time calculation (setup/cleanup between clients)

### 3. Calendar Integration
- Bi-directional synchronization with Google Calendar API v3
- Calendar conflict detection and resolution
- Staff schedule management (time blocks and availability)
- Timezone handling (store in UTC, display in salon's local time)

### 4. Notification System
- SMS reminders 24 hours before appointment
- Email confirmations and updates
- Admin notifications for changes
- Delivery status tracking with retry logic for failures
- Celery background tasks for reliable delivery

### 5. Client Management
- Detailed client profiles with preference tracking
- Color formula history and notes
- Allergy and sensitivity records
- Automatic client preference learning from appointment history
- Client search with autocomplete functionality

### 6. Admin Panel
- Staff appointment and calendar management
- Service pricing and package management
- Client history and CRM notes
- Basic financial reporting and data export

## DATABASE SCHEMA:
### Core Tables
- **Client**: id, name, email, phone, preferences (JSON), allergies (array), created_at, updated_at
- **Appointment**: id, client_id, stylist_id, service_id, start_time, end_time, status, notes
- **Service**: id, name, duration_minutes, base_price, category
- **Stylist**: id, user_id (FK to Django User), specialties (array), availability_schedule (JSON)
- **Product**: id, name, brand, quantity_current, quantity_threshold, cost, retail_price
- **Notification**: id, appointment_id, type, status, sent_at, delivered_at

### Business Rules & Constraints
1. **Customer Overlap Protection**: Customers cannot have overlapping appointments
2. **Staff Availability**: Appointments must be within staff working hours
3. **Service Duration**: End time must match start time + service duration
4. **Future Bookings Only**: Appointments cannot be created in the past
5. **Advance Booking**: Minimum 1 hour advance notice required
6. **Valid Contact Info**: Valid email and phone number required for bookings
7. **Cancellation Policy**: 24-hour minimum notice for cancellations

## SECURITY & COMPLIANCE:
- Rate limiting on API endpoints to prevent abuse
- Input validation and sanitization for all user data
- HTTPS enforcement with secure headers (HSTS, CSP, X-Frame-Options)
- GDPR compliance: right to deletion, data portability, audit trail
- Client data anonymization for analytics
- Encrypted backup storage with retention policies

## PERFORMANCE & DEPLOYMENT:
### Performance Requirements
- Database queries must use select_related/prefetch_related to avoid N+1 problems
- Redis caching for frequently accessed data (client lists, service menus)
- Appointment booking should respond within 200ms
- Frontend bundle size should be under 500KB gzipped

### Deployment Strategy
- Docker Compose for development (Django, Redis, PostgreSQL)
- Environment-specific settings files (development, staging, production)
- Static file collection and serving via nginx
- SSL certificate management and HTTPS enforcement
- Monitoring and logging setup with structured logs
- Database connection pooling for production load

## **AI INTEGRATION ROADMAP FUTURE**:
### Phase 1: Data Foundation (Current)
- Client preference tracking
- Service duration estimation based on client type
- Appointment history analysis

### Phase 2: Basic AI Features
- Intelligent service recommendations based on client history
- Optimal appointment time suggestions
- Client retention predictions

### Phase 3: Advanced AI
- Automated inventory forecasting and reordering
- Staff performance optimization
- Revenue prediction and business insights

## OTHER CONSIDERATIONS:
### Common Pitfalls to Avoid
- Handle concurrent appointment modifications gracefully
- Proper error handling for SMS/email delivery failures with retry logic
- Backup and restore procedures for PostgreSQL data
- Container health checks and restart policies in Docker Compose

### Cost Optimization
- Single PostgreSQL instance for 4-person team
- Efficient Redis usage for caching and sessions
- Optimized Celery worker configuration
- Minimal infrastructure overhead for small team operations
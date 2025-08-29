
The system implements enterprise security with multi-role authentication (owner, manager, stylist, receptionist), Redis 7 clustering for performance optimization, and full containerization via Docker Compose for scalable deployment.

**Strategic Vision**: Foundation for AI-powered salon operations with future capabilities for intelligent scheduling optimization, client behavior prediction, and automated business insights generation.
# INITIAL.md - MarioBeautyApp MVP Development Specification

## FEATURE OVERVIEW:
Build an MVP beauty salon management application for Mario's 4-person salon team using proven technology stack: Django 5.2 LTS with Django-Ninja for API endpoints, React 18 with TypeScript 5.9 for frontend development, and PostgreSQL 17 for data persistence.

The system implements core MVP functionality: client management, service catalog, staff scheduling, appointment booking, and basic notifications. Advanced features (AI, analytics, inventory) are deferred to post-MVP phases.

**Strategic Vision**: Solid MVP foundation that reduces manual work by 60% and enables online booking, with architecture ready for future AI and analytics enhancements.
=======

The system implements enterprise security with multi-role authentication (owner, manager, stylist, receptionist), Redis 7 clustering for performance optimization, and full containerization via Docker Compose for scalable deployment.

**Strategic Vision**: Foundation for AI-powered salon operations with future capabilities for intelligent scheduling optimization, client behavior prediction, and automated business insights generation.

---

## TECHNOLOGY STACK & ARCHITECTURE:

### Backend Infrastructure (Django MVP Stack)
```python
# Core Framework Stack (MVP Focus)
DJANGO_VERSION = "5.2"  # LTS for stability
DJANGO_NINJA_VERSION = "1.0+"  # Modern API framework
PYDANTIC_VERSION = "2.5+"  # Type validation
CELERY_VERSION = "5.3+"  # Background tasks (basic notifications)
REDIS_VERSION = "7.2+"  # Caching and task queue
POSTGRESQL_VERSION = "17"  # Database

# MVP Dependencies (Simplified)
dependencies = [
    "django==5.2",
    "django-ninja>=1.0",
    "pydantic>=2.5",
    "celery[redis]>=5.3",
    "psycopg2-binary>=2.9",
    "django-redis>=5.4",
    "django-cors-headers>=4.3",
    "djangorestframework-simplejwt>=5.3",
    "python-decouple>=3.8",
]
```

### Frontend Architecture (React + TypeScript)
```typescript
// React Ecosystem (Stable Versions)
const techStack = {
  react: "18.2",  // Stable version for MVP
  typescript: "5.9",
  vite: "5.0+",
  tailwindcss: "3.4+",
  reactQuery: "5.0+",
  reactHookForm: "7.48+",
  reactRouter: "6.20+",
  lucideReact: "0.300+",
};
```

---

## MVP SYSTEM ARCHITECTURE:

### 1. Basic Authentication & Authorization
```python
# Simple User Model with Role-Based Access
class SalonUser(AbstractUser):
    ROLE_CHOICES = [
        ('owner', 'Salon Owner'),
        ('staff', 'Staff Member'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    is_active_staff = models.BooleanField(default=False)
    
    @property
    def can_manage_appointments(self):
        return self.role in ['owner', 'staff']
```

### 2. Core Appointment System with Conflict Prevention
```python
# Basic Appointment Management
class AppointmentManager(models.Manager):
    def check_availability(self, staff_member, start_time, duration):
        """Basic availability checking"""
        end_time = start_time + duration
        
        conflicts = self.filter(
            staff_member=staff_member,
            start_time__lt=end_time,
            end_time__gt=start_time,
            status='confirmed'
        ).exists()
        
        return not conflicts

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    staff_member = models.ForeignKey('SalonUser', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    
    objects = AppointmentManager()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['staff_member', 'start_time'],
                name='no_double_booking'
            ),
            models.CheckConstraint(
                check=models.Q(end_time__gt=models.F('start_time')),
                name='valid_time_range'
            )
        ]
```

### 3. Basic Notification System
```python
# Simple Notification Pipeline
@shared_task(bind=True, max_retries=3)
def send_appointment_notification(self, appointment_id, notification_type):
    """Basic notification delivery"""
    try:
        appointment = Appointment.objects.select_related(
            'client', 'staff_member', 'service'
        ).get(id=appointment_id)
        
        # Email notification
        if notification_type == 'confirmation':
            send_mail(
                subject=f'Appointment Confirmed - {appointment.service.name}',
                message=f'Your appointment is confirmed for {appointment.start_time}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[appointment.client.email],
            )
        
        # SMS notification (optional)
        if appointment.client.phone and notification_type in ['reminder', 'confirmation']:
            # Basic SMS integration would go here
            pass
            
    except Exception as exc:
        logger.error(f'Notification failed: {exc}')
        raise self.retry(countdown=60 * (2 ** self.request.retries))
```

### 4. Basic Client Management
```python
# Simple Client Profiles
class Client(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    
    # Basic Preferences
    allergies = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
```
        self.service_history.append(service_data)
        self.save()
```

---

## DATABASE SCHEMA & BUSINESS RULES:

### Core Entity Relationships
```sql
-- Enterprise Database Design
CREATE TABLE salon_clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    hair_type VARCHAR(50),
    color_preferences JSONB DEFAULT '{}',
    allergies JSONB DEFAULT '[]',
    service_history JSONB DEFAULT '[]',
    lifetime_value DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE salon_appointments (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES salon_clients(id),
    stylist_id INTEGER REFERENCES auth_user(id),
    service_id INTEGER REFERENCES salon_services(id),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    total_price DECIMAL(10,2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Business Rule Constraints
    CONSTRAINT no_time_overlap EXCLUDE USING gist (
        stylist_id WITH =,
        tstzrange(start_time, end_time) WITH &&
    ) WHERE (status IN ('confirmed', 'in_progress')),
    
    CONSTRAINT valid_time_range CHECK (end_time > start_time),
    CONSTRAINT future_appointments CHECK (start_time > NOW() - INTERVAL '1 hour')
);

-- Performance Indexes
CREATE INDEX idx_appointments_stylist_time ON salon_appointments 
    USING btree (stylist_id, start_time) 
    WHERE status IN ('confirmed', 'in_progress');
```

---

## FRONTEND ARCHITECTURE & COMPONENTS:

### React Component Structure
```typescript
// Enterprise React Architecture
interface AppointmentBookingProps {
  clientId?: string;
  preSelectedService?: string;
  onSuccess?: (appointment: Appointment) => void;
}

export const AppointmentBooking: React.FC<AppointmentBookingProps> = ({
  clientId,
  preSelectedService,
  onSuccess
}) => {
  // React Query for server state management
  const { data: services } = useQuery({
    queryKey: ['services'],
    queryFn: () => api.services.getAll(),
    staleTime: 1000 * 60 * 5, // 5 minutes
  });

  // Form management with React Hook Form
  const {
    control,
    handleSubmit,
    watch,
    formState: { errors, isSubmitting }
  } = useForm<AppointmentFormData>({
    resolver: zodResolver(appointmentSchema),
    defaultValues: {
      serviceId: preSelectedService,
      clientId: clientId,
    }
  });

  // Optimistic updates for better UX
  const createAppointmentMutation = useMutation({
    mutationFn: api.appointments.create,
    onMutate: async (newAppointment) => {
      await queryClient.cancelQueries({ queryKey: ['appointments'] });
      const previousAppointments = queryClient.getQueryData(['appointments']);
      
      queryClient.setQueryData(['appointments'], (old: Appointment[]) => [
        ...old,
        { ...newAppointment, id: 'temp-' + Date.now(), status: 'pending' }
      ]);
      
      return { previousAppointments };
    },
    onError: (err, newAppointment, context) => {
      queryClient.setQueryData(['appointments'], context?.previousAppointments);
      toast.error('Failed to create appointment. Please try again.');
    },
    onSuccess: (appointment) => {
      queryClient.invalidateQueries({ queryKey: ['appointments'] });
      onSuccess?.(appointment);
      toast.success('Appointment created successfully!');
    }
  });

  return (
    <form onSubmit={handleSubmit(createAppointmentMutation.mutate)}>
      <ServiceSelector control={control} services={services} />
      <StylistSelector control={control} selectedService={watch('serviceId')} />
      <DateTimePicker control={control} selectedStylist={watch('stylistId')} />
      <SubmitButton isLoading={isSubmitting}>Book Appointment</SubmitButton>
    </form>
  );
};
```

---

## SECURITY & COMPLIANCE FRAMEWORK:

### Enterprise Security Implementation
```python
# GDPR Compliance & Data Protection
class GDPRCompliantManager:
    def anonymize_client_data(self, client_id):
        """GDPR Article 17 - Right to be forgotten"""
        client = Client.objects.get(id=client_id)
        
        # Anonymize personal data
        client.first_name = f"Client_{client.id}"
        client.last_name = "Deleted"
        client.email = f"deleted_{client.id}@example.com"
        client.phone = "000-000-0000"
        
        # Keep business data for analytics (anonymized)
        client.service_history = self.anonymize_service_history(client.service_history)
        client.save()

# Input Validation & Sanitization
from pydantic import BaseModel, validator

class AppointmentCreateSchema(BaseModel):
    client_id: int
    stylist_id: int
    service_id: int
    start_time: datetime
    notes: Optional[str] = ""
    
    @validator('start_time')
    def validate_future_time(cls, v):
        if v <= datetime.now(tz=timezone.utc):
            raise ValueError('Appointment must be in the future')
        return v
    
    @validator('notes')
    def sanitize_notes(cls, v):
        return bleach.clean(v, tags=[], strip=True)
```

---

## PRODUCTION DEPLOYMENT:

### Docker Configuration
```yaml
# docker-compose.production.yml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile.prod
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
      - DEBUG=False
    volumes:
      - static_volume:/app/staticfiles
    depends_on:
      - db
      - redis
    restart: unless-stopped

  db:
    image: postgres:17-alpine
    environment:
      - POSTGRES_DB=mario_salon
      - POSTGRES_USER=salon_user
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    restart: unless-stopped

  celery:
    build: .
    command: celery -A config worker -l info --concurrency=4
    depends_on:
      - db
      - redis
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  static_volume:
```

### Performance Requirements
- Database queries must use select_related/prefetch_related to avoid N+1 problems
- Redis caching for frequently accessed data (client lists, service menus)
- Appointment booking should respond within 200ms
- Frontend bundle size should be under 500KB gzipped

### AI Integration Roadmap
**Phase 1**: Client preference tracking and service duration estimation
**Phase 2**: Intelligent service recommendations and optimal appointment time suggestions
**Phase 3**: Automated inventory forecasting and staff performance optimization

---

## DOCUMENTATION REFERENCES:
- Django 5.2 LTS: https://docs.djangoproject.com/en/5.2/
- Django-Ninja: https://django-ninja.dev/
<<<<<<< HEAD
- React 18: https://react.dev/
=======
- TypeScript 5.9: https://www.typescriptlang.org/docs/
- PostgreSQL 17: https://www.postgresql.org/docs/17/
- Celery: https://docs.celeryq.dev/en/stable/
- Redis: https://redis.io/docs/
- Google Calendar API: https://developers.google.com/calendar/api/v3/reference
- Twilio SMS API: https://www.twilio.com/docs/sms
- SendGrid Email API: https://docs.sendgrid.com/
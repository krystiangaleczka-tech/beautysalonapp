# FEATURE CONTEXT

## User Journeys

### Client Booking Journey (MVP)
1. **Service Selection**
   - Browse available services (nails, skincare, podology, eyelashes)
   - View basic service descriptions and pricing
   - Select preferred service

2. **Appointment Scheduling**
   - Choose available date from calendar
   - Select from available time slots
   - Choose staff member or "any available"
   - Confirm booking details

3. **Booking Confirmation**
   - Receive booking confirmation via email
   - View appointment details
   - Option to cancel or reschedule

### Staff Daily Workflow (MVP)
1. **Daily Schedule Review**
   - Login to staff dashboard
   - View today's appointments
   - Check client information and notes

2. **Appointment Management**
   - Mark appointments as completed
   - Add basic notes about services
   - Update appointment status

3. **Basic Client Interaction**
   - View client contact information
   - Access appointment history
   - Schedule follow-up appointments

### Salon Owner Management Journey (MVP)
1. **Daily Operations**
   - View daily appointment schedule
   - Monitor overall booking status
   - Check staff schedules

2. **Client Management**
   - Add new clients to system
   - Update client information
   - View client appointment history

3. **Service Management**
   - Manage service catalog and pricing
   - Update staff availability
   - Basic appointment oversight

## Business Rules

### Appointment Scheduling Rules (MVP)
- **Booking Window**: Clients can book up to 30 days in advance
- **Cancellation Policy**: 24-hour notice required for cancellations
- **Same-Day Booking**: Available until 2 hours before appointment
- **Conflict Prevention**: System prevents double-booking automatically
- **Buffer Time**: 15-minute buffer between appointments

### Service Duration and Pricing (MVP)
- **Standard Services**: Manicure 45min, Pedicure 60min, Facial 90min, Eyelashes 120min
- **Fixed Pricing**: Set prices per service type
- **Payment**: Payment completed at time of service

### Staff Scheduling Rules (MVP)
- **Working Hours**: 9 AM - 6 PM business hours
- **Availability**: Staff set their available days/times
- **Appointment Assignment**: Automatic or manual assignment to available staff

### Data Privacy Rules (MVP)
- **Client Data**: Basic contact information and appointment history
- **Data Retention**: Standard business retention policies
- **GDPR Compliance**: Basic right to access and delete data

## API Contracts

### Authentication Endpoints
```typescript
// JWT Authentication
POST /api/auth/login
Request: { email: string, password: string, mfa_code?: string }
Response: { access_token: string, refresh_token: string, user: UserProfile }

POST /api/auth/refresh
Request: { refresh_token: string }
Response: { access_token: string }

POST /api/auth/logout
Headers: { Authorization: "Bearer {token}" }
Response: { success: boolean }
```

### Appointment Management
```typescript
// Get Available Slots
GET /api/appointments/availability
Query: { date: Date, service_id: string, therapist_id?: string, duration: number }
Response: { slots: TimeSlot[], next_available: Date }

// Create Appointment
POST /api/appointments
Request: {
  client_id: string,
  service_id: string,
  therapist_id: string,
  start_time: DateTime,
  duration: number,
  notes?: string,
  add_ons?: string[]
}
Response: { appointment: Appointment, payment_required: boolean }

// Update Appointment
PATCH /api/appointments/{id}
Request: { start_time?: DateTime, notes?: string, status?: AppointmentStatus }
Response: { appointment: Appointment, conflicts?: ConflictWarning[] }

// Cancel Appointment
DELETE /api/appointments/{id}
Query: { reason: string, refund_requested: boolean }
Response: { success: boolean, refund_amount?: number, refund_timeline?: string }
```

### Client Management
```typescript
// Client Profile
GET /api/clients/{id}
Response: {
  client: {
    id: string,
    personal_info: PersonalInfo,
    preferences: ServicePreferences,
    history: ServiceHistory[],
    loyalty_points: number,
    allergies?: string[],
    notes?: string
  }
}

// Update Client Profile
PATCH /api/clients/{id}
Request: Partial<ClientProfile>
Response: { client: ClientProfile }

// Client Service History
GET /api/clients/{id}/history
Query: { limit?: number, offset?: number, service_type?: string }
Response: { history: ServiceRecord[], total: number, pagination: PaginationInfo }
```

### Service Catalog
```typescript
// Get Services
GET /api/services
Query: { category?: string, therapist_id?: string, available_only?: boolean }
Response: {
  services: {
    id: string,
    name: string,
    description: string,
    duration: number,
    price: Price,
    category: ServiceCategory,
    requirements?: string[],
    add_ons?: ServiceAddon[]
  }[]
}

// Service Details
GET /api/services/{id}
Response: {
  service: ServiceDetails,
  available_therapists: TherapistInfo[],
  reviews: ServiceReview[],
  frequently_booked_with: Service[]
}
```

### Staff Management
```typescript
// Staff Schedule
GET /api/staff/{id}/schedule
Query: { start_date: Date, end_date: Date }
Response: {
  schedule: {
    date: Date,
    shifts: {
      start_time: DateTime,
      end_time: DateTime,
      appointments: AppointmentSummary[],
      breaks: Break[]
    }[]
  }[]
}

// Update Availability
PATCH /api/staff/{id}/availability
Request: {
  date: Date,
  available_slots: TimeSlot[],
  unavailable_reason?: string
}
Response: { updated_schedule: Schedule, conflicts?: ConflictWarning[] }

// Performance Metrics
GET /api/staff/{id}/metrics
Query: { period: 'week' | 'month' | 'quarter' }
Response: {
  metrics: {
    appointments_completed: number,
    revenue_generated: number,
    client_satisfaction: number,
    no_shows: number,
    commission_earned: number
  }
}
```

### Payment Processing
```typescript
// Process Payment
POST /api/payments
Request: {
  appointment_id: string,
  amount: number,
  payment_method: PaymentMethod,
  tip_amount?: number,
  save_payment_method?: boolean
}
Response: {
  payment: PaymentRecord,
  receipt_url: string,
  loyalty_points_earned?: number
}

// Refund Payment
POST /api/payments/{id}/refund
Request: { amount: number, reason: string }
Response: {
  refund: RefundRecord,
  refund_timeline: string,
  updated_appointment: Appointment
}
```

### Business Analytics
```typescript
// Revenue Dashboard
GET /api/analytics/revenue
Query: { start_date: Date, end_date: Date, group_by?: 'day' | 'week' | 'month' }
Response: {
  revenue_data: RevenueDataPoint[],
  total_revenue: number,
  growth_rate: number,
  top_services: ServiceRevenue[]
}

// Client Analytics
GET /api/analytics/clients
Query: { period: 'month' | 'quarter' | 'year' }
Response: {
  new_clients: number,
  returning_clients: number,
  retention_rate: number,
  average_spend: number,
  lifetime_value: number
}

// Staff Performance
GET /api/analytics/staff
Query: { staff_id?: string, period: 'week' | 'month' | 'quarter' }
Response: {
  staff_metrics: StaffMetrics[],
  team_averages: TeamAverages,
  top_performers: StaffRanking[]
}
```

### Notification System
```typescript
// Send Notification
POST /api/notifications
Request: {
  recipient_type: 'client' | 'staff' | 'admin',
  recipient_id: string,
  message: NotificationMessage,
  channels: ('email' | 'sms' | 'push' | 'in_app')[],
  scheduled_time?: DateTime
}
Response: { notification_id: string, delivery_status: DeliveryStatus }

// Notification Preferences
GET /api/notifications/preferences/{user_id}
Response: {
  preferences: {
    appointment_reminders: NotificationChannels,
    marketing_messages: NotificationChannels,
    service_updates: NotificationChannels,
    emergency_alerts: NotificationChannels
  }
}
```

## Data Models

### Core Entities
```typescript
interface Appointment {
  id: string;
  client_id: string;
  therapist_id: string;
  service_id: string;
  start_time: DateTime;
  end_time: DateTime;
  status: 'scheduled' | 'confirmed' | 'in_progress' | 'completed' | 'cancelled' | 'no_show';
  notes?: string;
  add_ons: string[];
  total_price: number;
  payment_status: 'pending' | 'paid' | 'refunded';
  created_at: DateTime;
  updated_at: DateTime;
}

interface Client {
  id: string;
  personal_info: {
    first_name: string;
    last_name: string;
    email: string;
    phone: string;
    date_of_birth?: Date;
    gender?: 'female' | 'male' | 'other' | 'prefer_not_to_say';
  };
  preferences: {
    preferred_therapist_id?: string;
    communication_channels: ('email' | 'sms' | 'push')[];
    language: string;
    allergies?: string[];
    skin_type?: string;
    special_requirements?: string;
  };
  loyalty_info: {
    points_balance: number;
    tier: 'regular' | 'silver' | 'gold' | 'platinum';
    member_since: Date;
  };
  gdpr_consent: {
    marketing: boolean;
    data_processing: boolean;
    photo_consent: boolean;
    consent_date: DateTime;
  };
}

interface Staff {
  id: string;
  personal_info: {
    first_name: string;
    last_name: string;
    email: string;
    phone: string;
    employee_id: string;
  };
  professional_info: {
    certifications: Certification[];
    specializations: string[];
    experience_years: number;
    languages: string[];
    bio?: string;
    photo_url?: string;
  };
  schedule_info: {
    default_working_hours: WorkingHours;
    timezone: string;
    calendar_sync_enabled: boolean;
  };
  employment_info: {
    hire_date: Date;
    role: 'therapist' | 'senior_therapist' | 'manager' | 'admin';
    commission_rate: number;
    hourly_rate?: number;
    status: 'active' | 'inactive' | 'on_leave';
  };
}
```

### Business Logic Types
```typescript
type ServiceCategory = 'nails' | 'skincare' | 'podology' | 'eyelashes' | 'hair' | 'massage' | 'other';

type AppointmentStatus = 'scheduled' | 'confirmed' | 'in_progress' | 'completed' | 'cancelled' | 'no_show';

type PaymentMethod = 'card' | 'cash' | 'mobile' | 'gift_certificate' | 'loyalty_points';

interface TimeSlot {
  start_time: DateTime;
  end_time: DateTime;
  available: boolean;
  therapist_id?: string;
}

interface ConflictWarning {
  type: 'overlap' | 'break_violation' | 'availability' | 'certification';
  message: string;
  affected_appointments?: string[];
  suggested_alternatives?: TimeSlot[];
}
```
# FEATURE CONTEXT

## User Journeys

### Client Booking Journey
1. **Service Discovery**
   - Browse available services by category (nails, skincare, podology, eyelashes)
   - View service descriptions, duration, and pricing
   - Filter by price range, duration, or therapist preference
   - Read service reviews and therapist profiles

2. **Appointment Scheduling**
   - Select preferred date from calendar widget
   - View real-time availability slots
   - Choose specific therapist or "any available"
   - Select appointment duration and add-ons
   - Confirm personal details and contact preferences

3. **Booking Confirmation**
   - Receive immediate booking confirmation
   - Add appointment to personal calendar
   - Set reminder preferences (SMS, email, push)
   - Access booking details and modification options

4. **Pre-Appointment**
   - Receive automated reminder notifications
   - Complete intake forms or questionnaires
   - Request appointment modifications if needed
   - Access salon location and parking information

5. **Post-Appointment**
   - Rate service experience and therapist
   - Rebook future appointments with preferred therapist
   - Access service history and recommendations
   - Participate in loyalty program activities

### Staff Daily Workflow
1. **Shift Start**
   - Login to staff dashboard
   - Review daily schedule and client notes
   - Check inventory levels for services
   - Update availability for walk-ins

2. **Client Management**
   - Access comprehensive client profiles
   - Update service notes and recommendations
   - Process payments and tip collection
   - Schedule follow-up appointments

3. **Service Delivery**
   - Mark appointment start/completion
   - Update service duration if needed
   - Add photos for before/after documentation
   - Process product sales and recommendations

4. **Shift End**
   - Complete daily sales summary
   - Update inventory usage
   - Review tomorrow's schedule
   - Submit time tracking and notes

### Salon Owner Management Journey
1. **Daily Operations**
   - Review daily/weekly revenue dashboard
   - Monitor staff performance metrics
   - Manage appointment scheduling conflicts
   - Process inventory orders and alerts

2. **Staff Management**
   - Create staff schedules and vacation management
   - Track individual performance and commissions
   - Manage training requirements and certifications
   - Handle staff communication and announcements

3. **Business Analysis**
   - Generate financial reports and trends
   - Analyze client retention and satisfaction
   - Review service popularity and profitability
   - Monitor marketing campaign effectiveness

4. **System Administration**
   - Configure salon settings and policies
   - Manage service catalog and pricing
   - Set up promotional campaigns and discounts
   - Maintain client communication templates

## Business Rules

### Appointment Scheduling Rules
- **Booking Window**: Clients can book up to 90 days in advance
- **Cancellation Policy**: 24-hour cancellation notice required for full refund
- **No-Show Policy**: 2 no-shows result in advance payment requirement
- **Same-Day Booking**: Available until 2 hours before desired appointment
- **Double Booking Prevention**: System prevents overlapping appointments automatically

### Service Duration and Pricing
- **Base Service Times**: Manicure 45min, Pedicure 60min, Facial 90min, Eyelashes 120min
- **Buffer Time**: 15-minute buffer between appointments for cleanup
- **Overtime Handling**: Services can extend up to 30 minutes with automatic billing
- **Group Bookings**: Maximum 4 people for synchronized services
- **Pricing Tiers**: Regular, Premium, VIP pricing based on therapist experience

### Staff Scheduling Rules
- **Minimum Notice**: 48-hour notice required for schedule changes
- **Maximum Hours**: 8-hour daily limit, 40-hour weekly limit per staff member
- **Break Requirements**: 30-minute break required for shifts over 6 hours
- **Certification Requirements**: Services can only be performed by certified staff
- **Commission Structure**: 40% commission on services, 15% on product sales

### Payment and Refund Rules
- **Payment Methods**: Card, cash, mobile payments, gift certificates accepted
- **Deposit Requirements**: 50% deposit required for services over €100
- **Refund Timeline**: Refunds processed within 5-7 business days
- **Tip Handling**: Digital tip processing with 100% to service provider
- **Late Payment**: Services require payment completion before start

### Data Privacy Rules
- **Client Consent**: Explicit consent required for photo documentation
- **Data Retention**: Client data retained for 3 years after last service
- **Marketing Consent**: Separate consent required for marketing communications
- **Right to Erasure**: Complete data deletion within 30 days of request
- **Access Control**: Staff can only access assigned client information

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
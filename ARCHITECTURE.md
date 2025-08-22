# Beauty Salon Booking System – Architecture

A comprehensive application for a beauty salon with Google Calendar integration, SMS notifications, and financial reporting. BMAD method integration for business analysis is included.

## System Overview

Kompleksowa aplikacja do rezerwacji w salonie kosmetycznym z integracją Google Calendar, powiadomieniami SMS oraz raportowaniem finansowym. Metodyka BMAD (Business Model Analysis and Design) jest zaimplementowana przez dedykowane skrypty Node.js.

## Architecture Diagram

graph TB
Client[Client Browser] --> LoadBalancer[Load Balancer]
LoadBalancer --> Django[Django Application]

React[React.js with TypeScript] -->|API calls| BookingAPI[Booking API]
React -->|API calls| Auth[Authentication Service]
React -->|API calls| NotificationService[Notification Service]
React -->|API calls| ReportingService[Reporting Service]

Django --> Database[(SQLite / PostgreSQL)]
Django --> Redis[(Redis Cache)]
Django --> Celery[Celery Workers]

Celery --> SMSProvider[SMS API Provider]
Celery --> GoogleAPI[Google Calendar API v3]

Django --> StaticFiles[Static Files CDN]

subgraph "Frontend Stack"
    React[React.js with TypeScript]
    Tailwind[TailwindCSS]
end

subgraph "Backend Services"
    Auth[Authentication Service]
    BookingAPI[Booking API]
    CalendarSync[Calendar Sync Service]
    NotificationService[Notification Service]
    ReportingService[Reporting Service]
end

subgraph "BMAD Integration"
    NodeJS[Node.js CLI]
    BMAD[BMAD Method Scripts]
end

BMAD --> NodeJS
NodeJS -->|calls| BookingAPI
NodeJS -->|pulls| CalendarSync


## Technology Stack

### Backend
- **Framework**: Django 4.2+ z Django REST Framework  
- **Database**: SQLite (development) → PostgreSQL (production)  
- **Cache/Queue**: Redis  
- **Task Queue**: Celery  
- **Authentication**: Django built-in auth + JWT dla API  

### Frontend
- **Framework**: React.js z TypeScript  
- **UI**: responsywne, mobile-first  
- **CSS**: TailwindCSS  
- **Bundling**: Webpack lub Vite dla optymalizacji zasobów  

### BMAD Integration
- **Node.js CLI**: `npx bmad-method install`  
- **Commands**:  
  - `git pull origin main`  
  - `npm run install:bma`  
- **Function**: Automatyzuje analizę modelu biznesowego i generuje raporty KPI  

### Integrations
- **Calendar**: Google Calendar API v3  
- **SMS**: SerwerSMS lub inny polski SMS provider  
- **Email**: Django Email Backend  

### Infrastructure
- **Development**: Docker (Django, Redis, PostgreSQL lokalnie)  
- **Staging/Production**: PythonAnywhere → Render/Railway  
- **Monitoring**: Django logging + zewnętrzna usługa monitorująca  
- **Backup**: automatyczne codzienne snapshoty bazy danych + przechowywanie w chmurze  

## System Components

### 1. Authentication & Authorization
- Role-based access control (Client, Employee, Admin)  
- JWT tokens dla API, sesje dla web UI  
- GDPR-compliant user data management  

### 2. Booking System
- Sprawdzanie dostępności w czasie rzeczywistym  
- Harmonogramowanie wizyt z wyborem usługi, pracownika, daty i godziny  
- Konfliktowanie terminów i automatyczne rozwiązywanie  
- Polityka anulowania 24h przed wizytą  

### 3. Calendar Integration
- Dwukierunkowa synchronizacja z Google Calendar API v3  
- Wykrywanie i rozwiązywanie konfliktów w kalendarzu  
- Zarządzanie harmonogramem pracowników (blokady czasowe)  

### 4. Notification System
- SMS przypomnienia 24h przed wizytą  
- E-mail potwierdzenia i aktualizacje  
- Powiadomienia admina o zmianach  
- Śledzenie statusu dostarczenia  

### 5. Financial Reporting
- Obliczenia przychodów w czasie rzeczywistym  
- Analiza rentowności usług  
- Raporty miesięczne / kwartalne  
- Eksport danych (CSV, Excel)  

### 6. Admin Panel
- Zarządzanie wizytami i kalendarzami pracowników  
- Edycja czasu i anulowanie wizyt  
- Zarządzanie cennikiem i pakietami usług  
- CRM: historia klientów i notatki  
- Eksport danych do księgowości  

## Database Schema

### Core Models
- **User** (klient, pracownik, administrator)  
- **Service** (usługa, cena, czas trwania, opis)  
- **Appointment** (wizyty powiązane z użytkownikami i usługami)  
- **Employee** (specjalizacje, grafiki)  
- **Schedule** (godziny pracy i dostępność)  
- **Notification** (logi SMS / e-mail)  
- **FinancialRecord** (przychody, zmiany cen)  
- **Setting** (konfiguracja systemu)  

### Relationships
- User 1:N Appointments  
- Service 1:N Appointments  
- Employee 1:N Appointments  
- Appointment 1:N Notifications  
- Service 1:N FinancialRecords  

## Security Considerations

### Data Protection
- GDPR: eksport i usuwanie danych  
- Szyfrowanie wrażliwych pól  
- Bezpieczne hasła, dwuetapowe logowanie opcjonalne  

### Application Security
- CSRF protection, XSS prevention, SQL injection via ORM  
- Rate limiting API  
- Walidacja i sanitization inputu  

### Infrastructure Security
- HTTPS enforcement  
- Secure headers (HSTS, CSP, X-Frame-Options)  
- Regularne aktualizacje  
- Rotacja kluczy API  

## Performance Requirements

- Rezerwacja < 30 s  
- Panel admin < 2 s  
- Synchronizacja kalendarza < 5 s  
- Dostarczenie SMS < 30 s  
- 100+ concurrent users  
- 99.9% uptime SLA  
- Auto-scaling  

## Deployment Strategy

### Development
- Docker Compose (Django, Redis, PostgreSQL)  
- Hot reload, test coverage > 80%  

### Production
- Blue-green deployments  
- Automated CI/CD z GitHub Actions with 2 branches [main(for develop), test(for testing)]
- Automatyczne migracje z rollback  
- Monitoring + alerting  

### Backup Strategy
- Codzienne snapshoty bazy  
- Przechowywanie backupów w AWS S3 lub innym storage  
- Testowanie przywracania danych co miesiąc  

## API Design

### Endpoints
- `/api/auth/`  
- `/api/appointments/`  
- `/api/services/`  
- `/api/calendar/`  
- `/api/notifications/`  
- `/api/reports/`  

### Response Format
{
"status": "success|error",
"data": {},
"message": "Opis sytuacji",
"meta": {
"pagination": {},
"timestamp": "ISO8601"
}
}

## Error Handling Strategy

- 4xx: walidacja, authentication errors, rate limits  
- 5xx: fallback, logging, automatyczne recovery  

## Monitoring & Logging

- Metryki wydajności, error rate, biznesowe (bookings, revenue)  
- Zasoby infrastruktury, kolejki zadań, czas odpowiedzi zewnętrznych API  
- Alerty: błędy krytyczne, anomalie biznesowe, threshold breaches  


## ADDON to DATABASE_SCHEMA.md
## Data Integrity Constraints

### Business Rules
1. **Appointment overlap protection for customer**: Customer can not apply overlapping appointments.
2. **Appointment Overlap By Employee**: Only employee can overlap appointments.
3. **Employee Availability**: Appointments must be within employee availability.
4. **Working Hours Validation**: Appointments must be within employee working hours
5. **Service Duration**: End time must match start time + service duration
6. **Future Bookings Only**: Appointments cannot be created in the past
7. **Cancellation Policy**: 24-hour minimum notice for cancellations
8. **Appointment Status**: Appointments can be marked as 'anulowane', 'zmienione', etc.
9. **Notification Status**: Notifications can be marked as 'wysłane', 'dostarczone', etc.
10. **Booking only with valid email**: Only valid emails can book appointments.
11. **Booking advance** : Booking can only be confirmed with at least 1 hour’s in advance by customer.
12. **Booking only with valid phone number**: Only valid phone numbers can book appointments.
### Foreign Key Constraints
- All relationships use `CASCADE` or `PROTECT` appropriately
- User deletion requires data anonymization process
- Service deletion requires appointment status check

## GDPR Compliance Features

### Data Export
- Complete user data export in JSON format
- Appointment history with all related data
- Notification and communication history

### Data Deletion
- Soft delete with anonymization option
- Retention policies for financial records
- Audit trail maintenance

### Data Minimization
- Optional fields for non-essential information
- Automatic cleanup of old notification logs
- Configurable data retention periods_
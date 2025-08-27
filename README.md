# Mario Beauty Salon Management System

## 🏪 Project Overview

Enterprise-grade beauty salon management system built with Django 5.2 LTS + React 18 + PostgreSQL 17. This system provides comprehensive salon operations management including intelligent appointment scheduling, client management, staff coordination, and business analytics.

## 🚀 Tech Stack

### Backend
- **Framework**: Django 5.2 LTS
- **API**: Django-Ninja (FastAPI-style for Django)
- **Database**: PostgreSQL 17 (SQLite for local development)
- **Cache**: Redis 7
- **Task Queue**: Celery
- **Authentication**: JWT with role-based permissions

### Frontend
- **Framework**: React 18 with TypeScript 5.9
- **Build Tool**: Vite 5.0
- **Styling**: Tailwind CSS 3.4 (Beauty salon theme)
- **State Management**: React Query + Zustand
- **UI Components**: Headless UI + Radix UI
- **Forms**: React Hook Form + Zod validation

## 📁 Project Structure

```
beautysalonapp/
├── .agent-os/                  # Agent OS development system
├── backend/                    # Django backend application
│   ├── config/                 # Django configuration
│   │   ├── settings/           # Environment-specific settings
│   │   ├── urls.py            # Main URL configuration
│   │   ├── wsgi.py            # WSGI application
│   │   └── asgi.py            # ASGI application
│   ├── apps/                   # Django applications
│   │   ├── core/              # Common functionality
│   │   ├── authentication/    # User management
│   │   ├── clients/           # Client management
│   │   ├── appointments/      # Appointment system
│   │   ├── services/          # Service catalog
│   │   ├── staff/             # Staff management
│   │   ├── notifications/     # Multi-channel notifications
│   │   ├── inventory/         # Inventory management
│   │   └── analytics/         # Business analytics
│   ├── requirements/          # Python dependencies
│   │   ├── base.txt          # Core dependencies
│   │   ├── development.txt   # Development tools
│   │   └── production.txt    # Production optimizations
│   └── manage.py              # Django management script
├── frontend/                   # React frontend application
│   ├── src/                   # Source code
│   │   ├── components/        # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── hooks/            # Custom hooks
│   │   ├── utils/            # Utility functions
│   │   ├── types/            # TypeScript definitions
│   │   └── api/              # API client
│   ├── package.json          # Node.js dependencies
│   ├── vite.config.ts        # Vite configuration
│   ├── tailwind.config.ts    # Tailwind CSS configuration
│   └── tsconfig.json         # TypeScript configuration
├── context/                    # Context engineering docs
│   ├── PROJECT_CONTEXT.md    # Business requirements
│   ├── TECHNICAL_CONTEXT.md  # Architecture decisions
│   └── FEATURE_CONTEXT.md    # User journeys & API contracts
├── con_eng/                   # Context engineering framework
├── INITIAL.md                 # Technical specification
├── DESIGNSYSTEM.md           # UI/UX design system
└── setup.sh                  # Development setup script
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 17 (optional for local development)
- Redis 7 (optional for local development)

### Quick Start

1. **Clone and setup the project:**
   ```bash
   git clone <repository-url>
   cd beautysalonapp
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Start the development servers:**

   **Backend (Terminal 1):**
   ```bash
   cd backend
   source venv/bin/activate
   python manage.py runserver
   ```

   **Frontend (Terminal 2):**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the applications:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api
   - API Documentation: http://localhost:8000/api/docs
   - Django Admin: http://localhost:8000/admin

### Manual Setup

If you prefer manual setup:

**Backend Setup:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Frontend Setup:**
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## 🏗️ Architecture

### Enterprise Patterns
- **Domain-Driven Design**: Clear business domain separation
- **CQRS**: Command Query Responsibility Segregation
- **API-First**: Django-Ninja for high-performance APIs
- **Microservices Ready**: Independent app scaling capability

### Security Features
- JWT authentication with refresh tokens
- Role-based access control (Owner, Manager, Stylist, Receptionist)
- GDPR compliance features
- Input validation and sanitization
- CORS and security headers

### Performance Features
- Redis caching for session management
- Database connection pooling
- Optimistic locking for appointments
- Background task processing with Celery
- Optimized database queries with select_related/prefetch_related

## 🎨 Design System

The application follows a beautiful, modern design system specifically crafted for the beauty industry:

- **Color Palette**: Sophisticated beige, blush pink, and lavender tones
- **Typography**: Inter (primary) + Playfair Display (accent)
- **Components**: Accessible, responsive, and elegant UI components
- **Animations**: Smooth transitions with Framer Motion

## 📱 Key Features

### For Salon Owners
- Real-time business dashboard
- Staff performance analytics
- Revenue tracking and forecasting
- Multi-location management
- Automated reporting

### For Staff
- Personal schedule management
- Client history and preferences
- Commission tracking
- Mobile-friendly interface
- Notification management

### For Clients
- Online appointment booking
- Service history tracking
- Loyalty program integration
- Automated reminders
- Review and rating system

## 🔧 Development Workflow

### Task-Based Development
This project follows a structured task-based development approach:

1. **Task 1**: ✅ Project Foundation Setup (Current)
2. **Task 2**: Context Engineering Documentation
3. **Task 3**: Django Backend Foundation
4. **Task 4**: Client Management System
5. **Task 5**: Service and Staff Management
6. **Task 6**: Advanced Appointment System
7. **Task 7**: Multi-Channel Notification System
8. **Task 8**: Inventory Management
9. **Task 9**: React Frontend Foundation
10. **Task 10**: Appointment Booking Interface
11. **Task 11**: Client Management Interface
12. **Task 12**: Staff and Admin Dashboards
13. **Task 13**: Security and Performance Optimization
14. **Task 14**: Production Deployment Setup
15. **Task 15**: AI Integration Foundation

### Git Workflow
- **Commits**: Following pattern `feat: Task X - [Description]`
- **Branches**: Feature branches with mandatory code review
- **Quality Gates**: 95% test coverage, <200ms response times

## 🧪 Testing

### Backend Testing
```bash
cd backend
source venv/bin/activate
pytest
pytest --cov=apps --cov-report=html
```

### Frontend Testing
```bash
cd frontend
npm test
npm run test:coverage
```

## 📚 Documentation

- **API Documentation**: Auto-generated OpenAPI docs at `/api/docs/`
- **Architecture**: See `INITIAL.md` for technical specifications
- **Design System**: See `DESIGNSYSTEM.md` for UI/UX guidelines
- **Context Engineering**: See `context/` folder for business requirements

## 🚀 Deployment

### Development
Local development with SQLite and dummy cache for simplicity.

### Production
- **Backend**: Railway/Heroku with PostgreSQL and Redis
- **Frontend**: Vercel/Netlify with global CDN
- **Database**: Managed PostgreSQL with automated backups
- **Monitoring**: Sentry for error tracking, performance monitoring

## 📄 License

This project is proprietary software for Mario Beauty Salon.

## 🤝 Contributing

1. Follow the established code style (Black, ESLint, Prettier)
2. Write tests for new features
3. Update documentation as needed
4. Follow the task-based development workflow

---

## 📞 Support

For technical support or questions about the Mario Beauty Salon Management System, please contact the development team.

**Enterprise Development Standards**: This project follows enterprise-grade development practices with 99.9% uptime requirements, comprehensive security measures, and scalable architecture design.
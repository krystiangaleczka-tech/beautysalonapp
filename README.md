<<<<<<< HEAD
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

### PRP-Driven Development
This project follows the **Product Requirements Planning (PRP)** methodology:

- **All tasks are defined in**: `con_eng/PRPs/mario-beauty-salon-complete-system.md`
- **Micro-task approach**: Each major feature broken into atomic, verifiable steps
- **Sequential execution**: Tasks must be completed in PRP-defined order
- **Quality gates**: Each micro-task includes validation requirements

### Git Workflow
- **Commits**: Following pattern `feat: Task X.Y - [Description]` after each micro-task
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
=======
# 💄 MarioBeautyApp
### *Where Three Decades of Beauty Expertise Meets Modern Technology*

<div align="center">





*"Beauty is not just our business—it's our family legacy."* — The Flak Family

</div>

***

## 🌟 The Flak Family Legacy: A Story Worth Telling

### Chapter One: The Beginning (1992)
Picture this: Kraków, Poland, early 1990s. The Iron Curtain had just fallen, democracy was blooming, and **Mariusz Flak**, a passionate worker with golden hands, met **Ilona Flak**, a makeup artist whose artistry could make angels jealous. Together, they opened a tiny 30-square-meter salon with just two styling chairs, a dream, and an unshakeable belief that every person deserves to feel absolutely gorgeous.

### Chapter Two: The Growth (1992-2020)
Word spread like wildfire. Clients didn't just come for haircuts—they came for the *experience*. Mariusz's precision was legendary, and Ilona's makeup transformations were pure magic. But what truly set them apart was their obsession with **genuine client feedback**. They listened, adapted, and evolved. Soon, their little salon became the talk of the city.

### Chapter Three: The Next Generation (2020-Present)
Enter their daughter—a tech-savvy business graduate who inherited her parents' passion but saw inefficiencies everywhere. Paper appointment books getting lost, client preferences forgotten, inventory chaos, missed opportunities for client engagement. She had a vision: *"What if we could bottle our family's personal touch and scale it through technology?"*

**MarioBeautyApp** was born from this question.

***

## 🚀 What Makes MarioBeautyApp Extraordinary?

This isn't just another booking system. This is the **digital embodiment of the Flak family philosophy**—where cutting-edge technology serves one purpose: making every client feel like family.


***

## 📖 Epic User Stories That Drive Everything We Build

### 👩‍💼 **Sarah's Story** - The Busy Executive
*"As a working mom with back-to-back meetings, I need to book my monthly highlights during my 30-second elevator ride, receive a reminder that doesn't get lost in my email chaos, and know that my colorist Anna will have my exact shade ready when I arrive—because my lunch break is sacred, and my roots are not."*

**Our Solution**: One-tap rebooking, SMS reminders with calendar integration, and pre-visit preparation alerts to staff.

### 👨‍💼 **Mariusz's Story** - The Salon Owner
*"As someone who's been cutting hair since 1992, I don't want technology to complicate my life. I want it to help me remember that Mrs. Nowak likes her tea with one sugar, that Mr. Kowalski is allergic to sulfates, and that our teenager clients love our playlist from the 2000s. I want to focus on what I do best—making people beautiful."*

**Our Solution**: Intuitive interfaces that feel natural, client history at your fingertips, and background automation that handles the boring stuff.

### 💄 **Anna's Story** - The Senior Stylist
*"As a colorist with 15 years of experience, I want to walk into work knowing exactly what each client needs, have all their formulas ready, and spend my mental energy on perfecting their look—not scrambling to remember if they wanted warm or cool tones last time."*

**Our Solution**: Pre-visit client briefings, formula history, and mobile access to client notes.

***

## 🛠️ The Tech Stack: Why Every Choice Matters

We don't just pick technologies because they're popular. Every decision serves the **Flak Philosophy**: reliable, elegant, and always client-first.

| Technology | The "Why" Behind Our Choice |
|------------|----------------------------|
| **Django 5.2 LTS + Django-Ninja** 🐍 | Like a master beauty's toolkit—mature, reliable, with everything you need. The admin panel alone saves hundreds of hours of custom development. LTS ensures long-term stability. |
| **PostgreSQL 17** 🐘 | Client data is sacred. PostgreSQL's ACID compliance means never losing an appointment, never corrupting a client's color history. It's the Swiss bank account of databases. Latest version brings performance improvements and better JSON handling. |
| **React 19 + TypeScript 5.9** ⚛️ | Modern, component-based UI with type safety. Perfect for complex booking interfaces and real-time updates. TypeScript prevents bugs before they reach production. |
| **Redis 7** ⚡ | Speed matters. When a receptionist is searching for a client while they're standing there, microseconds count. Redis caches frequent queries and handles our task queue with lightning speed. |
| **Celery** 🌾 | The invisible worker bee. While stylists focus on their craft, Celery sends reminders, processes loyalty points, and generates reports—all in the background, never interrupting the flow. |
| **Docker** 🐳 | Consistency is key. What works on our developer's laptop works identically in production. No "but it worked on my machine" disasters. |
| **Gunicorn** 🦄 | The reliable workhorse that serves our app to the world, handling multiple clients simultaneously without breaking a sweat. |
| **Nginx** 🚀 | The bouncer and valet rolled into one—handles SSL certificates, serves images lightning-fast, and directs traffic with military precision. |
| **Tailwind CSS + Custom React Components** 🎨 | Beautiful, responsive design foundation enhanced with custom React components. Because if you're in the beauty business, your software better look gorgeous too. |

### 🗗️ Architecture Philosophy: "The Salon Metaphor"

Think of our architecture like a perfectly organized salon:

```yaml
version: '3.9'
services:
  # The Reception Desk - First impression matters
  nginx:
    image: nginx:stable-alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - static_volume:/app/static
      - ssl_certs:/etc/ssl/certs
    depends_on:
      - web

  # The Heart of Operations - Where the magic happens
  web:
    build: .
    command: gunicorn mariobeauty.wsgi:application --workers=4 --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - media_volume:/app/media
    depends_on:
      - db
      - cache
    environment:
      DJANGO_SETTINGS_MODULE: mariobeauty.settings.production
      DATABASE_URL: postgres://mario:${DB_PASSWORD}@db:5432/mariobeauty_db
      REDIS_URL: redis://cache:6379/0
      SECRET_KEY: ${SECRET_KEY}
      EMAIL_HOST: ${EMAIL_HOST}
      SMS_API_KEY: ${SMS_API_KEY}

  # The Memory Bank - Client histories, preferences, everything
  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: mario
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: mariobeauty_db
      POSTGRES_INITDB_ARGS: --encoding=UTF8 --lc-collate=C --lc-ctype=C
    volumes:
      - db_/var/lib/postgresql/data
      - ./backups:/backups
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U mario"]
      interval: 30s
      timeout: 10s
      retries: 3

  # The Quick Access Memory - Lightning-fast recalls
  cache:
    image: redis:7-alpine
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 10s
      retries: 3

  # The Behind-the-Scenes Assistant - Never sleeps, always working
  worker:
    build: .
    command: celery -A mariobeauty worker --loglevel=info --concurrency=2
    depends_on:
      - db
      - cache
    environment:
      DJANGO_SETTINGS_MODULE: mariobeauty.settings.production
      DATABASE_URL: postgres://mario:${DB_PASSWORD}@db:5432/mariobeauty_db
      REDIS_URL: redis://cache:6379/0
    
  # The Scheduler - Automated tasks running like clockwork
  scheduler:
    build: .
    command: celery -A mariobeauty beat --loglevel=info
    depends_on:
      - db
      - cache
    environment:
      DJANGO_SETTINGS_MODULE: mariobeauty.settings.production
      DATABASE_URL: postgres://mario:${DB_PASSWORD}@db:5432/mariobeauty_db
      REDIS_URL: redis://cache:6379/0

  # React Frontend Build & Development
  frontend:
    build: 
      context: ./frontend
      dockerfile: Dockerfile
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    ports:
      - "3000:3000"
    command: npm start

volumes:
  db_
  redis_
  static_volume:
  media_volume:
  ssl_certs:
```

***

## ⚡ Quick Start: From Zero to Beauty in 5 Minutes

```bash
# 1. Get the magic
git clone https://github.com/flak-family/MarioBeautyApp.git
cd MarioBeautyApp

# 2. Set your secrets (copy .env.example to .env and fill in your details)
cp .env.example .env
# Edit .env with your email, SMS, and other service credentials

# 3. Launch the beauty
docker-compose up --build -d

# 4. Create your salon empire
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata demo_data.json  # Optional: demo salon data

# 5. Open your salon to the world
# 🌐 Admin: https://localhost/admin
# 💄 Client Portal: https://localhost/
# 📱 API Docs: https://localhost/api/docs/
# ⚛️ React Frontend: https://localhost:3000
```

***

### 🎯 The "Flak Touch" Features v1 for future! (2027 NOT TO DO) ###

**💌 The Relationship Engine**
- Post-appointment thank-you messages with photo reminders of their fabulous new look
- Loyalty point gamification that feels personal, not corporate
- Referral tracking with rewards for both referrer and referred

**🏆 The Memory Palace**
- Every client interaction is remembered: their favorite coffee, preferred stylist, last color formula, even their dog's name
- AI-powered preference learning that gets better with every visit
- Birthday surprises, anniversary reminders, and "we miss you" gentle nudges

**⚡ The Magic Scheduler**
- Drag-and-drop booking that prevents double-bookings with the precision of a Swiss watch
- Smart suggestions: "Mrs. Kowalska usually books with Anna on Fridays at 2 PM—slot available!"
- Buffer time calculations (because rushing kills the experience)
- Weather-based service suggestions (rainy day = perfect for deep conditioning)

**📊 The Crystal Ball Dashboard**
- Predict busy periods before they happen
- Inventory alerts that know your rhythm: "You're low on blonde 40vol—reorder before the weekend rush?"
- Staff performance insights that celebrate success, not just track numbers


## 🌈 What's Coming Next: Our Roadmap

### 🚀 Version 2.0 - "The AI Stylist" (2027)
- **Smart Color Matching**: AI suggestions based on skin tone analysis
- **Virtual Try-On**: AR hair color and style preview
- **Predictive Scheduling**: ML-powered optimal appointment timing

### 🌟 Version 3.0 - "The Ecosystem" (2027)
- **Mobile App**: Native iOS/Android experience with React Native
- **Inventory Automation**: Auto-ordering from preferred suppliers
- **Multi-Location Management**: Franchise-ready features

### 💫 Version 4.0 - "The Future" (2027)
- **Voice Booking**: "Alexa, book my usual with Anna"
- **Blockchain Loyalty**: Cross-salon reward programs
- **Sustainability Tracking**: Carbon footprint reduction gamification

***

## 👨‍💻 Contributing: Join Our Family

We believe the best software is built by passionate people who care about the craft. Whether you're a seasoned developer or just starting out, we welcome you!

### 🎯 Contribution Guidelines
1. **Quality First**: Every PR needs tests with ≥85% coverage
2. **Beauty Matters**: Follow our style guide (PEP 8 + ESLint for TypeScript/React)
3. **Client-Centric**: Every feature should make someone's day better
4. **Family Values**: Respectful code reviews and helpful feedback

### 🏆 Hall of Fame
Special thanks to our amazing contributors who make MarioBeautyApp better every day!

***

## 📞 Support & Community

- 🐛 **Bug Reports**: [Issues](https://github.com/flak-family/MarioBeautyApp/issues)
- 💡 **Feature Requests**: [Discussions](https://github.com/flak-family/MarioBeautyApp/discussions)
- 📧 **Direct Contact**: hello@mariobeautyapp.com
- 💬 **Discord Community**: [Join us!](https://discord.gg/mariobeauty)

***

## 📜 License & Love

MarioBeautyApp is open-source software licensed under the **MIT License**. We believe great tools should be accessible to everyone.

***

<div align="center">

### *"From our family to yours—thank you for choosing MarioBeautyApp"*

**🌟 Made with MAZEN ❤️ for the Flak Family in Poland 🌟**

***

*Ready to transform your salon? [Get started today!](https://mariobeautyapp.com) 💄✨*

</div>
>>>>>>> 929117a2a2c6f2d0ffff7d4a41d856af7788d504

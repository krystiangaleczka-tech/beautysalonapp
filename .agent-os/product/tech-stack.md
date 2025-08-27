# Technical Stack

## Application Framework
- **application_framework**: Django 5.2 LTS
- **api_framework**: Django-Ninja 1.0+
- **version**: 5.2.0 (Enterprise Long Term Support)
- **architecture**: Microservices with API-first design
- **async_support**: ASGI for real-time features

## Database System
- **database_system**: PostgreSQL 17
- **features**: Advanced constraints, JSON fields, full-text search, ACID compliance
- **performance**: Connection pooling, query optimization, enterprise indexing
- **constraints**: Appointment conflict prevention, data integrity enforcement
- **backup**: Hourly incremental, daily full backups with <1 hour RPO

## JavaScript Framework
- **javascript_framework**: React 19
- **language**: TypeScript 5.9
- **build_tool**: Vite 5.0+
- **features**: Server Components, Concurrent Features, Suspense
- **state_management**: React Query 5.0+ + Context API
- **forms**: React Hook Form 7.48+ with Zod validation

## Import Strategy
- **import_strategy**: node
- **module_system**: ES6 imports with tree-shaking
- **bundling**: Vite with optimized chunking
- **code_splitting**: Route-based and component-based splitting

## CSS Framework
- **css_framework**: Tailwind CSS 3.4+
- **design_tokens**: Custom beauty salon theme (beige/pink/lavender palette)
- **responsive**: Mobile-first responsive design
- **animations**: Tailwind transitions + Framer Motion
- **custom_properties**: CSS variables for consistent theming

## UI Component Library
- **ui_component_library**: Custom design system built on Headless UI
- **accessibility**: WCAG 2.1 AA compliant components
- **composition**: Radix UI primitives for complex interactions
- **testing**: Storybook for component documentation

## Fonts Provider
- **fonts_provider**: Google Fonts
- **primary_font**: Inter (modern, professional, variable font)
- **secondary_font**: Playfair Display (elegant, beauty industry serif)
- **optimization**: Font display swap, preloading, variable fonts

## Icon Library
- **icon_library**: Lucide React (modern Heroicons successor)
- **custom_icons**: Beauty industry-specific SVG icons
- **format**: Optimized SVG with React components
- **accessibility**: Proper ARIA labels and descriptions

## Application Hosting
- **application_hosting**: Vercel (frontend) + Railway (backend)
- **deployment**: GitHub integration with automated CI/CD
- **environments**: Development, staging, production
- **scaling**: Automatic horizontal scaling
- **edge**: Global CDN with edge functions

## Database Hosting
- **database_hosting**: Railway PostgreSQL / Supabase
- **connection_pooling**: PgBouncer with max 100 connections per instance
- **performance**: Query optimization, proper indexing
- **monitoring**: Real-time performance metrics
- **compliance**: GDPR-ready data handling

## Asset Hosting
- **asset_hosting**: Vercel Edge Network
- **file_storage**: Vercel Blob for user uploads
- **image_optimization**: Next.js Image optimization
- **caching**: Aggressive caching with proper cache headers

## Deployment Solution
- **deployment_solution**: Vercel + Railway with Docker
- **ci_cd**: GitHub Actions for testing and deployment
- **infrastructure**: Infrastructure as Code with proper versioning
- **monitoring**: Comprehensive application and infrastructure monitoring
- **rollback**: Blue-green deployment with instant rollback

## Code Repository URL
- **code_repository_url**: https://github.com/username/beautysalonapp
- **branching_strategy**: Git Flow (main, develop, feature branches)
- **commit_convention**: feat: Task X - [Description] pattern
- **code_review**: Mandatory peer review for all changes

## Enterprise Dependencies

### Backend Core Dependencies
```python
# Production Dependencies (requirements/base.txt)
django==5.2                    # LTS framework
django-ninja>=1.0              # High-performance API framework
pydantic>=2.5                  # Type validation and serialization
celery[redis]>=5.3             # Distributed task processing
psycopg2-binary>=2.9           # PostgreSQL adapter
django-redis>=5.4              # Redis integration
django-cors-headers>=4.3       # CORS handling
djangorestframework-simplejwt>=5.3  # JWT authentication
pillow>=10.1                   # Image processing
python-decouple>=3.8           # Environment configuration
sentry-sdk[django]>=1.38       # Error monitoring
bleach>=6.1                    # Input sanitization
django-extensions>=3.2         # Development utilities
# DESIGNSYSTEM.md - Mario Beauty Salon Web Application

## Design Philosophy
**"Elegant Wellness Experience"** - A sleek, modern, and feminine design system that embodies the tranquility and sophistication of professional beauty services. The design creates a calming, trustworthy environment that makes clients feel pampered and confident in their booking decisions.

---

## 🎨 Color Palette

### Primary Colors
```css
/* Sophisticated Beige Tones */
--color-primary-50: #faf8f5;    /* Cream White - backgrounds */
--color-primary-100: #f5f1ea;   /* Light Beige - cards */
--color-primary-200: #ede6d9;   /* Soft Beige - borders */
--color-primary-300: #e0d4c0;   /* Medium Beige - hover states */
--color-primary-400: #d0bfa7;   /* Warm Beige - secondary elements */
--color-primary-500: #b8a082;   /* Main Beige - primary brand color */
--color-primary-600: #a08865;   /* Dark Beige - active states */
--color-primary-700: #8a7354;   /* Deep Beige - text on light */
--color-primary-800: #6d5b43;   /* Darker Beige - headings */
--color-primary-900: #4a3d2e;   /* Darkest Beige - emphasis */
```

### Secondary Colors - Blush Pink
```css
/* Feminine Pink Accents */
--color-secondary-50: #fdf2f4;   /* Light Blush - notification backgrounds */
--color-secondary-100: #fce3e8;  /* Soft Pink - success states */
--color-secondary-200: #f9c2ce;  /* Medium Pink - highlights */
--color-secondary-300: #f494a8;  /* Rose Pink - interactive elements */
--color-secondary-400: #ed6b85;  /* Vibrant Pink - call-to-action */
--color-secondary-500: #e13d5e;  /* Main Pink - accent color */
--color-secondary-600: #c2244a;  /* Deep Pink - active buttons */
--color-secondary-700: #a21b3c;  /* Dark Pink - pressed states */
--color-secondary-800: #7d1530;  /* Darker Pink - error states */
--color-secondary-900: #5a0f24;  /* Darkest Pink - critical alerts */
```

### Tertiary Colors - Lavender
```css
/* Calming Lavender Tones */
--color-tertiary-50: #f6f4ff;    /* Light Lavender - info backgrounds */
--color-tertiary-100: #ebe6ff;   /* Soft Lavender - calm sections */
--color-tertiary-200: #d4c7ff;   /* Medium Lavender - badges */
--color-tertiary-300: #b8a3ff;   /* Vibrant Lavender - links */
--color-tertiary-400: #9978ff;   /* Rich Lavender - focus states */
--color-tertiary-500: #7c4dff;   /* Main Lavender - accent color */
--color-tertiary-600: #6a38e6;   /* Deep Lavender - active links */
--color-tertiary-700: #5829cc;   /* Dark Lavender - visited links */
--color-tertiary-800: #461fb3;   /* Darker Lavender - special elements */
--color-tertiary-900: #341699;   /* Darkest Lavender - emphasis */
```

### Neutral Colors
```css
/* Professional Grays */
--color-neutral-50: #fafafa;     /* Pure White - page backgrounds */
--color-neutral-100: #f5f5f5;    /* Light Gray - card backgrounds */
--color-neutral-200: #e5e5e5;    /* Soft Gray - dividers */
--color-neutral-300: #d4d4d4;    /* Medium Gray - borders */
--color-neutral-400: #a3a3a3;    /* Gray - placeholders */
--color-neutral-500: #737373;    /* Dark Gray - body text */
--color-neutral-600: #525252;    /* Darker Gray - secondary text */
--color-neutral-700: #404040;    /* Deep Gray - headings */
--color-neutral-800: #262626;    /* Very Dark Gray - important text */
--color-neutral-900: #171717;    /* Black - highest contrast */
```

### Semantic Colors
```css
/* Status and Feedback Colors */
--color-success: #10b981;        /* Green - confirmations */
--color-warning: #f59e0b;        /* Amber - warnings */
--color-error: #ef4444;          /* Red - errors */
--color-info: #3b82f6;           /* Blue - information */
```

---

## 📝 Typography

### Font Family
```css
/* Primary Font Stack */
--font-family-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Secondary Font Stack (for elegance) */
--font-family-secondary: 'Playfair Display', Georgia, 'Times New Roman', serif;

/* Monospace (for code/technical content) */
--font-family-mono: 'JetBrains Mono', Consolas, Monaco, 'Courier New', monospace;
```

### Font Sizes & Line Heights
```css
/* Heading Sizes */
--text-xs: 0.75rem;      /* 12px - captions, metadata */
--text-sm: 0.875rem;     /* 14px - small text, labels */
--text-base: 1rem;       /* 16px - body text */
--text-lg: 1.125rem;     /* 18px - large body text */
--text-xl: 1.25rem;      /* 20px - small headings */
--text-2xl: 1.5rem;      /* 24px - section headings */
--text-3xl: 1.875rem;    /* 30px - page headings */
--text-4xl: 2.25rem;     /* 36px - hero headings */
--text-5xl: 3rem;        /* 48px - display headings */
--text-6xl: 3.75rem;     /* 60px - large displays */

/* Line Heights */
--leading-tight: 1.25;   /* Tight spacing for headings */
--leading-normal: 1.5;   /* Normal spacing for body text */
--leading-relaxed: 1.625; /* Relaxed spacing for large text */
--leading-loose: 2;      /* Loose spacing for special cases */
```

### Font Weights
```css
--font-weight-light: 300;
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
--font-weight-extrabold: 800;
```

---

## 📏 Spacing System

### Base Spacing Scale
```css
/* Consistent spacing using 4px base unit */
--space-px: 1px;
--space-0-5: 0.125rem;   /* 2px */
--space-1: 0.25rem;      /* 4px */
--space-1-5: 0.375rem;   /* 6px */
--space-2: 0.5rem;       /* 8px */
--space-2-5: 0.625rem;   /* 10px */
--space-3: 0.75rem;      /* 12px */
--space-3-5: 0.875rem;   /* 14px */
--space-4: 1rem;         /* 16px */
--space-5: 1.25rem;      /* 20px */
--space-6: 1.5rem;       /* 24px */
--space-7: 1.75rem;      /* 28px */
--space-8: 2rem;         /* 32px */
--space-10: 2.5rem;      /* 40px */
--space-12: 3rem;        /* 48px */
--space-16: 4rem;        /* 64px */
--space-20: 5rem;        /* 80px */
--space-24: 6rem;        /* 96px */
--space-32: 8rem;        /* 128px */
```

### Layout Spacing
```css
/* Container and section spacing */
--container-padding: var(--space-4);     /* Mobile: 16px */
--container-padding-lg: var(--space-8);  /* Desktop: 32px */
--section-spacing: var(--space-16);      /* Between sections: 64px */
--component-spacing: var(--space-6);     /* Between components: 24px */
```

---

## 🔘 Border Radius

### Rounded Corners (Modern & Feminine)
```css
/* Subtle to prominent rounded corners */
--radius-none: 0;
--radius-sm: 0.25rem;    /* 4px - small elements */
--radius-base: 0.5rem;   /* 8px - buttons, inputs */
--radius-md: 0.75rem;    /* 12px - cards, modals */
--radius-lg: 1rem;       /* 16px - large cards */
--radius-xl: 1.5rem;     /* 24px - hero sections */
--radius-2xl: 2rem;      /* 32px - special elements */
--radius-full: 9999px;   /* Perfect circles */
```

---

## 🎯 Component Design System

### 1. Buttons

#### Primary Button (Call-to-Action)
```css
.btn-primary {
  background: linear-gradient(135deg, var(--color-secondary-500), var(--color-secondary-400));
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-base);
  font-weight: var(--font-weight-semibold);
  border: none;
  box-shadow: 0 4px 12px rgba(225, 61, 94, 0.3);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: linear-gradient(135deg, var(--color-secondary-600), var(--color-secondary-500));
  box-shadow: 0 6px 16px rgba(225, 61, 94, 0.4);
  transform: translateY(-1px);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: var(--color-primary-100);
  color: var(--color-primary-800);
  border: 2px solid var(--color-primary-300);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-base);
  font-weight: var(--font-weight-medium);
}

.btn-secondary:hover {
  background: var(--color-primary-200);
  border-color: var(--color-primary-400);
}
```

#### Tertiary Button (Lavender Accent)
```css
.btn-tertiary {
  background: linear-gradient(135deg, var(--color-tertiary-500), var(--color-tertiary-400));
  color: white;
  padding: var(--space-2-5) var(--space-5);
  border-radius: var(--radius-base);
  font-weight: var(--font-weight-medium);
  border: none;
}
```

### 2. Input Fields

#### Text Input
```css
.input-field {
  background: var(--color-neutral-50);
  border: 2px solid var(--color-primary-200);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-base);
  color: var(--color-neutral-700);
  transition: all 0.2s ease;
}

.input-field:focus {
  outline: none;
  border-color: var(--color-secondary-400);
  box-shadow: 0 0 0 3px rgba(244, 148, 168, 0.1);
}

.input-field::placeholder {
  color: var(--color-neutral-400);
}
```

#### Select Dropdown
```css
.select-field {
  background: var(--color-neutral-50);
  border: 2px solid var(--color-primary-200);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  appearance: none;
  background-image: url("data:image/svg+xml...");
}
```

### 3. Cards & Containers

#### Service Card
```css
.service-card {
  background: linear-gradient(145deg, var(--color-neutral-50), var(--color-primary-50));
  border: 1px solid var(--color-primary-200);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: 0 4px 16px rgba(184, 160, 130, 0.1);
  transition: all 0.3s ease;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(184, 160, 130, 0.15);
  border-color: var(--color-secondary-300);
}
```

#### Appointment Card
```css
.appointment-card {
  background: white;
  border-left: 4px solid var(--color-tertiary-400);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  margin-bottom: var(--space-3);
}
```

### 4. Navigation & Layout

#### Header Navigation
```css
.header-nav {
  background: linear-gradient(135deg, var(--color-primary-50), white);
  border-bottom: 1px solid var(--color-primary-200);
  padding: var(--space-4) 0;
  backdrop-filter: blur(10px);
}

.nav-link {
  color: var(--color-primary-700);
  font-weight: var(--font-weight-medium);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-base);
  transition: all 0.2s ease;
}

.nav-link:hover {
  background: var(--color-secondary-100);
  color: var(--color-secondary-600);
}
```

#### Sidebar
```css
.sidebar {
  background: linear-gradient(180deg, var(--color-primary-50), var(--color-primary-100));
  border-right: 1px solid var(--color-primary-200);
  width: 280px;
  padding: var(--space-6);
}
```

### 5. Forms & Booking Interface

#### Booking Form Container
```css
.booking-form {
  background: white;
  border-radius: var(--radius-xl);
  padding: var(--space-8);
  box-shadow: 0 16px 64px rgba(184, 160, 130, 0.1);
  border: 1px solid var(--color-primary-200);
}

.form-section {
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-6);
  border-bottom: 1px solid var(--color-primary-200);
}

.form-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
}
```

#### Time Slot Selector
```css
.time-slot {
  background: var(--color-primary-100);
  border: 2px solid var(--color-primary-200);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.time-slot:hover {
  background: var(--color-secondary-100);
  border-color: var(--color-secondary-300);
}

.time-slot.selected {
  background: var(--color-secondary-500);
  border-color: var(--color-secondary-600);
  color: white;
}

.time-slot.unavailable {
  background: var(--color-neutral-200);
  color: var(--color-neutral-400);
  cursor: not-allowed;
}
```

### 6. Status & Feedback Elements

#### Status Badges
```css
.badge-confirmed {
  background: linear-gradient(135deg, var(--color-success), #059669);
  color: white;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
}

.badge-pending {
  background: linear-gradient(135deg, var(--color-warning), #d97706);
  color: white;
}

.badge-cancelled {
  background: linear-gradient(135deg, var(--color-error), #dc2626);
  color: white;
}
```

#### Progress Indicators
```css
.progress-bar {
  background: var(--color-primary-200);
  border-radius: var(--radius-full);
  height: 8px;
  overflow: hidden;
}

.progress-bar-fill {
  background: linear-gradient(90deg, var(--color-secondary-500), var(--color-tertiary-500));
  height: 100%;
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}
```

---

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile-first approach */
--breakpoint-sm: 640px;   /* Small tablets */
--breakpoint-md: 768px;   /* Tablets */
--breakpoint-lg: 1024px;  /* Small laptops */
--breakpoint-xl: 1280px;  /* Laptops */
--breakpoint-2xl: 1536px; /* Large screens */
```

### Container Sizes
```css
.container {
  width: 100%;
  margin: 0 auto;
  padding: 0 var(--space-4);
}

@media (min-width: 640px) {
  .container { max-width: 640px; }
}

@media (min-width: 768px) {
  .container { 
    max-width: 768px;
    padding: 0 var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container { 
    max-width: 1024px;
    padding: 0 var(--space-8);
  }
}

@media (min-width: 1280px) {
  .container { max-width: 1200px; }
}
```

---

## 🎭 Animation & Transitions

### Standard Transitions
```css
/* Smooth, professional animations */
--transition-fast: 0.15s ease;
--transition-base: 0.2s ease;
--transition-slow: 0.3s ease;
--transition-slower: 0.5s ease;

/* Easing functions */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
--ease-in-back: cubic-bezier(0.36, 0, 0.66, -0.56);
```

### Hover Effects
```css
.hover-lift {
  transition: transform var(--transition-base);
}

.hover-lift:hover {
  transform: translateY(-2px);
}

.hover-glow {
  transition: box-shadow var(--transition-base);
}

.hover-glow:hover {
  box-shadow: 0 8px 32px rgba(225, 61, 94, 0.2);
}
```

---

## 🖼️ Visual Elements

### Shadows & Depth
```css
/* Subtle, elegant shadows */
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-base: 0 4px 12px rgba(184, 160, 130, 0.1);
--shadow-md: 0 8px 24px rgba(184, 160, 130, 0.12);
--shadow-lg: 0 16px 48px rgba(184, 160, 130, 0.15);
--shadow-xl: 0 24px 64px rgba(184, 160, 130, 0.2);

/* Colored shadows for accents */
--shadow-pink: 0 8px 32px rgba(225, 61, 94, 0.2);
--shadow-lavender: 0 8px 32px rgba(124, 77, 255, 0.2);
```

### Gradients
```css
/* Background gradients */
--gradient-primary: linear-gradient(135deg, var(--color-primary-50), var(--color-primary-100));
--gradient-secondary: linear-gradient(135deg, var(--color-secondary-500), var(--color-secondary-400));
--gradient-tertiary: linear-gradient(135deg, var(--color-tertiary-500), var(--color-tertiary-400));
--gradient-neutral: linear-gradient(135deg, var(--color-neutral-50), white);

/* Overlay gradients */
--gradient-overlay: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.6));
```

---

## 🎨 Icon System

### Icon Specifications
- **Library**: Lucide React (consistent, professional icons)
- **Size Scale**: 16px, 20px, 24px, 32px, 48px
- **Style**: Outlined icons with 2px stroke width
- **Colors**: Match component context (primary, secondary, neutral)

### Common Icons Usage
```css
.icon-sm { width: 16px; height: 16px; } /* Small UI elements */
.icon-base { width: 20px; height: 20px; } /* Buttons, inputs */
.icon-md { width: 24px; height: 24px; } /* Navigation, cards */
.icon-lg { width: 32px; height: 32px; } /* Section headers */
.icon-xl { width: 48px; height: 48px; } /* Hero sections */
```

---

## 🔧 Implementation Guidelines

### 1. Component Priority Order
1. **Layout Components** (Header, Sidebar, Main Container)
2. **Form Components** (Inputs, Buttons, Selectors)
3. **Booking Components** (Calendar, Time Slots, Service Cards)
4. **Data Display** (Tables, Lists, Cards)
5. **Feedback Components** (Modals, Toasts, Loading states)

### 2. Accessibility Requirements
- **Minimum contrast ratio**: 4.5:1 for normal text, 3:1 for large text
- **Focus indicators**: Visible focus rings using secondary color
- **Touch targets**: Minimum 44px × 44px for interactive elements
- **Screen reader support**: Proper ARIA labels and semantic HTML

### 3. Performance Considerations
- **CSS Custom Properties**: Use for consistent theming
- **Component composition**: Build complex components from simpler ones
- **Lazy loading**: For images and non-critical components
- **Bundle optimization**: Tree-shake unused CSS

### 4. Brand Guidelines
- **Feminine & Professional**: Balance elegant aesthetics with business functionality
- **Trustworthy**: Use consistent spacing and typography for reliability
- **Calming**: Leverage beige and lavender for stress-free booking experience
- **Modern**: Utilize gradients, shadows, and rounded corners appropriately

---

## 🚀 Quick Implementation Checklist

### CSS Variables Setup
- [ ] Import design tokens as CSS custom properties
- [ ] Set up Tailwind CSS configuration with custom colors
- [ ] Configure font loading (Inter + Playfair Display)
- [ ] Implement responsive breakpoints

### Core Components
- [ ] Button variants (primary, secondary, tertiary)
- [ ] Input field styles (text, select, date, time)
- [ ] Card layouts (service cards, appointment cards)
- [ ] Navigation components (header, sidebar)
- [ ] Status indicators (badges, progress bars)

### Booking-Specific Elements
- [ ] Calendar component styling
- [ ] Time slot selector grid
- [ ] Service selection cards
- [ ] Staff member cards
- [ ] Confirmation flow design

### Testing & Validation
- [ ] Cross-browser compatibility
- [ ] Mobile responsiveness
- [ ] Accessibility compliance
- [ ] Performance optimization
- [ ] Design system consistency

---

*This design system serves as the foundation for Mario Beauty Salon's web application, ensuring a cohesive, professional, and feminine user experience that builds trust and encourages bookings.*
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        // Primary Colors (Sophisticated Beige Tones)
        primary: {
          50: '#faf8f5',   // Cream White - backgrounds
          100: '#f5f1ea',  // Light Beige - cards
          200: '#ede6d9',  // Soft Beige - borders
          300: '#e0d4c0',  // Medium Beige - hover states
          400: '#d0bfa7',  // Warm Beige - secondary elements
          500: '#b8a082',  // Main Beige - primary brand color
          600: '#a08865',  // Dark Beige - active states
          700: '#8a7354',  // Deep Beige - text on light
          800: '#6d5b43',  // Darker Beige - headings
          900: '#4a3d2e',  // Darkest Beige - emphasis
        },
        // Secondary Colors (Blush Pink)
        secondary: {
          50: '#fdf2f4',   // Light Blush - notification backgrounds
          100: '#fce3e8',  // Soft Pink - success states
          200: '#f9c2ce',  // Medium Pink - highlights
          300: '#f494a8',  // Rose Pink - interactive elements
          400: '#ed6b85',  // Vibrant Pink - call-to-action
          500: '#e13d5e',  // Main Pink - accent color
          600: '#c2244a',  // Deep Pink - active buttons
          700: '#a21b3c',  // Dark Pink - pressed states
          800: '#7d1530',  // Darker Pink - error states
          900: '#5a0f24',  // Darkest Pink - critical alerts
        },
        // Tertiary Colors (Lavender)
        tertiary: {
          50: '#f6f4ff',   // Light Lavender - info backgrounds
          100: '#ebe6ff',  // Soft Lavender - calm sections
          200: '#d4c7ff',  // Medium Lavender - badges
          300: '#b8a3ff',  // Vibrant Lavender - links
          400: '#9978ff',  // Rich Lavender - focus states
          500: '#7c4dff',  // Main Lavender - accent color
          600: '#6a38e6',  // Deep Lavender - active links
          700: '#5829cc',  // Dark Lavender - visited links
          800: '#461fb3',  // Darker Lavender - special elements
          900: '#341699',  // Darkest Lavender - emphasis
        },
        // Semantic Colors
        success: '#10b981',
        warning: '#f59e0b',
        error: '#ef4444',
        info: '#3b82f6',
      },
      fontFamily: {
        primary: ['Inter', 'system-ui', 'sans-serif'],
        secondary: ['Playfair Display', 'Georgia', 'serif'],
        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
      },
      fontSize: {
        'xs': '0.75rem',      // 12px - captions, metadata
        'sm': '0.875rem',     // 14px - small text, labels
        'base': '1rem',       // 16px - body text
        'lg': '1.125rem',     // 18px - large body text
        'xl': '1.25rem',      // 20px - small headings
        '2xl': '1.5rem',      // 24px - section headings
        '3xl': '1.875rem',    // 30px - page headings
        '4xl': '2.25rem',     // 36px - hero headings
        '5xl': '3rem',        // 48px - display headings
        '6xl': '3.75rem',     // 60px - large displays
      },
      spacing: {
        '0.5': '0.125rem',   // 2px
        '1.5': '0.375rem',   // 6px
        '2.5': '0.625rem',   // 10px
        '3.5': '0.875rem',   // 14px
        '4.5': '1.125rem',   // 18px
        '5.5': '1.375rem',   // 22px
        '6.5': '1.625rem',   // 26px
        '7.5': '1.875rem',   // 30px
        '8.5': '2.125rem',   // 34px
        '9.5': '2.375rem',   // 38px
        '18': '4.5rem',      // 72px
        '88': '22rem',       // 352px
        '104': '26rem',      // 416px
        '112': '28rem',      // 448px
        '128': '32rem',      // 512px
      },
      borderRadius: {
        'none': '0',
        'sm': '0.25rem',     // 4px - small elements
        'DEFAULT': '0.5rem', // 8px - buttons, inputs
        'md': '0.75rem',     // 12px - cards, modals
        'lg': '1rem',        // 16px - large cards
        'xl': '1.5rem',      // 24px - hero sections
        '2xl': '2rem',       // 32px - special elements
        'full': '9999px',    // Perfect circles
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'fade-out': 'fadeOut 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
        'scale-in': 'scaleIn 0.2s ease-out',
        'bounce-soft': 'bounceSoft 0.6s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeOut: {
          '0%': { opacity: '1' },
          '100%': { opacity: '0' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        bounceSoft: {
          '0%': { transform: 'scale(0.95)' },
          '50%': { transform: 'scale(1.02)' },
          '100%': { transform: 'scale(1)' },
        },
      },
      boxShadow: {
        'soft': '0 4px 16px rgba(184, 160, 130, 0.1)',
        'soft-hover': '0 8px 32px rgba(184, 160, 130, 0.15)',
        'pink': '0 4px 12px rgba(225, 61, 94, 0.3)',
        'pink-hover': '0 6px 16px rgba(225, 61, 94, 0.4)',
      },
      backdropBlur: {
        'xs': '2px',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}

export default config
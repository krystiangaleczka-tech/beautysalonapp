import React from 'react'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from '../src/App'

// Mock the auth hook
jest.mock('../src/hooks/useAuth', () => ({
  ...jest.requireActual('../src/hooks/useAuth'),
  useAuth: () => ({
    user: { id: '1', email: 'test@example.com', firstName: 'John', lastName: 'Doe' },
    login: jest.fn(),
    logout: jest.fn(),
    isLoading: false
  })
}))

const queryClient = new QueryClient()

const renderWithProviders = (component: React.ReactElement) => {
  return render(
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        {component}
      </BrowserRouter>
    </QueryClientProvider>
  )
}

describe('Frontend Foundation', () => {
  test('renders home page', () => {
    renderWithProviders(<App />)
    expect(screen.getByText('Mario Beauty Salon')).toBeInTheDocument()
    expect(screen.getByText('Enterprise Beauty Salon Management System')).toBeInTheDocument()
  })

  test('renders login page', () => {
    renderWithProviders(<App />)
    window.history.pushState({}, 'Login', '/login')
    expect(screen.getByText('Sign in to your account')).toBeInTheDocument()
  })

  test('renders protected routes when authenticated', () => {
    renderWithProviders(<App />)
    window.history.pushState({}, 'Dashboard', '/dashboard')
    expect(screen.getByText('Dashboard content goes here')).toBeInTheDocument()
  })
})
import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../../hooks/useAuth'
import Button from '../ui/Button'

const Header: React.FC = () => {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  return (
    <header className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Link to="/" className="text-xl font-bold text-primary-600">
                Mario Beauty Salon
              </Link>
            </div>
            <nav className="ml-6 flex space-x-8">
              <Link to="/dashboard" className="inline-flex items-center px-1 pt-1 border-b-2 border-primary-500 text-sm font-medium text-gray-900">
                Dashboard
              </Link>
              <Link to="/appointments" className="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
                Appointments
              </Link>
              <Link to="/clients" className="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
                Clients
              </Link>
              <Link to="/services" className="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
                Services
              </Link>
              <Link to="/staff" className="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
                Staff
              </Link>
            </nav>
          </div>
          <div className="flex items-center">
            {user ? (
              <div className="flex items-center">
                <span className="text-sm text-gray-700 mr-4">
                  Welcome, {user.firstName}
                </span>
                <Button variant="outline" size="sm" onClick={handleLogout}>
                  Logout
                </Button>
              </div>
            ) : (
              <Link to="/login">
                <Button variant="primary" size="sm">
                  Login
                </Button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
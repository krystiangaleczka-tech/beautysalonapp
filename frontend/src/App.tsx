import { Routes, Route, Navigate, Outlet } from 'react-router-dom'
import { useAuth } from './hooks/useAuth'
import Layout from './components/layout/Layout'
import './App.css'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={<ProtectedRoute><DashboardPage /></ProtectedRoute>} />
        <Route path="/appointments" element={<ProtectedRoute><AppointmentsPage /></ProtectedRoute>} />
        <Route path="/clients" element={<ProtectedRoute><ClientsPage /></ProtectedRoute>} />
        <Route path="/services" element={<ProtectedRoute><ServicesPage /></ProtectedRoute>} />
        <Route path="/staff" element={<ProtectedRoute><StaffPage /></ProtectedRoute>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  )
}

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { user, isLoading } = useAuth()
  
  if (isLoading) {
    return <div>Loading...</div>
  }
  
  if (!user) {
    return <Navigate to="/login" replace />
  }
  
  return (
    <Layout>
      {children}
    </Layout>
  )
}

function HomePage() {
  return (
    <div className="bg-gradient-to-r from-primary-100 to-secondary-100 min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-primary-800 mb-4">
          Mario Beauty Salon
        </h1>
        <p className="text-lg text-primary-600 mb-8">
          Enterprise Beauty Salon Management System
        </p>
        <div className="space-y-2">
          <p className="text-sm text-gray-600">✨ React 18 + TypeScript</p>
          <p className="text-sm text-gray-600">🎨 Tailwind CSS + Beauty Theme</p>
          <p className="text-sm text-gray-600">⚡ Vite Build System</p>
          <p className="text-sm text-gray-600">🏗️ Ready for Development</p>
        </div>
      </div>
    </div>
  )
}

function LoginPage() {
  const { login } = useAuth()
  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [error, setError] = React.useState('')
  const [isLoading, setIsLoading] = React.useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')
    
    try {
      await login(email, password)
    } catch (err) {
      setError('Invalid email or password')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-10 bg-white rounded-xl shadow-lg">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Sign in to your account
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {error && (
            <div className="rounded-md bg-red-50 p-4">
              <div className="text-sm text-red-700">
                {error}
              </div>
            </div>
          )}
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 focus:z-10 sm:text-sm"
                placeholder="Email address"
              />
            </div>
            <div>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 focus:z-10 sm:text-sm"
                placeholder="Password"
              />
            </div>
          </div>
          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
            >
              {isLoading ? 'Signing in...' : 'Sign in'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

function DashboardPage() {
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
        <p className="text-gray-500">Dashboard content goes here</p>
      </div>
    </div>
  )
}

function AppointmentsPage() {
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
        <p className="text-gray-500">Appointments content goes here</p>
      </div>
    </div>
  )
}

function ClientsPage() {
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
        <p className="text-gray-500">Clients content goes here</p>
      </div>
    </div>
  )
}

function ServicesPage() {
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
        <p className="text-gray-500">Services content goes here</p>
      </div>
    </div>
  )
}

function StaffPage() {
  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
        <p className="text-gray-500">Staff content goes here</p>
      </div>
    </div>
  )
}

export default App
import { useState, useEffect, createContext, useContext } from 'react'
import api from '../services/api'

interface User {
  id: string
  email: string
  firstName: string
  lastName: string
}

interface AuthContextType {
  user: User | null
  login: (email: string, password: string) => Promise<void>
  logout: () => void
  isLoading: boolean
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem('authToken')
    if (token) {
      // In a real app, you would validate the token and fetch user data
      // For now, we'll just set a mock user
      setUser({
        id: '1',
        email: 'user@example.com',
        firstName: 'John',
        lastName: 'Doe'
      })
    }
    setIsLoading(false)
  }, [])

  const login = async (email: string, password: string) => {
    setIsLoading(true)
    try {
      // In a real app, you would make an API call to authenticate
      // const response = await api.post('/auth/login', { email, password })
      // const { token, user } = response.data
      // localStorage.setItem('authToken', token)
      // setUser(user)
      
      // Mock implementation
      localStorage.setItem('authToken', 'mock-token')
      setUser({
        id: '1',
        email,
        firstName: 'John',
        lastName: 'Doe'
      })
    } catch (error) {
      throw new Error('Invalid credentials')
    } finally {
      setIsLoading(false)
    }
  }

  const logout = () => {
    localStorage.removeItem('authToken')
    setUser(null)
  }

  const value = {
    user,
    login,
    logout,
    isLoading
  }

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
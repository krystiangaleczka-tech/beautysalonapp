import apiClient from '../src/services/api'

describe('API Client Configuration', () => {
  test('should have correct base URL', () => {
    expect(apiClient.defaults.baseURL).toBe('http://localhost:8000/api')
  })

  test('should have timeout set', () => {
    expect(apiClient.defaults.timeout).toBe(10000)
  })

  test('should have correct headers', () => {
    expect(apiClient.defaults.headers['Content-Type']).toBe('application/json')
  })

  test('should have request interceptor', () => {
    expect(apiClient.interceptors.request.handlers.length).toBeGreaterThan(0)
  })

  test('should have response interceptor', () => {
    expect(apiClient.interceptors.response.handlers.length).toBeGreaterThan(0)
  })
})
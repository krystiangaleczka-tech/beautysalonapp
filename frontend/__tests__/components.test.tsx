import React from 'react'
import { render, screen } from '@testing-library/react'
import Button from '../src/components/ui/Button'
import Input from '../src/components/ui/Input'
import Card from '../src/components/ui/Card'
import Loading from '../src/components/ui/Loading'
import Error from '../src/components/ui/Error'

describe('UI Components', () => {
  test('renders Button component', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })

  test('renders Input component', () => {
    render(<Input label="Test Input" />)
    expect(screen.getByLabelText('Test Input')).toBeInTheDocument()
  })

  test('renders Card component', () => {
    render(<Card title="Test Card">Card content</Card>)
    expect(screen.getByText('Test Card')).toBeInTheDocument()
    expect(screen.getByText('Card content')).toBeInTheDocument()
  })

  test('renders Loading component', () => {
    render(<Loading message="Loading..." />)
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  test('renders Error component', () => {
    render(<Error message="Something went wrong" />)
    expect(screen.getByText('Something went wrong')).toBeInTheDocument()
  })
})
import React from 'react'
import Button from './Button'

interface ErrorProps {
  message?: string
  onRetry?: () => void
}

const Error: React.FC<ErrorProps> = ({
  message = 'Something went wrong. Please try again.',
  onRetry
}) => {
  return (
    <div className="flex flex-col items-center justify-center p-4 text-center">
      <div className="bg-red-100 rounded-full p-3 mb-4">
        <svg className="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>
      <h3 className="text-lg font-medium text-gray-900 mb-1">Error</h3>
      <p className="text-sm text-gray-500 mb-4">{message}</p>
      {onRetry && (
        <Button onClick={onRetry} variant="primary">
          Try Again
        </Button>
      )}
    </div>
  )
}

export default Error
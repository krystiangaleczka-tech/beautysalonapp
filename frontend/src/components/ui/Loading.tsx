import React from 'react'

interface LoadingProps {
  message?: string
  size?: 'sm' | 'md' | 'lg'
}

const Loading: React.FC<LoadingProps> = ({
  message = 'Loading...',
  size = 'md'
}) => {
  const sizeClasses = {
    sm: 'h-4 w-4',
    md: 'h-8 w-8',
    lg: 'h-12 w-12',
  }
  
  return (
    <div className="flex flex-col items-center justify-center p-4">
      <div className="flex items-center justify-center">
        <div className={`${sizeClasses[size]} animate-spin rounded-full border-4 border-primary-500 border-t-transparent`}></div>
      </div>
      {message && (
        <p className="mt-2 text-sm text-gray-600">{message}</p>
      )}
    </div>
  )
}

export default Loading
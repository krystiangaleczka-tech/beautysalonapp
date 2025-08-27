#!/bin/bash

# Mario Beauty Salon - Development Environment Setup Script
# This script sets up the local development environment

set -e

echo "🏪 Setting up Mario Beauty Salon Development Environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

# Create virtual environment for Django
echo "🐍 Setting up Python virtual environment..."
if [ ! -d "backend/venv" ]; then
    python3 -m venv backend/venv
fi

# Activate virtual environment
source backend/venv/bin/activate

# Install Django dependencies
echo "📦 Installing Django dependencies..."
pip install -r backend/requirements/development.txt

# Copy environment file if it doesn't exist
if [ ! -f "backend/.env" ]; then
    echo "📝 Creating backend environment file..."
    cp backend/.env.example backend/.env
fi

# Create logs directory
mkdir -p backend/logs

# Run Django migrations
echo "🗄️ Running Django migrations..."
cd backend
python manage.py migrate
cd ..

# Create Django superuser (optional)
echo "👤 Would you like to create a Django superuser? (y/n)"
read -r create_superuser
if [ "$create_superuser" = "y" ]; then
    cd backend
    python manage.py createsuperuser
    cd ..
fi

# Install Node.js dependencies
echo "⚛️ Installing React dependencies..."
cd frontend
npm install

# Copy frontend environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating frontend environment file..."
    cp .env.example .env
fi

cd ..

echo "✅ Development environment setup complete!"
echo ""
echo "🚀 To start the development servers:"
echo "   Backend:  cd backend && source venv/bin/activate && python manage.py runserver"
echo "   Frontend: cd frontend && npm run dev"
echo ""
echo "📖 API Documentation will be available at: http://localhost:8000/api/docs/"
echo "🎨 Frontend will be available at: http://localhost:3000"
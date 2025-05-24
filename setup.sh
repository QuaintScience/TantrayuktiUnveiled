#!/bin/bash

# Tantrayukti Game Setup Script
echo "🏛️ Setting up The Architect of Knowledge: Tantrayukti Unveiled"
echo "============================================================"

# Check Python version
python_version=$(python3 --version 2>&1)
echo "📋 Python version: $python_version"

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# Make run script executable
chmod +x run.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the game server, run:"
echo "   source venv/bin/activate  # (if using virtual environment)"
echo "   python run.py"
echo ""
echo "📱 Then open your browser to: http://localhost:5000"
echo ""
echo "🎮 Enjoy exploring the ancient wisdom of Tantrayukti!"

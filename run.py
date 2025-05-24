#!/usr/bin/env python3
"""
Tantrayukti Game Server Launcher
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_sqlalchemy
        print("✅ All requirements satisfied")
        return True
    except ImportError as e:
        print(f"❌ Missing requirement: {e}")
        print("Please install requirements with: pip install -r requirements.txt")
        return False

def main():
    print("🏛️ The Architect of Knowledge: Tantrayukti Unveiled")
    print("=" * 50)
    
    if not check_requirements():
        sys.exit(1)
    
    print("🚀 Starting the Tantrayukti Game Server...")
    print("📱 Open your browser to: http://localhost:5001")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Import and run the app
        from app import app, init_db
        
        # Initialize database
        with app.app_context():
            init_db()
        
        # Run the server
        app.run(debug=True, host='0.0.0.0', port=5001)
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

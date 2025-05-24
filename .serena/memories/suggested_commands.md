# Suggested Commands

## Development Commands
```bash
# Start the Flask development server
python app.py

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Initialize database (run once)
python -c "from app import init_db; init_db()"
```

## System Commands (Darwin/macOS)
```bash
# List files
ls -la

# Change directory
cd path/to/directory

# Find files
find . -name "*.py"

# Search in files
grep -r "search_term" .

# Git operations
git status
git add .
git commit -m "message"
git push
```

## Project Specific
```bash
# Run the web server
python app.py

# Access the game
open http://localhost:5000
```
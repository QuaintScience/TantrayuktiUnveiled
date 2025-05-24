# Installation and Testing Instructions

## Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server:**
   ```bash
   python app.py
   ```
   
   Or use the launcher script:
   ```bash
   python run.py
   ```

3. **Open Browser:**
   Navigate to: http://localhost:5000

## Alternative Setup (with virtual environment)

1. **Setup (run once):**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Run the game:**
   ```bash
   source venv/bin/activate
   python run.py
   ```

## Testing Checklist

### ✅ User Registration
- [ ] Enter a new username → should create new account
- [ ] Enter existing username → should log in existing user
- [ ] Empty username → should show error

### ✅ Game Flow
- [ ] Start new game → should load first question
- [ ] Select tantrayukti tools → should enable submit button
- [ ] Submit answer → should show feedback
- [ ] Navigate through all questions
- [ ] Complete game → should show final statistics

### ✅ UI/UX
- [ ] Ancient aesthetic loads correctly
- [ ] Responsive design works on mobile
- [ ] Sound effects play (may need user interaction first)
- [ ] All animations work smoothly
- [ ] Sanskrit text displays correctly

### ✅ Data Persistence
- [ ] User stats persist across sessions
- [ ] Game progress is tracked
- [ ] Best scores are recorded

## Expected Behavior

1. **Landing Page:** Ancient scroll aesthetic with registration
2. **Game Interface:** Question cards with tantrayukti options
3. **Feedback:** Detailed explanations after each answer
4. **Statistics:** User progress tracking and ranking system

## Troubleshooting

- **Module not found:** Run `pip install -r requirements.txt`
- **Database issues:** Delete `tantrayukti_game.db` to reset
- **Port in use:** Change port in `app.py` line 311
- **Sound not working:** Ensure CDN access and user interaction

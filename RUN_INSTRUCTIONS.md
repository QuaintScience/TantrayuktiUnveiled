# 🏛️ The Architect of Knowledge: Tantrayukti Unveiled
## Complete Setup and Run Instructions

### 🚀 **QUICK START (3 steps):**

1. **Install Python dependencies:**
   ```bash
   pip install flask flask-sqlalchemy
   ```

2. **Run the server:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   ```
   http://localhost:5000
   ```

---

## 🎮 **How to Play:**

1. **Register:** Enter any name (new users created automatically, returning users recognized)
2. **Start Game:** Click "Start New Game" button
3. **Analyze Text:** Read the ancient Indian text fragment carefully
4. **Choose Tools:** Select appropriate Tantrayukti analytical tools
5. **Submit:** Get immediate feedback with detailed explanations
6. **Progress:** Complete all questions to see your final score

---

## 🛠️ **Alternative Setup Methods:**

### **Method 1: Using requirements.txt**
```bash
pip install -r requirements.txt
python app.py
```

### **Method 2: With virtual environment (recommended)**
```bash
# Run the setup script (Unix/Mac)
chmod +x setup.sh
./setup.sh

# Then run
source venv/bin/activate
python run.py
```

### **Method 3: Manual virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## ✨ **Game Features:**

- **🎨 Ancient Aesthetic:** Manuscript-inspired design with Sanskrit elements
- **🔊 Sound Effects:** Subtle audio feedback using Web Audio API
- **📱 Responsive:** Works on desktop, tablet, and mobile
- **📊 Progress Tracking:** User statistics and game history
- **🎯 Educational:** Learn 14 different Tantrayukti analytical tools
- **📚 Rich Content:** 15 text fragments from various Indian classical disciplines

---

## 🎓 **Educational Content:**

### **Disciplines Covered:**
- **Legal/Governance** (Arthaśāstra tradition)
- **Medical/Diagnostic** (Caraka & Suśruta Saṃhitā)
- **Philosophy/Logic** (Nyāya, Vaiśeṣika, Yoga Darśana)
- **Grammar/Linguistics** (Vyākaraṇa tradition)
- **Ritual/Religious** (Kalpa Sūtra tradition)
- **Astronomy/Astrology** (Jyotiśa tradition)

### **Tantrayukti Tools:**
1. **Prayojana** (प्रयोजन) - Purpose/Objective
2. **Adhikaraṇa** (अधिकरण) - Central Topic
3. **Uddeśa** (उद्देश) - Overview/Listing
4. **Nirdeśa** (निर्देश) - Detailed Explanation
5. **Ūhya** (ऊह्य) - Contextual Inference
6. **Dr̥ṣṭānta** (दृष्टान्त) - Illustrative Analogy
7. **Pūrvapakṣa** (पूर्वपक्ष) - Preliminary Objection
8. **Uttarapakṣa** (उत्तरपक्ष) - Conclusive Resolution
9. **Apavarga** (अपवर्ग) - Exception
10. **Vidhāna** (विधान) - Thematic Arrangement
11. **Viparyaya** (विपर्यय) - Warning Against Error
12. **Svasaṁjñā** (स्वसंज्ञा) - Technical Definition
13. **Atideśa** (अतिदेश) - Extension of Principles
14. **Arthāpatti** (अर्थापत्ति) - Logical Implication

---

## 🔍 **Troubleshooting:**

### **Common Issues:**

❌ **"Module not found" error:**
```bash
pip install flask flask-sqlalchemy
```

❌ **"Port already in use":**
- Edit `app.py` line 311: change `port=5000` to `port=5001`

❌ **JavaScript errors:**
- Clear browser cache (Ctrl+F5)
- Try incognito/private mode
- Disable browser extensions

❌ **Sounds not working:**
- Normal behavior - sounds play after first click
- Requires user interaction to enable audio

❌ **Database errors:**
```bash
rm tantrayukti_game.db  # Delete and restart
python app.py
```

### **Testing Checklist:**
- [ ] Server starts without errors
- [ ] Home page loads with ancient aesthetic
- [ ] Can register/login with any name
- [ ] "Start New Game" button works
- [ ] Questions load and display properly
- [ ] Can select Tantrayukti tools
- [ ] Submit button enables when tools selected
- [ ] Feedback appears after submission
- [ ] Can complete full game

---

## 📋 **System Requirements:**

- **Python 3.7+**
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Internet connection** (for fonts and Bootstrap CSS)
- **~50MB disk space**

---

## 🎉 **Enjoy the Game!**

Experience the sophisticated analytical framework of ancient Indian scholarship through this interactive educational game. Learn how classical scholars used different tools for different types of texts - legal, medical, philosophical, and more!

**🌟 The game demonstrates that Tantrayukti were not rigid protocols, but adaptive instruments responsive to the content and goals of each discipline.**

---

*For detailed technical information, see `README.md` and `TESTING.md`*

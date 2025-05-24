"""
The Architect of Knowledge: Tantrayukti Unveiled
Flask web server for the educational game
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
import os
import json
import random
from werkzeug.security import generate_password_hash, check_password_hash

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tantrayukti_game.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'tantrayukti_ancient_wisdom_key_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tantrayukti_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import game data after db is initialized
from game_data import TANTRAYUKTI_DEVICES, TEXTUAL_FRAGMENTS

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    total_score = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    best_score = db.Column(db.Integer, default=0)

class GameSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, default=0)
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('game_session.id'), nullable=False)
    fragment_id = db.Column(db.String(50), nullable=False)
    chosen_yukti = db.Column(db.Text, nullable=False)  # JSON string
    correct_yukti = db.Column(db.Text, nullable=False)  # JSON string
    is_correct = db.Column(db.Boolean, default=False)
    points_earned = db.Column(db.Integer, default=0)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_db():
    """Initialize the database with tables"""
    logger.info("🏛️ Initializing database tables...")
    with app.app_context():
        db.create_all()
        logger.info("✅ Database tables created successfully")

@app.route('/')
def index():
    """Main landing page"""
    logger.info("🏠 User accessed main page")
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('index.html', user=user)
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """Register a new user or login existing user"""
    username = request.json.get('username', '').strip()
    
    if not username:
        logger.warning("⚠️ Registration attempt with empty username")
        return jsonify({'error': 'Username is required'}), 400
    
    # Check if user exists
    user = User.query.filter_by(username=username).first()
    
    if user:
        # Existing user - log them in
        session['user_id'] = user.id
        session['username'] = user.username
        logger.info(f"🔄 User {username} logged in (returning user)")
        return jsonify({
            'success': True,
            'message': f'Welcome back, {username}!',
            'user': {
                'username': user.username,
                'total_score': user.total_score,
                'games_played': user.games_played,
                'best_score': user.best_score
            }
        })
    else:
        # New user - create account
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        logger.info(f"🆕 New user {username} registered successfully")
        return jsonify({
            'success': True,
            'message': f'Welcome to the ancient wisdom, {username}!',
            'user': {
                'username': new_user.username,
                'total_score': 0,
                'games_played': 0,
                'best_score': 0
            }
        })

@app.route('/game')
def game():
    """Game page"""
    if 'user_id' not in session:
        logger.warning("⚠️ Unauthorized access to game page")
        return redirect(url_for('index'))
    
    user = User.query.get(session['user_id'])
    logger.info(f"🎮 User {user.username} accessed game page")
    return render_template('game.html', user=user)

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game session"""
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_id = session['user_id']
    
    # Create new game session
    game_session = GameSession(user_id=user_id)
    db.session.add(game_session)
    db.session.commit()
    
    session['game_session_id'] = game_session.id
    
    # Select random fragments for this game
    fragments = random.sample(TEXTUAL_FRAGMENTS, min(8, len(TEXTUAL_FRAGMENTS)))
    session['game_fragments'] = [f['id'] for f in fragments]
    session['current_question'] = 0
    
    logger.info(f"🎯 User {session['username']} started new game session {game_session.id}")
    
    return jsonify({
        'success': True,
        'session_id': game_session.id,
        'total_questions': len(fragments)
    })

@app.route('/get_question')
def get_question():
    """Get the current question"""
    if 'user_id' not in session or 'game_session_id' not in session:
        return jsonify({'error': 'No active game session'}), 400
    
    current_q = session.get('current_question', 0)
    fragments = session.get('game_fragments', [])
    
    if current_q >= len(fragments):
        return jsonify({'game_complete': True})
    
    fragment_id = fragments[current_q]
    fragment = next(f for f in TEXTUAL_FRAGMENTS if f['id'] == fragment_id)
    
    logger.info(f"❓ Serving question {current_q + 1}/{len(fragments)} to {session['username']}")
    
    return jsonify({
        'question_number': current_q + 1,
        'total_questions': len(fragments),
        'fragment': fragment,
        'tantrayukti_devices': TANTRAYUKTI_DEVICES
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    """Submit an answer for evaluation"""
    if 'user_id' not in session or 'game_session_id' not in session:
        return jsonify({'error': 'No active game session'}), 400
    
    data = request.json
    session_id = data.get('session_id')
    fragment_id = data.get('fragment_id')
    chosen_yukti = data.get('chosen_yukti', [])
    
    if session_id != session['game_session_id']:
        return jsonify({'error': 'Invalid session'}), 400
    
    # Find the fragment
    fragment = next((f for f in TEXTUAL_FRAGMENTS if f['id'] == fragment_id), None)
    if not fragment:
        return jsonify({'error': 'Fragment not found'}), 400
    
    # Evaluate the answer
    correct_yukti = fragment['correct_yukti']
    correct_matches = [y for y in chosen_yukti if y in correct_yukti]
    incorrect_matches = [y for y in chosen_yukti if y not in correct_yukti]
    missing_correct = [y for y in correct_yukti if y not in chosen_yukti]
    
    # Calculate points
    points_earned = 0
    if len(correct_matches) == len(correct_yukti) and len(incorrect_matches) == 0:
        # Perfect match
        points_earned = 3
    elif len(correct_matches) > 0 and len(incorrect_matches) == 0:
        # Partially correct (missing some correct answers)
        points_earned = 2
    elif len(correct_matches) > 0:
        # Some correct, some incorrect
        points_earned = 1
    else:
        # All incorrect
        points_earned = -1
    
    # Update game session
    game_session = GameSession.query.get(session_id)
    if game_session:
        game_session.score += points_earned
        game_session.total_questions += 1
        if points_earned > 0:
            game_session.correct_answers += 1
    
    # Record the answer
    answer = Answer(
        session_id=session_id,
        fragment_id=fragment_id,
        chosen_yukti=json.dumps(chosen_yukti),
        correct_yukti=json.dumps(correct_yukti),
        is_correct=(points_earned > 0),
        points_earned=points_earned
    )
    db.session.add(answer)
    db.session.commit()
    
    # Move to next question
    session['current_question'] = session.get('current_question', 0) + 1
    
    logger.info(f"📝 {session['username']} answered Q{session['current_question']}: {points_earned} points")
    
    return jsonify({
        'success': True,
        'points_earned': points_earned,
        'new_score': game_session.score if game_session else points_earned,
        'correct_yukti': correct_yukti,
        'explanation': fragment['explanation'],
        'correct_matches': correct_matches,
        'incorrect_matches': incorrect_matches,
        'missing_correct': missing_correct
    })

@app.route('/complete_game', methods=['POST'])
def complete_game():
    """Complete the current game session"""
    if 'user_id' not in session or 'game_session_id' not in session:
        return jsonify({'error': 'No active game session'}), 400
    
    session_id = session['game_session_id']
    user_id = session['user_id']
    
    # Update game session
    game_session = GameSession.query.get(session_id)
    if game_session:
        game_session.completed_at = datetime.utcnow()
        
        # Update user stats
        user = User.query.get(user_id)
        if user:
            user.games_played += 1
            user.total_score += game_session.score
            if game_session.score > user.best_score:
                user.best_score = game_session.score
        
        db.session.commit()
        
        # Calculate statistics
        accuracy = 0
        if game_session.total_questions > 0:
            accuracy = round((game_session.correct_answers / game_session.total_questions) * 100)
        
        # Determine rank
        rank = 'Beginning Scholar'
        if accuracy >= 90:
            rank = 'Scholar Sage'
        elif accuracy >= 80:
            rank = 'Learned Scholar'
        elif accuracy >= 70:
            rank = 'Promising Student'
        elif accuracy >= 60:
            rank = 'Dedicated Learner'
        
        logger.info(f"🏁 {session['username']} completed game: {game_session.score} points, {accuracy}% accuracy")
        
        # Clear session game data
        session.pop('game_session_id', None)
        session.pop('game_fragments', None)
        session.pop('current_question', None)
        
        return jsonify({
            'success': True,
            'final_score': game_session.score,
            'correct_answers': game_session.correct_answers,
            'total_questions': game_session.total_questions,
            'accuracy': accuracy,
            'rank': rank,
            'games_played': user.games_played if user else 1
        })
    
    return jsonify({'error': 'Game session not found'}), 400

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user"""
    username = session.get('username', 'Unknown')
    session.clear()
    logger.info(f"👋 User {username} logged out")
    return jsonify({'success': True})


if __name__ == '__main__':
    init_db()
    logger.info("🚀 Starting Tantrayukti Game Server...")
    app.run(debug=True, host='0.0.0.0', port=5000)

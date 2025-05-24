/**
/**
 * Tantrayukti Game JavaScript
 * Handles game logic, UI interactions, and API communication
 * 
 * Copyright (C) 2024 Gokul Chittaranjan (gokul@quaintscience.com)
 * QuaintScience Technologies Pvt. Ltd.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

class TantrayuktiGame {
    constructor() {
        this.currentQuestion = 0;
        this.totalQuestions = 0;
        this.score = 0;
        this.gameSessionId = null;
        this.selectedYukti = [];
        this.currentFragment = null;
        this.gameStarted = false;
        
        // Game state
        this.questions = [];
        this.answers = [];
        
        // Initialize when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.init());
        } else {
            this.init();
        }
    }

    init() {
        console.log('🎮 Initializing Tantrayukti Game');
        this.setupEventListeners();
        this.resetGameState();
    }

    setupEventListeners() {
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.ctrlKey && !e.altKey) {
                if (this.gameStarted && document.getElementById('submitButton') && !document.getElementById('submitButton').disabled) {
                    this.submitAnswer();
                    e.preventDefault();
                }
            }
        });
    }

    resetGameState() {
        this.currentQuestion = 0;
        this.totalQuestions = 0;
        this.score = 0;
        this.gameSessionId = null;
        this.selectedYukti = [];
        this.currentFragment = null;
        this.gameStarted = false;
        this.questions = [];
        this.answers = [];
        
        // Reset UI
        this.updateScore(0);
        this.updateProgress(0, 0);
        this.showSection('startGameSection');
    }

    async startNewGame() {
        console.log('🚀 Starting new game...');
        
        try {
            playSound('gameStart');
            this.showLoadingState('Starting your scholarly journey...');
            
            const response = await fetch('/start_game', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const data = await response.json();
            
            if (data.success) {
                this.gameSessionId = data.session_id;
                this.totalQuestions = data.total_questions;
                this.gameStarted = true;
                
                console.log(`✅ Game started - Session: ${this.gameSessionId}, Questions: ${this.totalQuestions}`);
                
                // Load first question
                await this.loadQuestion();
            } else {
                throw new Error(data.error || 'Failed to start game');
            }
        } catch (error) {
            console.error('❌ Error starting game:', error);
            this.showError('Failed to start game. Please try again.');
        }
    }

    async loadQuestion() {
        try {
            console.log(`📖 Loading question ${this.currentQuestion + 1}...`);
            
            const response = await fetch('/get_question');
            const data = await response.json();
            
            if (data.game_complete) {
                await this.completeGame();
                return;
            }
            
            if (data.fragment && data.tantrayukti_devices) {
                this.currentFragment = data.fragment;
                this.currentQuestion = data.question_number - 1; // Convert to 0-based
                
                this.displayQuestion(data.fragment, data.tantrayukti_devices);
                this.updateProgress(data.question_number, data.total_questions);
                
                console.log(`✅ Question loaded: ${data.fragment.discipline} - ${data.fragment.difficulty}`);
            } else {
                throw new Error('Invalid question data received');
            }
        } catch (error) {
            console.error('❌ Error loading question:', error);
            this.showError('Failed to load question. Please try again.');
        }
    }

    displayQuestion(fragment, tantrayuktiDevices) {
        // Display fragment text
        document.getElementById('fragmentText').innerHTML = `"${fragment.text}"`;
        
        // Display meta information
        document.getElementById('fragmentDiscipline').textContent = fragment.discipline;
        document.getElementById('fragmentSource').textContent = fragment.source;
        
        const difficultyBadge = document.getElementById('fragmentDifficulty');
        difficultyBadge.textContent = fragment.difficulty;
        difficultyBadge.className = `badge bg-${this.getDifficultyColor(fragment.difficulty)}`;
        
        // Display Tantrayukti options
        this.displayTantrayuktiOptions(tantrayuktiDevices);
        
        // Reset selection state
        this.selectedYukti = [];
        this.updateSubmitButton();
        
        // Show question section
        this.showSection('questionSection');
        
        // Add fade-in animation
        setTimeout(() => {
            document.getElementById('questionSection').classList.add('fade-in');
        }, 100);
    }

    displayTantrayuktiOptions(devices) {
        const container = document.getElementById('tantrayuktiOptions');
        container.innerHTML = '';
        
        Object.entries(devices).forEach(([key, device]) => {
            const optionHtml = `
                <div class="col-md-6 mb-3">
                    <div class="tantrayukti-option" data-yukti="${key}" onclick="game.toggleYukti('${key}')">
                        <div class="card-body">
                            <div class="tantrayukti-name">
                                ${device.name}
                                <span class="tantrayukti-sanskrit">${device.sanskrit}</span>
                            </div>
                            <div class="tantrayukti-description">
                                ${device.description}
                            </div>
                            <div class="tantrayukti-category">
                                ${device.category}
                            </div>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += optionHtml;
        });
    }

    toggleYukti(yuktiKey) {
        playSound('buttonClick');
        
        const option = document.querySelector(`[data-yukti="${yuktiKey}"]`);
        const container = document.getElementById('tantrayuktiOptions');
        const index = this.selectedYukti.indexOf(yuktiKey);
        
        if (index > -1) {
            // Deselect
            this.selectedYukti.splice(index, 1);
            option.classList.remove('selected');
        } else {
            // Select
            this.selectedYukti.push(yuktiKey);
            option.classList.add('selected');
        }
        
        // Add/remove container class for visual feedback
        if (this.selectedYukti.length > 0) {
            container.classList.add('has-selection');
        } else {
            container.classList.remove('has-selection');
        }
        
        this.updateSubmitButton();
        console.log('📝 Selected Yukti:', this.selectedYukti);
    }

    updateSubmitButton() {
        const submitButton = document.getElementById('submitButton');
        const hasSelection = this.selectedYukti.length > 0;
        
        submitButton.disabled = !hasSelection;
        submitButton.innerHTML = hasSelection 
            ? '<i class="fas fa-check me-2"></i>Submit Answer'
            : '<i class="fas fa-check me-2"></i>Select at least one tool';
    }

    async submitAnswer() {
        if (this.selectedYukti.length === 0) return;
        
        try {
            console.log('📤 Submitting answer:', this.selectedYukti);
            playSound('buttonClick');
            
            // Disable submit button
            const submitButton = document.getElementById('submitButton');
            const originalText = submitButton.innerHTML;
            submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Evaluating...';
            submitButton.disabled = true;
            
            const response = await fetch('/submit_answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: this.gameSessionId,
                    fragment_id: this.currentFragment.id,
                    chosen_yukti: this.selectedYukti
                })
            });

            const result = await response.json();
            
            if (result.success) {
                this.score = result.new_score;
                this.updateScore(this.score);
                
                // Store answer for review
                this.answers.push({
                    fragment: this.currentFragment,
                    chosen: this.selectedYukti,
                    correct: result.correct_yukti,
                    points: result.points_earned,
                    feedback: result.feedback
                });
                
                this.showFeedback(result);
                console.log(`✅ Answer submitted - Points: ${result.points_earned}, New Score: ${result.new_score}`);
            } else {
                throw new Error(result.error || 'Failed to submit answer');
            }
        } catch (error) {
            console.error('❌ Error submitting answer:', error);
            this.showError('Failed to submit answer. Please try again.');
            
            // Restore submit button
            const submitButton = document.getElementById('submitButton');
            submitButton.innerHTML = originalText;
            submitButton.disabled = false;
        }
    }

    showFeedback(result) {
        const feedbackSection = document.getElementById('feedbackSection');
        const feedbackIcon = document.getElementById('feedbackIcon');
        const feedbackTitle = document.getElementById('feedbackTitle');
        const feedbackContent = document.getElementById('feedbackContent');
        
        // Determine feedback type
        let feedbackType, iconClass, titleText;
        
        if (result.points_earned >= 3) {
            feedbackType = 'correct';
            iconClass = 'fas fa-trophy';
            titleText = 'Excellent! Perfect Understanding';
            playSound('correct');
        } else if (result.points_earned >= 1) {
            feedbackType = 'partial';
            iconClass = 'fas fa-star-half-alt';
            titleText = 'Good! Partially Correct';
            playSound('correct');
        } else {
            feedbackType = 'incorrect';
            iconClass = 'fas fa-times-circle';
            titleText = 'Learning Opportunity';
            playSound('incorrect');
        }
        
        // Update feedback UI
        feedbackSection.className = `feedback-section feedback-${feedbackType}`;
        feedbackIcon.className = iconClass + ' me-2';
        feedbackTitle.textContent = titleText;
        
        // Build feedback content
        let feedbackHtml = `
            <div class="row mb-3">
                <div class="col-md-6">
                    <h6><i class="fas fa-user-check me-2"></i>Your Selection:</h6>
                    <ul class="list-unstyled">`;
        
        this.selectedYukti.forEach(yukti => {
            feedbackHtml += `<li class="mb-1"><i class="fas fa-dot-circle me-2 text-primary"></i>${yukti}</li>`;
        });
        
        feedbackHtml += `
                    </ul>
                </div>
                <div class="col-md-6">
                    <h6><i class="fas fa-bullseye me-2"></i>Correct Answer:</h6>
                    <ul class="list-unstyled">`;
        
        result.correct_yukti.forEach(yukti => {
            feedbackHtml += `<li class="mb-1"><i class="fas fa-check-circle me-2 text-success"></i>${yukti}</li>`;
        });
        
        feedbackHtml += `
                    </ul>
                </div>
            </div>
            <div class="feedback-explanation">
                <h6><i class="fas fa-lightbulb me-2"></i>Explanation:</h6>
                <p>${result.explanation}</p>
                <p><strong>Purpose:</strong> ${this.currentFragment.purpose}</p>
            </div>
            <div class="points-earned text-center mt-3">
                <span class="badge bg-primary fs-6">Points Earned: ${result.points_earned}</span>
            </div>
        `;
        
        feedbackContent.innerHTML = feedbackHtml;
        
        // Show feedback section
        this.showSection('feedbackSection');
        feedbackSection.classList.add('slide-up');
    }

    async nextQuestion() {
        console.log('➡️ Moving to next question...');
        
        // Clear feedback animations
        document.getElementById('feedbackSection').classList.remove('slide-up');
        
        // Load next question
        this.currentQuestion++;
        await this.loadQuestion();
    }

    async skipQuestion() {
        if (confirm('Are you sure you want to skip this question? You will not earn any points.')) {
            console.log('⏭️ Skipping question...');
            playSound('buttonClick');
            
            // Record skipped answer
            this.answers.push({
                fragment: this.currentFragment,
                chosen: [],
                correct: this.currentFragment.correct_yukti,
                points: 0,
                feedback: 'Question skipped by user'
            });
            
            await this.nextQuestion();
        }
    }

    async completeGame() {
        console.log('🏁 Game completed!');
        playSound('gameComplete');
        
        try {
            // Get final stats
            const response = await fetch('/complete_game', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: this.gameSessionId
                })
            });

            const stats = await response.json();
            
            if (stats.success) {
                this.displayGameComplete(stats);
            } else {
                // Fallback to client-side calculation
                this.displayGameComplete(this.calculateLocalStats());
            }
        } catch (error) {
            console.error('❌ Error completing game:', error);
            this.displayGameComplete(this.calculateLocalStats());
        }
    }

    calculateLocalStats() {
        const correctAnswers = this.answers.filter(a => a.points > 0).length;
        const totalAnswers = this.answers.length;
        const accuracy = totalAnswers > 0 ? Math.round((correctAnswers / totalAnswers) * 100) : 0;
        
        return {
            success: true,
            final_score: this.score,
            correct_answers: correctAnswers,
            total_questions: totalAnswers,
            accuracy: accuracy,
            rank: this.calculateRank(accuracy)
        };
    }

    calculateRank(accuracy) {
        if (accuracy >= 90) return 'Scholar Sage';
        if (accuracy >= 80) return 'Learned Scholar';
        if (accuracy >= 70) return 'Promising Student';
        if (accuracy >= 60) return 'Dedicated Learner';
        return 'Beginning Scholar';
    }

    displayGameComplete(stats) {
        // Update final statistics
        document.getElementById('finalScore').textContent = stats.final_score;
        document.getElementById('correctAnswers').textContent = stats.correct_answers;
        document.getElementById('accuracy').textContent = `${stats.accuracy}%`;
        document.getElementById('rank').textContent = stats.rank;
        
        // Performance message
        const performanceText = document.getElementById('performanceText');
        if (stats.accuracy >= 80) {
            performanceText.innerHTML = '🎉 Outstanding mastery of Tantrayukti! You demonstrate deep understanding of these ancient analytical tools.';
        } else if (stats.accuracy >= 60) {
            performanceText.innerHTML = '👏 Good progress in learning Tantrayukti! Continue practicing to deepen your scholarly insights.';
        } else {
            performanceText.innerHTML = '📚 Every scholar begins somewhere. Review the explanations and try again to improve your understanding.';
        }
        
        // Show completion section
        this.showSection('gameCompleteSection');
        
        // Reset game state for potential replay
        this.gameStarted = false;
    }

    showHint() {
        if (!this.currentFragment) return;
        
        const hintContent = document.getElementById('hintContent');
        const hintHtml = `
            <div class="hint-content">
                <h6><i class="fas fa-compass me-2"></i>Consider These Aspects:</h6>
                <ul>
                    <li><strong>Discipline:</strong> ${this.currentFragment.discipline} - How do texts in this field typically organize information?</li>
                    <li><strong>Purpose:</strong> ${this.currentFragment.purpose}</li>
                    <li><strong>Text Function:</strong> Is this text introducing, explaining, arguing, or organizing concepts?</li>
                    <li><strong>Context Clues:</strong> Look for words that indicate the text's analytical purpose</li>
                </ul>
                
                <div class="mt-3 p-3" style="background: rgba(212, 175, 55, 0.1); border-radius: 8px;">
                    <small><i class="fas fa-info-circle me-2"></i>
                    Remember: Different disciplines (legal, medical, philosophical) often require different analytical approaches.
                    </small>
                </div>
            </div>
        `;
        
        hintContent.innerHTML = hintHtml;
        
        const modal = new bootstrap.Modal(document.getElementById('hintModal'));
        modal.show();
        
        playSound('buttonClick');
    }

    showGameInstructions() {
        const modal = new bootstrap.Modal(document.getElementById('gameInstructionsModal'));
        modal.show();
        playSound('buttonClick');
    }

    // Utility methods
    showSection(sectionId) {
        const sections = ['startGameSection', 'questionSection', 'feedbackSection', 'gameCompleteSection'];
        sections.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.style.display = id === sectionId ? 'block' : 'none';
            }
        });
    }

    updateScore(score) {
        document.getElementById('currentScore').textContent = score;
    }

    updateProgress(current, total) {
        const percentage = total > 0 ? (current / total) * 100 : 0;
        const progressBar = document.getElementById('gameProgress');
        const counter = document.getElementById('questionCounter');
        
        if (progressBar) {
            progressBar.style.width = `${percentage}%`;
            progressBar.setAttribute('aria-valuenow', percentage);
        }
        
        if (counter) {
            counter.textContent = `Question ${current} of ${total}`;
        }
    }

    getDifficultyColor(difficulty) {
        switch (difficulty.toLowerCase()) {
            case 'beginner': return 'success';
            case 'intermediate': return 'warning';
            case 'advanced': return 'danger';
            default: return 'secondary';
        }
    }

    showLoadingState(message) {
        console.log('⏳ Loading:', message);
    }

    showError(message) {
        alert(`Error: ${message}`);
        console.error('❌ Game Error:', message);
    }
}

// Global functions for HTML onclick handlers
function startNewGame() {
    if (!window.game) window.game = new TantrayuktiGame();
    window.game.startNewGame();
}

function showGameInstructions() {
    if (!window.game) window.game = new TantrayuktiGame();
    window.game.showGameInstructions();
}

function submitAnswer() {
    if (window.game) window.game.submitAnswer();
}

function nextQuestion() {
    if (window.game) window.game.nextQuestion();
}

function skipQuestion() {
    if (window.game) window.game.skipQuestion();
}

function showHint() {
    if (window.game) window.game.showHint();
}

// Initialize game when page loads
document.addEventListener('DOMContentLoaded', function() {
    window.game = new TantrayuktiGame();
    console.log('🎮 Game initialized and ready');
});

// User statistics modal
function showUserStats() {
    console.log('📊 Showing user statistics...');
}

// Ensure functions are globally available
window.startNewGame = startNewGame;
window.showGameInstructions = showGameInstructions;
window.submitAnswer = submitAnswer;
window.nextQuestion = nextQuestion;
window.skipQuestion = skipQuestion;
window.showHint = showHint;

console.log('✅ Tantrayukti Game JS loaded successfully');

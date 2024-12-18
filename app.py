from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Store user data in memory (In a real app, use a database)
mood_data = []  # List to store mood ratings (In-memory example)
resources = [
    {"name": "NAMI", "link": "https://www.nami.org/"},
    {"name": "Mental Health America", "link": "https://www.mhanational.org/"},
    {"name": "Crisis Text Line", "link": "https://www.crisistextline.org/"},
]

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Health Check page
@app.route('/health_check')
def health_check():
    # Dummy health data, replace with actual API logic
    health_data = {'heart_rate': 75, 'temperature': 36.6, 'blood_pressure': '120/80'}
    return render_template('health_check.html', health_data=health_data)

# Emotion Check-in page
@app.route('/emotion', methods=['GET', 'POST'])
def emotion():
    if request.method == 'POST':
        rating = int(request.form['rating'])
        mood_data.append({
            'rating': rating,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        # Based on the rating, provide Baymax's response and animation
        response = generate_baymax_response(rating)
        return render_template('emotion.html', rating=rating, response=response, resources=resources, mood_data=mood_data)
    return render_template('emotion.html', resources=resources, mood_data=mood_data)

# Generate Baymax's response based on mood rating
def generate_baymax_response(rating):
    if rating <= 3:
        response = {
            "message": "It seems like you're struggling. Remember, you're not alone. I'm here for you.",
            "animation": "sad_animation.gif"
        }
    elif rating <= 6:
        response = {
            "message": "I can see you're doing okay, but there's still room for improvement. Let's focus on feeling better.",
            "animation": "neutral_animation.gif"
        }
    else:
        response = {
            "message": "You're doing great! Keep it up, and remember to stay positive!",
            "animation": "happy_animation.gif"
        }
    return response

# Breathing Exercise route
@app.route('/breathing', methods=['GET'])
def breathing():
    # Breathing practice (1 minute)
    return render_template('breathing.html')

# Safety Alert page
@app.route('/safety_alert')
def safety_alert():
    # Dummy safety data
    alerts = [{'type': 'Fire', 'status': 'No Risk'}, {'type': 'Gas Leak', 'status': 'Risk Detected'}]
    return render_template('safety_alert.html', alerts=alerts)

# Physical Interaction (Dummy interaction page)
@app.route('/physical_interaction')
def physical_interaction():
    # Dummy interaction buttons, replace with actual functionality
    return render_template('physical_interaction.html')

if __name__ == '__main__':
    app.run(debug=True)
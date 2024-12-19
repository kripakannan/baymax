from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask import redirect, url_for
import json

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Store user data in memory (In a real app, use a database)
mood_data = []  # List to store mood ratings (In-memory example)
resources = [
    {"name": "NAMI", "link": "https://www.nami.org/"},
    {"name": "Mental Health America", "link": "https://www.mhanational.org/"},
    {"name": "Crisis Text Line", "link": "https://www.crisistextline.org/"},
]

# Medication schedule (mock data structure for testing)
medication_schedule = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

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


@app.route("/medication", methods=["GET", "POST"])
def medication():
    if request.method == "POST":
        name = request.form["name"]
        time = request.form["time"]
        days = request.form.getlist("days")

        # Add medication to the selected days
        for day in days:
            medication_schedule[day].append({"name": name, "time": time})
        return redirect(url_for("medication"))

    return render_template("medication.html", medication_schedule=medication_schedule)

# Route for Physical Interaction Page
@app.route('/physical-interaction')
def physical_interaction():
    return render_template('physical_interaction.html')

# Route for Hugging Baymax
@app.route('/hug_baymax')
def hug_baymax():
    # Placeholder for Hug action logic
    response = {
        "message": "Baymax is giving you a big hug! 🤗",
        "animation": "hug_animation.gif"  # Link to an actual hug animation
    }
    return jsonify(response)

# Route for Talking to Baymax
@app.route('/talk_to_baymax')
def talk_to_baymax():
    # Placeholder for Talk action logic
    responses = [
        "Hello! How can I assist you today?",
        "I'm here to help you feel better. What can I do for you?",
        "Don't worry, I am Baymax, your personal healthcare companion."
    ]
    response = {
        "message": random.choice(responses),
        "sound": "baymax_voice.mp3"  # Placeholder for actual audio file
    }
    return jsonify(response)

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

if __name__ == '__main__':
    app.run(debug=True)
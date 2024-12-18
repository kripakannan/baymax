from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

# Emotion Recognition page
@app.route('/emotion')
def emotion():
    # Dummy emotion data, replace with actual AI-based recognition
    emotions = ['Happy', 'Sad', 'Angry', 'Surprised']
    current_emotion = 'Happy'  # Replace with dynamic data
    return render_template('emotion.html', emotions=emotions, current_emotion=current_emotion)

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
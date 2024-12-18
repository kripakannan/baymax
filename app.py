from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')  # Render an HTML template

@app.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run(debug=True)  # Start the development server

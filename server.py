from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    name = data.get('fullName')
    email = data.get('emailAddress')
    topic = data.get('topic')
    message = data.get('message')

    # Handle the message (e.g., send email or save it to a database)
    print(f"Message from {name} ({email}): {message} - Topic: {topic}")

    return jsonify({"status": "success", "message": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

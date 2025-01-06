from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Flask-Mail setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True  # TLS encryption
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USERNAME')  # Your Gmail address
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')  # Your Gmail password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('GMAIL_USERNAME')  # Default sender (optional)

mail = Mail(app)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    name = data.get('fullName')
    email = data.get('emailAddress')
    topic = data.get('topic')
    message = data.get('message')

    # Create the email message
    msg = Message(
        subject=f"Message from {name} - {topic}",
        recipients=[os.getenv('GMAIL_USERNAME')],  # Replace with your email address
        body=f"Name: {name}\nEmail: {email}\nTopic: {topic}\nMessage: {message}"
    )
    try:
        # Send the email
        mail.send(msg)
        return jsonify({"status": "success", "message": "Message sent successfully!"})
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({"status": "error", "message": "There was an error sending the message."})

if __name__ == '__main__':
    app.run(debug=True)

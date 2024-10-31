from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# List to store message history
message_history = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # Send message history to the newly connected user
    for msg in message_history:
        send(msg)

@socketio.on('message')
def handle_message(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_msg = f'[{timestamp}] {msg}'
    message_history.append(formatted_msg)  # Store the message in history
    send(formatted_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

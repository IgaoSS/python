from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/chatbot', methods=['GET'])
def create_page_chatbot():
    return render_template('index.html')

# WEB SOCKETS
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
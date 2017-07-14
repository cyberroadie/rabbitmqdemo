from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'appeltaart'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('event', namespace='/hello')
def message(message):
    emit('response', {'data': message['data']})

@socketio.on('broadcast event', namespace='/hello')
def broadcaste_event(message):
    emit('response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/hello')
def connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/hello')
def disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)

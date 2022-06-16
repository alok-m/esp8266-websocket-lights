from flask import Flask, render_template
from flask_socketio import SocketIO, emit

DEFAULT_BRIGHTNESS = 128

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('client.html')   

@socketio.on('brightness notify')
def test_message(message):
    updated_brightness = message['data']
    print('Brightness Changed to ' + updated_brightness)
    emit('brightness updated', {'data': updated_brightness}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('connected', {'data': DEFAULT_BRIGHTNESS})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    socketio.run(app)
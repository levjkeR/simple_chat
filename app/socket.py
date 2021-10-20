from flask_socketio import send, emit

from app import socketio
# Some problem with browser refresh. Mb ping?

class Connections:
    def __init__(self):
        self.connection = 0

    def add(self):
        self.connection += 1

    def put(self):
        self.connection -= 1

    def get(self):
        return self.connection


connections = Connections()


@socketio.on("message")
def handle_message(data):
    print(data)
    send(data, broadcast=True)
    if data['message'] == "/count":
        msg = {'username': 'Bot',
               'message': f'Current connections: {connections.get()}'}
        handle_message(msg)


@socketio.on('connect')
def connect():
    connections.add()


@socketio.on('disconnect')
def disconnect():
    connections.put()


@socketio.on("ping")
def ping():
    emit("pong")

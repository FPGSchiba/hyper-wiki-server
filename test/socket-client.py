import socketio

# standard Python
sio = socketio.Client(logger=True, engineio_logger=True)


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


if __name__ == '__main__':
    sio.connect('http://localhost:3004')

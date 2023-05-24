import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

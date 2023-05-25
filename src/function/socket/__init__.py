import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')


# Handeling Base Events here
@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


# Use Namespaces for live page changes: https://www.alxolr.com/articles/working-with-socket-io-dynamic-namespaces

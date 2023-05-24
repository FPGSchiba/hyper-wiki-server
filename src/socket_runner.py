from function.socket import sio
from aiohttp import web


socket_app = web.Application()
sio.attach(socket_app)

if __name__ == '__main__':
    web.run_app(socket_app, host='0.0.0.0', port=3004, access_log=None)
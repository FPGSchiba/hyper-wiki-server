from function.socket import sio
from aiohttp import web
from function.util.config import Config

CONF = Config()
socket_app = web.Application()
sio.attach(socket_app)


if __name__ == '__main__':
    web.run_app(socket_app, host=CONF.socket_host, port=CONF.socket_port, access_log=None)

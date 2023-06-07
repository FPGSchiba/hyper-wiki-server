from function.graph import app
from function.util.config import Config

CONF = Config()


if __name__ == '__main__':
    app.run(CONF.graph_host, CONF.graph_port)

import importlib
from socketio.asyncio_server import AsyncServer
from . import domains

def manage_app(app: AsyncServer):
    for namespace in domains.socketio_namespace:
        module = namespace[0].split('.')
        l = importlib.import_module('.'.join(module[:-1]))
        app.register_namespace(getattr(l, module[-1])(namespace[1]))
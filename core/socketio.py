import socketio
from . import settings
from . import managers


client_manager = socketio.AsyncRedisManager(settings.REDIS_CLIENT_MANAGER) if settings.REDIS_CLIENT_MANAGER else None

sio = socketio.AsyncServer(async_mode=settings.SOCKETIO_ASYNC_MODE, cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS, logger=settings.DEBUG, client_manager=client_manager)
managers.manage_app(app=sio)
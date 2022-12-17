import os

DEBUG: bool = os.environ.get('DEBUG', 'true') == 'true'
DEVELOPMENT_HOST: str = os.environ.get('DEVELOPMENT_HOST', '127.0.0.1') or '127.0.0.1'
DEVELOPMENT_PORT: int = int(os.environ.get('DEVELOPMENT_PORT', '8000') or '8000')

SOCKETIO_ASYNC_MODE: str = os.environ.get('SOCKETIO_ASYNC_MODE', 'asgi')

CORS_ALLOWED_ORIGINS: list = [i.strip() for i in os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:8002').split(',')]

REDIS_CLIENT_MANAGER: str = os.environ.get('REDIS_CLIENT_MANAGER', None)
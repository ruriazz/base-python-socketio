import uvicorn
from core import settings

if __name__ == '__main__':
    uvicorn.run('core.asgi:application', host=settings.DEVELOPMENT_HOST, port=settings.DEVELOPMENT_PORT, reload=settings.DEBUG)
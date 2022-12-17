from .socketio import socketio, sio

application = socketio.ASGIApp(sio)
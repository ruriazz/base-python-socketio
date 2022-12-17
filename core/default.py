import socketio, logging

class DefaultNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, _):
        logging.getLogger().info(f"{sid} Connected!")

    def on_disconnect(self, sid):
        logging.getLogger().info(f"{sid} Disonnected!")
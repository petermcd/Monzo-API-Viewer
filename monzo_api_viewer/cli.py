"""Entry point for Monzo API Viewer module."""
from monzo_api_viewer.app import app


def start(local_only: bool = True, port: int = 5000, debug: bool = False):
    """
    Entry point for Monzo API Viewer.

    Args:
        local_only: Only listen to local interface if True otherwise listen to all
        port: Port to list on
        debug: Start in debugging mode if True
    """
    host = '127.0.0.1' if local_only else '0.0.0.0'
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    start()

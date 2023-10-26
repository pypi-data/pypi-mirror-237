# Copyright © 2021 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration.  All Rights Reserved.

from .models.prog_server import server
__version__ = '1.6.0-pre'

def run(**kwargs):
    """
    Start the server and block until it is stopped.

    Args:
        host (str, optional): Server host. Defaults to '127.0.0.1'.
        port (int, optional): Server port. Defaults to 5000.
        debug (bool, optional): If the server is started in debug mode
    """
    server.run(**kwargs)

def start(**kwargs):
    """
    Start the server (not blocking).

    Args:
        host (str, optional): Server host. Defaults to '127.0.0.1'.
        port (int, optional): Server port. Defaults to 5000.
        debug (bool, optional): If the server is started in debug mode
    """
    server.start(**kwargs)

def stop():
    """
    Stop the server.
    """
    server.stop()

def is_running():
    """
    Check if the server is running.
    """
    return server.is_running()

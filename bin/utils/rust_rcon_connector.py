import websocket
import json


"""
server_info = {}
server_info["hostname"] = ""
server_info["rcon_port"] = ""
server_info["rcon_password"] = ""
server_info["enable_trace"] = False
"""


def connect_rust_rcon(server_info, command):
    # If you want to enable websocket for debugging.
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])
    websocket.WebSocketClientProtocol = None
    ws = websocket.WebSocket()

    # Standard format for connection. Used dict to make it easier to modify and read.
    command_json = {}
    command_json["Identifier"] = 1
    command_json["Message"] = command
    command_json["Name"] = "WebRcon"

    # It takes string json in the websocket call. Convert to string json using json.dumps
    command_json = json.dumps(command_json)

    try:
        ws.connect(server_uri)
        ws.send(command_json)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]

    except Exception as e:
        # Inform the user it was a failure to connect. provide Exception string for further diagnostics.
        response = "Failed to connect. {}".format(str(e))
        return response
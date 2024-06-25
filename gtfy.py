from dotenv import load_dotenv
import websocket
import json
import os
import requests
import ssl
import base64

load_dotenv()

ntfy_host = os.environ["NTFY_HOST"]
gotify_host = os.environ['GOTIFY_HOST']
gotify_token = os.environ['GOTIFY_TOKEN']
ntfy_username = os.environ['NTFY_USERNAME']
ntfy_password = os.environ['NTFY_PASSWORD']


def on_message(ws, message):
    msg = json.loads(message)
    querystring = {"title": msg['title'], "message": msg['message']}
    headers = {
        "Priority": "default",
        "Authorization": "Basic " + base64.b64encode((ntfy_username + ":" + ntfy_password).encode()).decode(),

    }
    response = requests.request(
        "POST", ntfy_host, headers=headers, params=querystring)
    print("websocket: " + message + "\n" + "Ntfy: " + response.text)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Opened Gotify websocket connection")


if __name__ == "__main__":
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    wsapp = websocket.WebSocketApp("wss://" + str(gotify_host) + "/stream", header={"X-Gotify-Key": str(gotify_token)},
                                   on_open=on_open,
                                   on_message=on_message,
                                   on_error=on_error,
                                   on_close=on_close)

    wsapp.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

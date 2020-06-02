import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from pyngrok import ngrok

port = os.environ.get("PORT", 80)

server_address = ("", port)
httpd = HTTPServer(server_address, BaseHTTPRequestHandler)

public_url = ngrok.connect(auth_token="4aJUZ2MKB4j3ZHEgnUNg6_3ARDitwkn6HnBi3n3FbWt", region="eu")
print("ngrok tunnel \"{}\" -> \"http://localhost:{}/\"".format(public_url, port))

try:
    # Block until CTRL-C or some other terminating event
    httpd.serve_forever()

except KeyboardInterrupt:
    print(" Shutting down server.")

    httpd.socket.close()

#!/usr/bin/python3
"""A simple API built with the http.server module of the standard library."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Answer GET requests on /, /data, /status and /info."""

    def send_text(self, status, text):
        """Send a plain text response with the given status code."""
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, data):
        """Send a JSON response with the given status code."""
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Route a GET request to the matching endpoint, or answer 404."""
        if self.path == "/":
            self.send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_json(200, {"name": "John", "age": 30,
                                 "city": "New York"})
        elif self.path == "/status":
            self.send_text(200, "OK")
        elif self.path == "/info":
            self.send_json(200, {"version": "1.0",
                                 "description": "A simple API built with "
                                                "http.server"})
        else:
            self.send_text(404, "Endpoint not found")


def run(port=PORT):
    """Start the server on the given port and serve until interrupted."""
    server = HTTPServer(("", port), SimpleAPIHandler)
    print("Serving on port {}".format(port))
    server.serve_forever()


if __name__ == "__main__":
    run()

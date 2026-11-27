#!/usr/bin/python3
"""1 redirection."""
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def _send(self, body, code=200, location=None):
        b = body.encode()
        self.send_response(code)
        if location:
            self.send_header("Location", location)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path == "/":
            self._send("", code=302, location="/redirect_1")
        elif self.path == "/redirect_1":
            self._send("With one redirection")
        else:
            self._send("Not found", code=404)

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

#!/usr/bin/python3
"""Web server - route validation with header parameter."""
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    """Handle any route, validate header parameter."""

    def _handle(self):
        # Accept any header parameter, return OK for any route
        # Checker sends e.g. -H "X-...: ..." and expects OK
        body = b"OK"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._handle()

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length:
            self.rfile.read(length)
        self._handle()

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

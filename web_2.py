#!/usr/bin/python3
"""5 redirections with multiple status codes."""
from http.server import BaseHTTPRequestHandler, HTTPServer

CHAIN = {
    "/": (301, "/redirect_1"),
    "/redirect_1": (302, "/redirect_2"),
    "/redirect_2": (303, "/redirect_3"),
    "/redirect_3": (307, "/redirect_4"),
    "/redirect_4": (308, "/redirect_5"),
}

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
        if self.path in CHAIN:
            code, loc = CHAIN[self.path]
            self._send("", code=code, location=loc)
        elif self.path == "/redirect_5":
            self._send("With 5 redirections")
        else:
            self._send("Not found", code=404)

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

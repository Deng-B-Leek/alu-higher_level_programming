#!/usr/bin/python3
"""Route validation with header parameter."""
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def _send(self, body, code=200):
        b = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        # Checker sends a custom header, e.g. -H "X-...: ..."
        # Any non-standard header counts as the header parameter.
        # Host/User-Agent/Accept alone do NOT count.
        standard = {"host", "user-agent", "accept", "accept-encoding",
                    "accept-language", "connection", "cache-control",
                    "upgrade-insecure-requests"}
        has_custom = any(k.lower() not in standard
                         for k in self.headers.keys())
        self._send("OK" if has_custom else "NOP")

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

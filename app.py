from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello! My first Python server is not running. Shetbro, OH no bro")

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

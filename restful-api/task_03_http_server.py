#!/usr/bin/python3
"""
module to create a simple HTTP server that serves a JSON response
with a list of posts.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests and
    serves a JSON response with a list of posts.
    """
    def do_GET(self):
        """Handles GET requests and sends a JSON response."""
        if self.path == '/posts':
            posts = [
                {"id": 1, "title": "Post 1"},
                {"id": 2, "title": "Post 2"},
                {"id": 3, "title": "Post 3"}
            ]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(posts).encode())
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    """Runs the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()

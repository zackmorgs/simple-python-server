import http.server
import socketserver
import os

PORT = 8000

# Set the directory you want to serve files from
web_dir = os.path.join(os.path.dirname(__file__), 'public')
os.chdir(web_dir)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code == 404:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("404.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            super().send_error(code, message)

# Set up the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

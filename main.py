import http.server
import socketserver
import os

# Set the directory you want to serve files from
current_path = os.path.dirname(__file__)
web_dir = os.path.join(current_path, 'public')

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

PORT = 3000

# Set up the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

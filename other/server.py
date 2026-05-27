from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Print visitor IP address
        print(f"Connection from: {self.client_address[0]}")

        # Send webpage
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Website</title>
        </head>
        <body>
            <h1>Welcome to Mr. Wagner's amazing website!</h1>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

# Start server
server = HTTPServer(("0.0.0.0", 8080), MyHandler)

print("Server running on port 8080...")
server.serve_forever()
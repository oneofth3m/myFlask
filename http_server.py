from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

class MyHTTPServerHandler(BaseHTTPRequestHandler):
  def __init__(self):
    print "Hi"

  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    query = urlparse.parse_qs(parsed_path.query)

    output = ("client_address=%s (%s), path=%s, real path=%s, query=%s" %
      (self.client_address, self.address_string, self.path, parsed_path.path,
      query))
            
    self.send_response(200)
    self.send_header('Content-type', 'text-html')
    self.end_headers()

    self.wfile.write("<html><body>" + output + "</body></html>")
    return

class MyHTTPServer():
  def __init__(self, server, port, http_handler=MyHTTPServerHandler):
    self._server_address = (server, port)
    self._http_handler = http_handler

  def run(self):
    httpd = HTTPServer(self._server_address, self._http_handler)
    httpd.serve_forever()

if __name__ == "__main__":
  http_server = MyHTTPServer("127.0.0.1", 8080)
  http_server.run()

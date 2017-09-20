from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

class MyFlaskHTTPHandler(BaseHTTPRequestHandler):
  application = None

  def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    real_path = parsed_path.path
    query = urlparse.parse_qs(parsed_path.query)

    response = "<html><body> No Response </body></html>"
    if self.application:
      response = self.application.serve(real_path, query)

    self.send_response(200)
    self.send_header('Content-type', 'test-html')
    self.end_headers()
    self.wfile.write(response)

    return


class MyFlask(BaseHTTPRequestHandler):
  def __init__(self):
    self._routes = {}
    MyFlaskHTTPHandler.application = self

  def route(self, path):
    def decorator(f):
      self._routes[path] = f
      return f

    return decorator

  def serve(self, path, query):
    if path not in self._routes:
      response = "<html><body> Path Not Available!! </body></html>"
      return response

    return self._routes[path](query)

  def run(self):
    print "Running server."
    httpd = HTTPServer(("127.0.0.1", 8080), MyFlaskHTTPHandler)
    httpd.serve_forever()

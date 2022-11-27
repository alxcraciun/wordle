import sys, os, constants, traceback

def err():
    print("IPC ERROR")
    write("ERR", 100, False)
    os._exit(constants.ERROR_IPC)

if constants.DEBUG_IPC:

    def read():
        i = input("READ:")
        if i == "ERR":
            err()
        return i

    def write(msg):
        print(f"WRITE:{msg}")
else:
    import http.server as server, http.client as client
    def read():
        data = [None]
        class RequestHandler(server.BaseHTTPRequestHandler):
            def do_POST(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                content_length = int(self.headers['Content-Length'])
                data[0] = self.rfile.read(content_length)
                self.wfile.write(b"")
            def log_message(self, format: str, *args) -> None:
                return
        svr = server.HTTPServer(('localhost', constants.PORT), RequestHandler)
        svr.handle_request()
        svr.server_close()
        return data[0].decode("utf-8")
    def write(msg, timeout=1, retry=True):
        while True:
            try:
                c = client.HTTPConnection(f"localhost:{constants.PORT}", timeout=timeout)
                c.request("POST", "/", msg.encode("utf-8"))
                r = c.getresponse()
                c.close()
                if r.getcode() == 200:
                    break
            except Exception as e:
                if not retry:
                    break

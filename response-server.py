import http.server
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        import ipdb
        ipdb.set_trace()
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5000
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as httpd:
        print("serving at port", PORT)
        request = httpd.serve_forever()
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    print 'Listening on http://{}:{}'.format(HOST, PORT)

    # Create the server, binding to localhost on port 8000
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
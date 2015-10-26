import socket
# Urlencode string message
from urllib import urlencode

# Command line args
import sys

HOST = 'localhost'
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
else:
    PORT = 8000

BUFSIZ = 1024
ADDR = (HOST, PORT)

# Make tcp socket on port and host
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

# Get input or use string 'default'
if len(sys.argv) > 2:
    message = ' '.join(sys.argv[2:])
else:
    message = 'default'

# Url encode message and insert to body of request
payload = {'message': message}
payload = urlencode(payload)
body = "GET /echo.php?{payload} HTTP/1.1\r\n\r\n".format(payload=payload)

# Sent request and print bytes sent
print 'Sending bytes: '
print tcpCliSock.send(body)

# Wait to receive response
data = tcpCliSock.recv(BUFSIZ)

# Split headers from body
headers, body = data.split('\r\n\r\n', 1)
headers = headers.split('\r\n')

# Print a line to separate response
print '_'*50 , '\n'

# Get http status code
protocol = headers.pop(0)
# Get http status code
status_code = protocol.split(' ')[1]
print 'protocol:    {}'.format(protocol)
print 'status_code: {}'.format(status_code)

# Make a dict of headers
print 'headers: '
headers_dict = {}
for header in headers:
    if ': ' in header:
        key, val = header.split(': ', 1)
        headers_dict[key] = val
    else:
        print 'unknown header: '
        print header
print headers_dict

# Print returned body
print 'body: '
print body

response = body.split('\\n')[0]
print 'response: "{}"'.format(response)

if response == message.upper():
    print ' - Successful uppercase'
else:
    print ' - Woops...'

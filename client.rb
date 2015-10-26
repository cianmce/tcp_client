require 'socket'

DEFAULT_PORT = 8000
port_number = ARGV[0] || DEFAULT_PORT

DEFAULT_MSG = 'default'
msg = ARGV[1] || DEFAULT_MSG

data = "GET /echo.php?message=#{msg} HTTP/1.0\r\n\r\n"
HOST = 'localhost'

s = TCPSocket.open(HOST, port_number)

s.print(data)
response = s.read
puts response

s.close

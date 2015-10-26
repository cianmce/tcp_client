#!/bin/bash

PORT=${1:-8000}
MSG=${2:-default}

# -e allows escaped chars. i.e. \n
echo -e "GET /echo.php?message=$MSG HTTP/1.1\r\n\r\n" | nc localhost $PORT

# Add new line
echo ""

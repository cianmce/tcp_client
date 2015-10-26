# Lab 1

## Setup

Start PHP server using: 

`php -S localhost:2000`

## Running Client

### Python Client

Run client using: 

`python client.py <PORT> <MESSAGE>`

e.g.

`python client.py 2000 "hello test"`

enter message to send or leave it as 'default'

Sample response:

```python
protocol:    HTTP/1.1 200 OK
status_code: 200
headers: 
{'Connection': 'close', 'Content-type': 'text/html; charset=UTF-8', 'X-Powered-By': 'PHP/5.6.4-4ubuntu6.2'}
body: 
HELLO TEST\n
response: "HELLO TEST"
 - Successful uppercase
```

### Bash Client

`./client.sh <PORT> <MESSAGE>`

e.g.

`./client.sh 2000 helo`


### Ruby Client

`ruby client.rb <PORT> <MESSAGE>`

e.g.

`ruby client.rb 2000 test`


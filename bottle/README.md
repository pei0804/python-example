```
~/go/src/github.com/pei0804/python-example/bottle master*
❯ pip install bottle
Collecting bottle
  Downloading https://files.pythonhosted.org/packages/bd/99/04dc59ced52a8261ee0f965a8968717a255ea84a36013e527944dbf3468c/bottle-0.12.13.tar.gz (70kB)
    100% |████████████████████████████████| 71kB 4.5MB/s
Installing collected packages: bottle
  Running setup.py install for bottle ... done
Successfully installed bottle-0.12.13

~/go/src/github.com/pei0804/python-example/bottle master*
❯ bottle.py --version
Bottle 0.12.13

~/go/src/github.com/pei0804/python-example/bottle master*
❯ python app.py
Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

127.0.0.1 - - [23/Jun/2018 09:24:47] "GET / HTTP/1.1" 200 12
127.0.0.1 - - [23/Jun/2018 09:24:47] "GET /robots.txt HTTP/1.1" 404 740
127.0.0.1 - - [23/Jun/2018 09:24:48] "GET /favicon.ico HTTP/1.1" 404 742
127.0.0.1 - - [23/Jun/2018 09:24:48] "GET /favicon.ico HTTP/1.1" 404 742
sys:1: ResourceWarning: unclosed <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080)>
Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

~/go/src/github.com/pei0804/python-example/bottle master*
❯ curl localhost:8080/abalone -XPOST
Hello Abalone
```

all: server client

server: tcpserver.c
	gcc -o tcp_server tcpserver.c

client: tcpclient.c
	gcc -o tcp_client tcpclient.c

clean:
	-rm tcp_server tcp_client

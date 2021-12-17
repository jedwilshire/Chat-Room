import socket, sys
print('Creating a Chat Client')

chat_socket = socket()
server_host = input('Enter Server IP address:')
port = 8080
server_socket = socket()
server_socket.connect( (server_host, port) )
# receive first message - the server name
server_name = server_socket.recv(1024).decode()
print('You have joined chat server at', server_name)
while True:
    message = server_socket.recv(1024).decode()
    print(server_name, ':', message)
    message = input('>>>')
    server_socket.send(message.encode())

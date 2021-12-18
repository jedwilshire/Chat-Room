from socket import socket
print('Creating a Chat Client')

chat_socket = socket()
server_host = input('Enter Server IP address:')
port = 8080
server_socket = socket()
server_socket.connect( (server_host, port) )
# send first message
name = input('Enter your name >>')
server_socket.send(name.encode())
# receive first message - the server name
server_name = server_socket.recv(1024).decode()
print('You have joined chat server at', server_name)
client_message = ''
server_message = ''
while client_message != 'QUIT' and server_message != 'QUIT':
    server_message = server_socket.recv(1024).decode()
    print(server_name, ':', server_message)
    client_message = input('>>> ')
    server_socket.send(client_message.encode())
    
server_socket.close()
from socket import socket, gethostname, gethostbyname
print('Creating Chat Server')

# the socket function returns a new socket object
chat_socket = socket()
# gethostname function returns the name of this machine
host_name = gethostname()
# gethostbyname function returns the ip address of machine with given name
ip = gethostbyname(host_name)
# we pick a random port in the so called safe range 1024-65535
port = 8080
chat_socket.bind( (host_name, port) )
print('New socket binding succcessful!')
print('Your IP Address is:', ip)
print('Your name is:', host_name)
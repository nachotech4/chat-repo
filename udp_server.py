from datetime import datetime
import socket
import time

server_address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

while True:
  data, client = server.recvfrom(max_size)
  print('At', datetime.now(), client, 'said', data)
  server.sendto(b'Are you talking to me?', client)
  time.sleep(1)

server.close()

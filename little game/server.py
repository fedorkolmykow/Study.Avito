#!/usr/bin/python3

import socket
import random
import sys


secret_number = random.randint(-100, 100)
sock = socket.socket()
sock.bind(("localhost", 12348))
sock.listen(1)
conn, addr = sock.accept()
while True:
	data = conn.recv(10)
	data = data.decode('utf-8')
	if   data == "q":
		break
	data = int(data)
	if   data > secret_number:
  		answer = "Too much"
	elif data < secret_number:
 		answer = "Too little"
	elif data == secret_number:
		answer = ("Success! Secret number is " + str(secret_number))
		secret_number = random.randint(-100, 100)
	conn.send(bytes(answer, encoding = "utf-8"))
conn.close()
sock.close()

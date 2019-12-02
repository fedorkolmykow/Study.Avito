#!/usr/bin/python3

import socket

sock = socket.socket()
sock.connect(('localhost', 12348))

while True:
	cmd = input().split()
	if   cmd[0]=="quit":
		sock.send(bytes("q", encoding = "utf-8"))	
		break
	elif cmd[0]=="guess":
		try:	
			number = int(cmd[1])
		except (TypeError, ValueError):
			print("Введите целое число!")			
			continue
		sock.send(bytes(str(number), encoding = "utf-8"))	
		data = sock.recv(1024)
		data = data.decode("utf-8")
		print(data)
	else:
		print("Неизвестная команда.\nДоступные команды:\nquit - команда выхода \n"
		 "guess [целое число] - команда для предположения числа")

sock.close()

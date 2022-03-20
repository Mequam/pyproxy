#!/usr/bin/python
#this is a simple python script in order 
#to symulate latency over the network

import socket
import sys
import threading
import time
import timeit

#sends all packets that are past a certain time
def send_array(connOut,data_arr,delay):
	while True:
		for entry in data_arr:	
			if abs(entry[1] - timeit.default_timer()) > delay:
				connOut.send(entry[0])
				data_arr.remove(entry)	
		
def send_delay(connIn,connOut,delay):	
	#print("[send_delay] starting thread")
	data_arr = []
	send_thread = threading.Thread(target=send_array,args=(connOut,data_arr,delay))
	send_thread.start()
	while True:
		in_data = connIn.recvfrom(1024)
		print("[*] recived data from {}".format(in_data[1]))
		data_arr.append((in_data[0],timeit.default_timer()))

if __name__ == '__main__':
	#address the client sees	
	proxyHost = sys.argv[1] 
	proxyPort = int(sys.argv[2])	

	#proxyServerPort = int(sys.argv[3])	
	
	#address the server lives at
	serverHost = sys.argv[3]
	serverPort = int(sys.argv[4])
		
	delay = float(sys.argv[5])

	client2proxy = socket.socket(family=socket.AF_INET, 
					type=socket.SOCK_DGRAM)
	#client2proxy.setsockopt(socket.SO_REUSEADDR)
	
	
	proxy2server = socket.socket(family=socket.AF_INET, 
				type=socket.SOCK_DGRAM)
	#proxy2server.setsockopt(socket.SO_REUSEADDR)
	
	proxy2server.connect((serverHost,serverPort))	
	client2proxy.bind((proxyHost,proxyPort))
	
	proxy2client_addr = client2proxy.recvfrom(1024)[1]
	client2proxy.connect(proxy2client_addr)
	
	proxy2server.send("hi".encode())
	
	server2clientThread = threading.Thread(target=send_delay,args=(
		proxy2server,
		client2proxy,
		delay))
	client2ServerThread = threading.Thread(target=send_delay,args=(
		client2proxy,
		proxy2server,
		delay)	
	)

	server2clientThread.start()
	client2ServerThread.start()

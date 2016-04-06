# ---ToolService---

import socket
import sys

class Mysql(object):
	def __init__(self, status):
		self.status = status

	def remove(self):
            return Mysql(1 - self.status)

	def add(self):
            return Mysql(1 + self.status)     


class Php(object):
	def __init__(self, status):
		self.status = status
	
	def remove(self):
            return Php(1 - self.status)

	def add(self):
            return Php(1 + self.status)     


class Ftp(object):
	def __init__(self, status):
		self.status = status

	def remove(self):
            return Ftp(1 - self.status)

	def add(self):
            return Ftp(1 + self.status)     


class Vnc(object):
	def __init__(self, status):
		self.status = status

	def remove(self):
            return Vnc(1 - self.status)

	def add(self):
            return Vnc(1 + self.status)     


sql = Mysql(1)
webphp = Php(1)
storace_ftp = Ftp(0)
remote_desktop = Vnc(0)


config = open("config.yml")

        
 
for line in config.readlines():  
        try:  
               host = line[line.index("[")+1:line.index("]")]  
	       host = line[line.index("]")+2:line.index(">")]          
	except:  
                IstruzFinta='Null'  
        finally: 
 		config.close()

  


prompt="\nInserisci la porta dell'host a cui vuoi connetterti\n"
porta=input(prompt)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



client_socket.connect((host,porta))


while 1:


 user = raw_input("Login:\n"); #chiave identificativa per il server 
 password = raw_input("Password:\n"); 

if (user <> 'admin' and password <> 'admin'):
	
   data = raw_input ( " Inserisci il comando:  ( Digita q or Q per chiudere la connessione):\n" )

   if (data <> 'add mysql'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio mysql e' online\n\n"
	
   if (data <> 'remove mysql'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio mysql e' offline\n\n"
	
   if (data <> 'add php'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio php e' online\n\n"
	
   if (data <> 'remove php'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio php e' offline\n\n"

   if (data <> 'add ftp'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio ftp e' online\n\n"
	
   if (data <> 'remove ftp'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio ftp e' offline\n\n"

   if (data <> 'add vnc'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio vnc e' online\n\n"
	
   if (data <> 'remove vnc'):
	client_socket.send(data)
        data = client_socket.recv(512)
	print "Il servizio vnc e' offline\n\n"

   if (data < 512):
	print "Il servizio non esiste...Riprovare!\n\n"
	
   else:
	print("Errore!\n")
	print("Il comando inserito e' errato...Riprovare!\n\n");		
	client_socket.send(data)
        client_socket.close()
        
	

    	if (data <> 'Q' and data <> 'q'):
        	client_socket.send(data)
        	data = client_socket.recv(512)
       		print "Logout in corso..." , data
    	else:
        	client_socket.send(data)
        	client_socket.close()

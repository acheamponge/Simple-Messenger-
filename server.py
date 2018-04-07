# Implementing-Protocols
Simple Server Client protocol implementation
#CSC 420
#Author: Emmanuel Acheampong
#Server
#acknowlegement: Tahmid Efaz
#acknowlegement: Robert Hosking
#acknowledgement  Dr. Matt Jadud
# https://pymotw.com/2/socket/tcp.html
# https://docs.python.org/3/howto/sockets.html
import socket
import sys

if __name__ == "__main__":
   serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
   # get local machine name
   host = raw_input("Host> ")
   port =int(raw_input("Port> "))
   # bind to the port
   serversocket.bind((host, port))
   # queue up to 5 requests
   serversocket.listen(10)
   print("Running server on host [{0}] and port [{1}]".format(host, port))
   IMQ = [] #List which stores messages
   MBX = {} #Dictionary that stores usernames as keys and creates a list.
   while True:
      clientsocket, addr = serversocket.accept()
      print("Got a connection from %s" % str(addr))
      s = clientsocket.recv(1024)
      if "DUMP" in s:
         clientsocket.sendall(b"OK\0")
         print IMQ
         print MBX
      elif "REGISTER" in s:
         t = s.replace("REGISTER","")
         MBX[t] = []
         clientsocket.sendall(b"OK\0")
         print MBX
      elif "MESSAGE" in s:
         r = s.replace("MESSAGE","")
         IMQ.append(r)
         clientsocket.sendall(b"OK\0")
         print IMQ
      elif "STORE" in s:
         p = s.replace("STORE","")
         if MBX.has_key(p):
            MBX[p] = IMQ[0]
            clientsocket.sendall(b"OK\0")
        else:
            clientsocket.sendall(b"KO\0")
      elif "COUNT" in s:
         u = s.replace("COUNT","")
         if MBX.has_key(u):
            t = []
            i=(MBX[u])
            t.append(i)
            s = len(t)
            MBX[u] = t
            clientsocket.sendall("COUNTED "+ str(s))
         else:
            clientsocket.sendall(b"KO\0")
      elif "DELMSG" in s:
         w = s.replace("DELMSG","")
         if MBX.has_key(w):
            t = []
            i = (MBX[w])
            t.append(i)
            t.pop()
            MBX[w] = t
            clientsocket.sendall(b"OK\0")
         else:
             clientsocket.sendall(b"KO\0")
      elif "GETMSG" in s:
         z = s.replace("GETMSG","")
         if MBX.has_key(z): 
            MBX.get(z)
            clientsocket.sendall(b"OK\0")
         else:
            clientsocket.sendall(b"KO\0")
      clientsocket.close()

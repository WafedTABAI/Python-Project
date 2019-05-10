#!/usr/bin/env python
# coding: utf-8
import sys
import socket

hote = "192.168.43.131"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    socket.connect((hote, port))
except socket :
    print
    "La connexion a echouee!"
    sys.exit()

print
"Connection on {}".format(port)

msgServeur = socket.recv(1024).decode()

ans = True
while ans :
    print(msgServeur)
    ans = input()
    if ans == "1" :
        msgClient = "1"
        socket.send(msgClient.encode())
        msgServeur = socket.recv(1024).decode()
        msgs = msgServeur.split("->->")
        a = input(msgs[0])
        b = input(msgs[1])
        msgClient = a + "->->" + b
        socket.send(msgClient.encode())
        msgServeur = socket.recv(1024).decode()
        msgs = msgServeur.split("->->")
        if (msgs[0] == "3") :
            print("Authentification reussie!\n")
            ans1 = True
            while ans1 :
                print(msgs[1])
                rep = input()
                if rep == "1" :
                    socket.send(rep.encode())
                    socket.send(str(a).encode())
                    msgServeur = socket.recv(1024).decode()
                    msgClient = input(msgServeur)
                    socket.send(msgClient.encode())
                    msgServeur = socket.recv(1024).decode()
                    print(msgServeur)
                elif rep == "2" :
                    socket.send(rep.encode())
                    socket.send(str(a).encode())
                    msgServeur = socket.recv(1024).decode()
                    msgClient = input(msgServeur)
                    socket.send(msgClient.encode())
                    msgServeur = socket.recv(1024).decode()
                    print(msgServeur)
                elif rep == "3" :
                    socket.send(rep.encode())
                    socket.send(str(a).encode())
                    msgServeur = socket.recv(1024).decode()
                    print(msgServeur)
                elif rep == "4" :
                    socket.send(rep.encode())
                    socket.send(str(a).encode())
                    msgServeur = socket.recv(1024).decode()
                    print(msgServeur)
                elif rep == "5" :
                    print("Deconnecté!")
                    socket.send(rep.encode())
                    msgServeur = socket.recv(1024).decode()
                    ans1 = False
        else :
            print(msgs[1])

    elif ans == "2" :
        msgClient = "2"
        socket.send(msgClient.encode())
        msgServeur = socket.recv(1024).decode()
        msgs = msgServeur.split("->->")
        a = input(msgs[0])
        b = input(msgs[1])
        msgClient = a + "->->" + b
        socket.send(msgClient.encode())
        msgServeur = socket.recv(1024).decode()

    elif ans == "3" :
        print ("Close")
        socket.close()
        del ans
        break
    elif ans != "" :
        print ("\n choix invalide")

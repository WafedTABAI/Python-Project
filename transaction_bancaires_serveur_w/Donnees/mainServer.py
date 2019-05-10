#!/usr/bin/env python
# coding: utf-8
import socket

from threading import Thread
from Donnees.ClientConnect import ClientConnect

class mainServer(Thread):
    def __init__(self,M_Comptes,M_Transactions,M_Factures):
        Thread.__init__(self)
        self.M_Comptes = M_Comptes
        self.M_Transactions = M_Transactions
        self.M_Factures= M_Factures

    def run(self):
        hote = "192.168.43.131"
        port = 15555
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.bind((hote, port))
        while 1:
            mySocket.listen(5)
            connexion, adresse = mySocket.accept()
            client = ClientConnect(mySocket,connexion,adresse,self.M_Comptes,self.M_Transactions,self.M_Factures)
            client.setDaemon(True)
            client.start()
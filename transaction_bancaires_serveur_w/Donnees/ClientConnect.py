import socket

from threading import Thread
from Donnees.Transactions import Transactions
from Donnees.Comptes import *
from Donnees.Factures import Factures
from Donnees.Transaction import Transaction
from Donnees.Facture import Facture

class ClientConnect(Thread):
    def __init__(self,mySocket,connexion,adresse,M_Comptes,M_Transactions,M_Factures):
        Thread.__init__(self)
        self.mySocket = mySocket
        self.connexion = connexion
        self.adresse = adresse
        self.M_Comptes = M_Comptes
        self.M_Transactions = M_Transactions
        self.M_Factures = M_Factures

    def run(self):



        authentification = """Bienvenue
                    1.S'authentifier
                    2.Creer un compte
                    3.Quitter
                    

                    Donnez votre choix:
          
                    """
        self.connexion.send(bytes(authentification.encode('utf-8')))
        msgClient = self.connexion.recv(1024).decode()
        ans=True
        while ans:

            if msgClient == "1":
                msgServeur = "Donnez la reference du compte:->->Donnez le mot de passe du compte:"
                self.connexion.send(msgServeur.encode())
                msgClient = self.connexion.recv(1024).decode()
                msgs = msgClient.split("->->")
                refCompte =msgs[0]
                mdp = msgs[1]
                comptes = Comptes()
                self.M_Comptes.acquire()
                comptes.read_object("comptes.txt")
                self.M_Comptes.release()
                if (comptes.isExist(refCompte) == True):
                    if(comptes.CompteLigne(refCompte).mdp==mdp):
                        menu =  "3->->\n"\
                                "\n Menu : " \
                                "\n 1.Retirer\n " \
                                "2.Ajouter\n " \
                                "3.Consulter les transactions \n " \
                                "4.Consulter les factures \n " \
                                "5.Se deconnecter " \
                                "\n Donnez votre choix: "

                        self.connexion.send(menu.encode())
                        msgClient = self.connexion.recv(1024).decode()

                        ans1 = True
                        while ans1:
                            if msgClient == "1":
                                ref = self.connexion.recv(1024).decode()
                                msgServeur="Donnez la somme a retirer: \n"
                                self.connexion.send(msgServeur.encode())
                                msgClient = self.connexion.recv(1024).decode()


                                trans = Transactions()
                                factures = Factures()

                                self.M_Comptes.acquire()
                                self.M_Transactions.acquire()
                                self.M_Factures.acquire()
                                factures.read_object("facture.txt")
                                trans.read_object("histo.txt")

                                tr = Transaction(int(ref), "retrait", msgClient,"", "")

                                tr = trans.VerifierTransaction(tr)

                                if (tr.etat == "negatif"):

                                    fact = Facture(int(ref), (0.2 * int(tr.valeur)))

                                    factures.ajouterFact(fact)

                                    del fact

                                trans.ajouterTrans(tr)

                                msgServeur=tr.resultat

                                self.connexion.send(msgServeur.encode())


                                factures.save_object("facture.txt")
                                trans.save_object("histo.txt")
                                self.M_Factures.release()
                                self.M_Transactions.release()
                                self.M_Comptes.release()



                                del trans

                                del factures
                            elif msgClient == "2":
                                ref = self.connexion.recv(1024).decode()
                                msgServeur = "Donnez la somme a ajouter: \n"
                                self.connexion.send(msgServeur.encode())
                                msgClient = self.connexion.recv(1024).decode()

                                trans = Transactions()


                                self.M_Comptes.acquire()
                                self.M_Transactions.acquire()


                                trans.read_object("histo.txt")

                                tr = Transaction(int(ref), "ajout", msgClient, "", "")

                                tr = trans.VerifierTransaction(tr)



                                trans.ajouterTrans(tr)

                                msgServeur = tr.resultat

                                self.connexion.send(msgServeur.encode())


                                trans.save_object("histo.txt")

                                self.M_Transactions.release()
                                self.M_Comptes.release()

                                del trans


                            elif msgClient == "3":
                                msgClient = self.connexion.recv(1024).decode()
                                trans = Transactions()
                                self.M_Transactions.acquire()
                                trans.read_object("histo.txt")
                                msgServeur = trans.AfficherListTransactionClient(msgClient)
                                self.M_Transactions.release()
                                self.connexion.send(msgServeur.encode())
                                del trans
                                msgClient = self.connexion.recv(1024).decode()
                            elif msgClient == "4":


                                msgClient = self.connexion.recv(1024).decode()
                                fact = Factures()
                                self.M_Factures.acquire()
                                fact.read_object("facture.txt")
                                msgServeur=fact.AfficherListFactureClient(msgClient)
                                self.M_Factures.release()
                                self.connexion.send(msgServeur.encode())
                                del fact
                                msgClient = self.connexion.recv(1024).decode()
                            elif msgClient == "5":
                                f = authentification
                                self.connexion.send(f.encode())
                                msgClient = self.connexion.recv(1024).decode()
                                ans1= False
                                break




                    else:

                        f ="1->->\nMot de passe incorrecte!\n" + authentification
                        self.connexion.send(f.encode())





                else:
                    f="2->->\nReference inexistante!\n"+authentification
                    self.connexion.send(f.encode())




            elif msgClient == "2":
                msgServeur = "Donnez la reference du compte:->->Donnez le mot de passe du compte:"
                self.connexion.send(msgServeur.encode())
                msgClient = self.connexion.recv(1024).decode()
                msgs = msgClient.split("->->")
                refCte = msgs[0]
                mdpp = msgs[1]
                cpt = Compte(int(refCte),0,"positif",0,mdpp)
                comptes = Comptes()
                self.M_Comptes.acquire()
                comptes.read_object("comptes.txt")
                comptes.ajouterCompte(cpt)
                comptes.save_object("comptes.txt")
                self.M_Comptes.release()
                f = "1->->\nCompte crée avec succes!\n" + authentification
                self.connexion.send(f.encode())




            elif msgClient == "3":
                print("\nAu revoir!")
                ans=False

            msgClient = self.connexion.recv(1024).decode()









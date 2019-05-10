from Donnees.Transactions import Transactions
from Donnees.Comptes import *
from Donnees.Factures import Factures
import threading
class mainManag(threading.Thread):
    def __init__(self,mutexComptes,mutexTransactions,mutexFactures):
        threading.Thread.__init__(self)
        self.mutexComptes = mutexComptes
        self.mutexTransactions = mutexTransactions
        self.mutexFactures = mutexFactures

    def run(self):
        ans=True
        while ans:
            print ("""Menu:
            1.Afficher tous les comptes
            2.Consulter un compte
            3.Consulter les factures d'un compte
            4.Consulter les transactions d'un compte
            5.Modifier plafond compte
            6.Quitter
            """)
            ans=input("donner votre choix : ")
            if ans=="1":
                comptes = Comptes()
                self.mutexComptes.acquire()
                comptes.read_object("comptes.txt")
                comptes.Affichertout()
                self.mutexComptes.release()
                del comptes
            elif ans=="2":
                comptes = Comptes()
                self.mutexComptes.acquire()
                comptes.read_object("comptes.txt")
                a = input("Donnez la reference du compte: ")
                if(comptes.isExist(a) == True):
                    comptes.CompteLigne(a).afficherLigneCompte()
                else:
                    print("Reference inexistante!")

                comptes.save_object("comptes.txt")
                self.mutexComptes.release()
                del comptes




            elif ans=="3":
                comptes = Comptes()
                fact = Factures()
                self.mutexComptes.acquire()
                self.mutexFactures.acquire()
                comptes.read_object("comptes.txt")
                fact.read_object("facture.txt")
                a = input("Donnez la reference du compte dont vous-voulez afficher les factures: ")
                if (comptes.isExist(a) == True):
                    print(fact.AfficherListFactureClient(a))
                else:
                    print("Reference inexistante!")
                self.mutexFactures.release()
                self.mutexComptes.release()
                del fact
                del comptes
            elif ans=="4":
                comptes = Comptes()
                trans = Transactions()
                self.mutexComptes.acquire()
                self.mutexTransactions.acquire()
                comptes.read_object("comptes.txt")
                trans.read_object("histo.txt")
                a = input("Donnez la reference du compte dont vous-voulez afficher les transactions: ")
                if (comptes.isExist(a) == True):
                    print(trans.AfficherListTransactionClient(a))

                else:
                    print("Reference inexistante!")
                self.mutexTransactions.release()
                self.mutexComptes.release()
                del trans
                del comptes

            elif ans == "5":
                comptes = Comptes()
                self.mutexComptes.acquire()
                comptes.read_object("comptes.txt")
                y = input("Donnez la reference du compte dont vous-voulez changer le plafond: ")
                if (comptes.isExist(y) == True):
                    u = input("Donnez la valeur du plafond a fixer: ")
                    comptes.ModifierPlafond(y,u)
                    print("Plafond modifie avec succes!")
                    comptes.save_object("comptes.txt")
                else:
                    print("Reference inexistante!")
                self.mutexComptes.release()
                del comptes



            elif ans == "6":
                print("Au revoir!")
                ans = False

            elif ans !="":
                print("\n Choix non-valide!")

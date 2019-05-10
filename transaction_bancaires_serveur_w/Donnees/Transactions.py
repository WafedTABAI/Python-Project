from Donnees.Transaction import Transaction
from Donnees.Comptes import Comptes

class Transactions(object):
    def __init__(self):
        self.listTransactions = [];

    def ajouterTrans(self,trans):
        self.listTransactions.append(trans);

    def getTrans(self,index):
        return self.listTransactions[index];

    def save_object(self,filename):
        with open(filename, "w") as f:
            for s in self.listTransactions:
                f.write(str(s) + "\n")

    def read_object(self, filename):
        with open(filename, "r") as f:
            for line in f:
                    lineTrans = line.strip()
                    trs= lineTrans.split("->->")
                    self.listTransactions.append(Transaction(trs[0],trs[1],trs[2],trs[3],trs[4]))

    def AfficherTrans(self):
        for i in self.listTransactions:
            i.afficherTransaction()

    def AfficherTout(self):
        self.read_object("histo.txt")
        self.AfficherTransaction()

    def VerifierTransaction(self,ligneTrans):
        comptes = Comptes()
        comptes.read_object("comptes.txt")
        p = comptes.CompteLigne(ligneTrans.refCpt)
        if(ligneTrans.transaction=="retrait"):

            if (p.etat =="negatif"):

                if(int(p.valeur)+int(ligneTrans.valeur)>int(p.plafond)):
                    ligneTrans.resultat = "echec"
                    ligneTrans.etat = "negatif"
                else:
                    ligneTrans.resultat = "succes"
                    ligneTrans.etat = "negatif"
                    comptes.ModifierLigneCompte2(ligneTrans.refCpt, ligneTrans.valeur)
                    comptes.save_object("comptes.txt")

            elif (p.etat=="positif"):

                if ( int(ligneTrans.valeur )> int(p.plafond)):
                    ligneTrans.resultat = "echec"
                    ligneTrans.etat ="positif"
                else:
                    ligneTrans.resultat = "succes"
                    comptes.ModifierLigneCompte1(ligneTrans.refCpt,ligneTrans.valeur)
                    p1 = comptes.CompteLigne(ligneTrans.refCpt)
                    ligneTrans.etat = p1.etat
                    comptes.save_object("comptes.txt")



        else:
            if (p.etat =="negatif"):
                ligneTrans.resultat = "succes"
                comptes.ModifierLigneCompte1(ligneTrans.refCpt, ligneTrans.valeur)
                p1 = comptes.CompteLigne(ligneTrans.refCpt)
                ligneTrans.etat = p1.etat
                comptes.save_object("comptes.txt")


            elif (p.etat=="positif"):
                if ( int(ligneTrans.valeur )> int(p.plafond)):
                    ligneTrans.resultat = "echec"
                    ligneTrans.etat ="positif"
                else:
                    ligneTrans.resultat = "succes"
                    comptes.ModifierLigneCompte2(ligneTrans.refCpt,ligneTrans.valeur)
                    ligneTrans.etat = "positif"
                    comptes.save_object("comptes.txt")

        return ligneTrans




    def AfficherListTransactionClient(self,refCpt):
        nb=0
        s = "La liste des transactions du compte numero: " + str(refCpt)
        for i in self.listTransactions:
            if (str(i.refCpt) == str(refCpt)):
                nb+=1
                s += "\n" + "{}      {}      {}      {}      {}".format(i.refCpt, i.transaction, i.valeur, i.resultat, i.etat)
        if(nb==0):
            print("Aucune transaction effectuee!")
        else:
            return s


    def isExist(self,refCpt):
        for i in self.listLigne:
            if (str(i.refCpt) == str(refCpt)):
                return True

        return False
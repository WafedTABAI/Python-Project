from Donnees.Facture import Facture

class Factures(object):
    def __init__(self):
        self.listFactures = [];

    def ajouterFact(self,fact):
        self.listFactures.append(fact);

    def getFact(self,index):
        return self.listFactures[index];

    def save_object(self,filename):
        with open(filename, "w") as f:
            for s in self.listFactures:
                f.write(str(s) + "\n")
    def read_object(self, filename):
        with open(filename, "r") as f:
            for line in f:
                    lineFact = line.strip()
                    fct = lineFact.split("->->")
                    self.listFactures.append(Facture(fct[0], fct[1]))


    def AfficherFact(self):
        for i in self.listFactures:
            i.afficherFacture()

    def AfficherTout(self):
        self.read_object("facture.txt")
        self.AfficherFact()

    def AfficherListFactureClient(self,refCpt):
        s = "La liste des factures pour les retraits durant les etat 'negatif' avec un TI=2% pour le compte: " + str(refCpt)
        somme = 0
        for i in self.listFactures:
            if (str(i.refCpt) == str(refCpt)):
                somme += float(i.somme)
                s += "\n" + "{}      {}".format(i.refCpt, i.somme)
            """s*=0.2"""
        s += "\n" + "Le Total a payer: " + str(somme)
        return s

    def isExist(self, refCpt):
        for i in self.listFactures:
            if (str(i.refCpt) == str(refCpt)):
                return True

        return False
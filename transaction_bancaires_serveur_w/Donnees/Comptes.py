from trace import Trace

from Donnees.Compte import Compte


class Comptes(object):
    def __init__(self):
        self.listCpt = [];

    def ajouterCompte(self,compte):
        self.listCpt.append(compte);

    def getCompte(self,index):
        return self.listCpt[index];

    def save_object(self,filename):
        with open(filename, "w") as f:
            for s in self.listCpt:
                f.write(str(s) + "\n")

    def read_object(self, filename):
        with open(filename, "r") as f:
            for line in f:
                lineCpt = line.strip()
                cpt = lineCpt.split("->->")
                self.listCpt.append(Compte(cpt[0],cpt[1],cpt[2],cpt[3],cpt[4]))

    def AfficherComptes(self):
        for i in self.listCpt:
            i.afficherLigneCompte()

    def Affichertout(self):
        self.AfficherComptes(

        )
    def ListeCompteClient(self):
        self.read_object("comptes.txt")
        s = "La Liste Des Comptes : "
        s += "\nrefCpt valeur etat plafond"
        for i in self.listCpt:
            s += "\n" + "{}      {}      {}      {}".format(i.refCpt,i.valeur,i.etat,i.plafond)
        return(s)

    def CompteLigne(self,refCpt):
        for i in self.listCpt:
            if(str(i.refCpt)  == str(refCpt)):
                return i
        return 0

    def ModifierLigneCompte1(self,refCpt,valeur):
        for i in self.listCpt:
            if(str(i.refCpt)  == str(refCpt)):
                val=int(i.valeur)
                val-=int(valeur)
                if(i.etat=="positif"):
                    if(val<0):
                        val=(-val)
                        i.valeur=str(val)
                        i.etat="negatif"
                    else:
                        i.valeur = str(val)
                if (i.etat == "negatif"):
                    if (val < 0):
                        val = (-val)
                        i.valeur = str(val)
                        i.etat = "positif"
                    else:
                        i.valeur = str(val)

                break

    def ModifierLigneCompte2(self,refCpt,valeur):
        for i in self.listCpt:
            if(str(i.refCpt)  == str(refCpt)):
                val=int(i.valeur)
                val+=int(valeur)
                i.valeur=str(val)
                break

    def ModifierPlafond(self, refCpt,plafond):
        for i in self.listCpt:
            if(str(i.refCpt)  == str(refCpt)):
                val=int(plafond)
                i.plafond=str(val)
                break




    def isExist(self,refCpt):
        for i in self.listCpt:
            if(str(i.refCpt)  == str(refCpt)):
                return True
        return False



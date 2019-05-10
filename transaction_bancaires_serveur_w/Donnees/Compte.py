class Compte(object):
    def __init__(self,refCpt,valeur,etat,plafond,mdp):
        self.refCpt = refCpt;
        self.valeur = valeur;
        self.etat = etat;
        self.plafond=plafond;
        self.mdp=mdp;


    def getrefCpt(self):
        return self.refCpt

    def __str__(self):
        test = [str(self.refCpt), str(self.valeur), str(self.etat), str(self.plafond), str(self.mdp)]
        s = '->->'
        return s.join(test)

    def afficherLigneCompte(self):
        print("{}      {}      {}      {}".format(self.refCpt,self.valeur,self.etat,self.plafond))

    def remplirCpt(self):
        self.refCpt = input("Donnez la reference du compte: ")
        self.valeur = input("Donnez la valeur du compte: ")
        self.etat = input("Donnez l'etat du compte: ")
        self.plafond=input("Donnez le plafond du compte:")

    def remplirCptClient(self):
        self.refCpt = input("Donnez la reference du compte: ")
        self.mdp = input("Donnez le mot de passe du compte: ")
        self.etat="Positif"
        self.plafond=0;



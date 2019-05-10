class Transaction(object):
    def __init__(self,refCpt,transaction,valeur,resultat,etat):
        self.refCpt= refCpt;
        self.transaction = transaction;
        self.valeur = valeur;
        self.resultat = resultat;
        self.etat=etat;

    def __str__(self):
        test = [str(self.refCpt), str(self.transaction), str(self.valeur), str(self.resultat),str(self.etat)]
        s = '->->'
        return s.join(test)

    def afficherTransaction(self):
        print("{}      {}      {}      {}      {}".format(self.refCpt,self.transaction,self.valeur,self.resultat,self.etat))
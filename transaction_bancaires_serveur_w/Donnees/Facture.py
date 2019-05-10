class Facture(object):
    def __init__(self,refCpt,somme):
        self.refCpt = refCpt;
        self.somme = somme;


    def __str__(self):
        test = [str(self.refCpt), str(self.somme)]
        s = '->->'
        return s.join(test)

    def afficherFacture(self):
        print("{}      {}".format(self.refCpt, self.somme))
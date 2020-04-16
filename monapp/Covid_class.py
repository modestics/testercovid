class Post():

    def  __init__(self,fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
         cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
         traitement_immunosuppresseur,code_postal):
        self.facteur_pronostique_defavorable=0
        self.fievre=fievre
        self.fievre_temp= fievre_temp
        self.toux =toux
        self.gout =gout
        self.gorge_ou_courbatures = gorge_ou_courbatures
        self.diarrhee =diarrhee
        self.fatigue =fatigue
        self.impossibilite_de_vous_alimenter =impossibilite_de_vous_alimenter
        self.manque_de_souffle = manque_de_souffle
        self.age =age
        self.hypertension =hypertension
        self.diabetique =diabetique
        self.cancer =cancer
        self.maladie_respiratoire =maladie_respiratoire
        self.insuffisance_renale =insuffisance_renale
        self.maladie_chronique_du_foie =maladie_chronique_du_foie
        self.enceinte =enceinte
        self.poids=poids
        self.taille=taille
        self.maladie_diminuer_vos_défenses_immunitaires =maladie_diminuer_vos_défenses_immunitaires
        self.traitement_immunosuppresseur =traitement_immunosuppresseur
        self.code_postal =code_postal
        self.facteur_de_gravite_mineur = 0
        self.facteur_de_gravite_majeur=0

    def fonction_facteur_pronostique_defavorable(self):
        imc=(self.poids/self.taille**2)
        facteurs = [self.age >= 70 , imc >= 30 ,  self.hypertension , self.diabetique , self.cancer , self.insuffisance_renale ,  self.maladie_respiratoire,  self.maladie_chronique_du_foie , self.enceinte , self.maladie_diminuer_vos_défenses_immunitaires , self.traitement_immunosuppresseur ]
        for facteur in facteurs:
            if facteur ==True:
                self.facteur_pronostique_defavorable = self.facteur_pronostique_defavorable + 1



    ###########################################################################
    # Facteurs de gravité mineurs :
    # Fièvre >= 39°C
    # Fièvre < 35,5°C
    ###########################################################################
    ###########################################################################
    #Fatigue : alitement > 50% du temps diurne ,Facteurs de gravité mineurs :
    ##########################################################################

    def fonction_facteur_de_gravite_mineur(self):
        donnees = [self.fievre, self.fievre_temp, self.toux, self.gout, self.gorge_ou_courbatures, self.diarrhee, self.fatigue,
                   self.impossibilite_de_vous_alimenter, self.manque_de_souffle, self.age, self.poids, self.taille, self.hypertension, self.diabetique,
                   self.cancer, self.maladie_respiratoire, self.insuffisance_renale, self.maladie_chronique_du_foie, self.enceinte,
                   self.maladie_diminuer_vos_défenses_immunitaires,
                   self.traitement_immunosuppresseur, self.code_postal]
        for i,valeur in enumerate(donnees):
            if ( (i,valeur)== (0 ,True)):
                if (int(donnees[1]) <= 35.5 or int(donnees[1]) >= 39):
                    self.facteur_de_gravite_mineur = self.facteur_de_gravite_mineur + 1
                    

            elif ((i,valeur)== (6 ,True)):
                self.facteur_de_gravite_mineur = self.facteur_de_gravite_mineur + 1
             
             


    ##############################################################
    # Facteurs de gravité majeurs :

    # Gêne respiratoire
    # Difficultés importantes pour s’alimenter ou boire depuis plus de 24 heures

    ##############################################################

    def fonction_facteur_de_gravite_majeur(self):
        self.facteur_de_gravite_majeur=0
        if self.manque_de_souffle:
            self.facteur_de_gravite_majeur = self.facteur_de_gravite_majeur + 1
        else:
            pass

        if self.impossibilite_de_vous_alimenter:
            self.facteur_de_gravite_majeur =   self.facteur_de_gravite_majeur + 1
        else:
            pass
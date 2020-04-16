"""Ceci est le code qui consiste en un groupe de parametres qui renvoient une reponse . Ici les parametre sont
initialisees par des valeurs pour des besoins d essais en attendant"""

# les valaeurs des parametres que devraient renseigner l usager

{'recevoir_valeurs_fiever': 'True',
 'recevoir_valeurs_toux': 'Truetoux', 
 'recevoir_valeurs_gout': 'True', 
 'recevoir_valeurs_courbatures': 'False',
  'recevoir_valeurs_diarrhee': 'Truediar', 
  'recevoir_valeurs_fatigue': 'True',
   'recevoir_valeurs_fatigue_moitiee_journee': 'True',
    'recevoir_valeurs_impossibilite_de_vous_alimenter': 'Truealim',
     'manque_de_souffle': 'True', 'recevoir_valeurs_age': 'True', 
     'recevoir_valeurs_taille': 'True', 'recevoir_valeurs_poids': 'Truepoids',
      'recevoir_valeurs_hypertension': 'True',
       'recevoir_valeurs_diabetique': 'True',
        'recevoir_valeurs_cancer': 'True', 
        'recevoir_valeurs_maladi_respiratoire': 'Trueresp',
         'recevoir_valeurs_insuffisance_renale': 'Trueins',
          'indeex_maladie_chronique_du_foie': 'Truefoi',
           'recevoir_valeurs_enceinte': 'True',
            'indeex_maladie_diminuer_ummunitaire': 'True',
             'recevoir_valeurs_traitement_immuinosuppresseur': 'Truetrait',
              'E_mail': 'sqKS@SDJSDS.COM', 'Ville': 'ABENGOUROU'}
fievre = False
toux = True
gorge_ou_courbatures = False
manque_de_souffle= False
age = 70


fievre_temp = 40

gout =False
diarrhee = False
fatigue = True
impossibilite_de_vous_alimenter = False
poids = 100
taille= False
hypertension = False
diabetique = False
cancer= False
insuffisance_renale = False
maladie_respiratoire = False
maladie_chronique_du_foie = False
enceinte = False
maladie_diminuer_vos_défenses_immunitaires = False
traitement_immunosuppresseur = False
code_postal = False
maladie_respiratoire =False
imc=40

# la classe qui se charge de manipuler les valeurs

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
        facteurs = [age >= 70 , imc >= 30 ,  hypertension , diabetique , cancer , insuffisance_renale ,  maladie_respiratoire,  maladie_chronique_du_foie , enceinte , maladie_diminuer_vos_défenses_immunitaires , traitement_immunosuppresseur ]
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
                    print(i,valeur)
            elif ((i,valeur)== (6 ,True)):
                self.facteur_de_gravite_mineur = self.facteur_de_gravite_mineur + 1
                print(i, valeur)


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

# le corps du code qui evalue chaque condition ca pourrait etre une autre classe

Post=Post(fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
         cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
         traitement_immunosuppresseur,code_postal)
Post.fonction_facteur_pronostique_defavorable()
Post.fonction_facteur_de_gravite_majeur()
Post.fonction_facteur_de_gravite_mineur()

resultats ="""Aucune reposnse"""
if int(Post.age)<= 15 :
    resultats = """     Prenez contact avec votre médecin généraliste au moindre doute.
Cette application n’est pour l’instant pas adaptée aux personnes de moins de 15 ans.
En cas d’urgence, appeler le 15."""
elif Post.facteur_de_gravite_majeur >=1:
    resultats = """Appelez le 15."""
elif (Post.fievre==True and Post.toux== True):
    if(Post.facteur_pronostique_defavorable==0):
        resultats ="""      Votre situation peut relever d’un COVID 19.
Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""

    elif Post.facteur_pronostique_defavorable >= 1:
        if Post.facteur_de_gravite_mineur ==(1 or 2):
            resultats = """     Votre situation peut relever d’un COVID 19.
    Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""


        elif Post.facteur_de_gravite_mineur >=2:
            resultats = """     Votre situation peut relever d’un COVID 19.
    Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
    Si vous n'arrivez pas à obtenir de consultation, appelez le 15."""
elif Post.fievre or(not Post.fievre and(Post.diarrhee or (Post.toux and Post.gorge_ou_courbatures) or (Post.toux and Post.impossibilite_de_vous_alimenter ))):
    if Post.facteur_pronostique_defavorable==0:
        if Post.facteur_de_gravite_mineur!=0:
            resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
Nous vous conseillons de rester à votre domicile."""
        elif Post.facteur_de_gravite_mineur == 0:

            if Post.age <= 50 :
                resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
    Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
    Nous vous conseillons de rester à votre domicile."""
            elif Post.age > 50:
                resultats = """Votre situation peut relever d’un COVID 19.
Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
        elif  Post.facteur_de_gravite_mineur!=0:
            resultats = """     Votre situation peut relever d’un COVID 19.
Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""

    if Post.facteur_pronostique_defavorable != 0:
        if Post.facteur_de_gravite_mineur <=1:
            resultats = """     Votre situation peut relever d’un COVID 19.
    Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
    Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
        elif Post.facteur_de_gravite_mineur >1:
            resultats = """     Votre situation peut relever d’un COVID 19.
    Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
    Si vous n'arrivez pas à obtenir de consultation, appelez le 15.."""
elif not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter):
    if Post.facteur_pronostique_defavorable >=1:
        resultats = """Votre situation peut relever d’un COVID 19. Un avis médical est recommandé.
Au moindre doute, appelez le 15. Nous vous conseillons de rester à votre domicile."""
    elif Post.facteur_pronostique_defavorable==0:
        resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
Nous vous conseillons de rester à votre domicile."""
elif not (Post.fievre and Post.gout and Post.gorge_ou_courbatures and  Post.diarrhee and Post.fatigue and Post.impossibilite_de_vous_alimenter and Post.manque_de_souffle)== True:
    resultats = """     Votre situation ne relève probablement pas du COVID 19.
N’hésitez pas à contacter votre médecin en cas de doute.
Vous pouvez refaire le test en cas de nouveau symptôme pour réévaluer la situation.
Pour toute information concernant le COVID 19, composer le 0 800 130 000.."""


print("Post.facteur_de_gravite_mineur     {}".format(Post.facteur_de_gravite_mineur))
print("Post.facteur_pronostique_defavorable    {}".format(Post.facteur_pronostique_defavorable))
print("Post.facteur_de_gravite_majeur      {}".format(Post.facteur_de_gravite_majeur))

print("Post.facteur_de_gravite_majeur     \n\n\n {}".format(resultats))
print("Post.facteur_de_gravite_majeur     \n\n\n {}".format(fievre))


"""
fievre = bool(input("Pensez-vous avoir eu de la fièvre ces derniers jours (frissons, sueurs) ? : "))
fievre_temp = (input("Quelle a été votre température la plus élevée ces dernières 48h ? : "))
toux = bool(input("Avez-vous noté une forte diminution de votre goût ou de votre odorat ces derniers jours ? OUI / NON") )
gout = bool(input("Avez-vous noté une forte diminution de votre goût ou de votre odorat ces derniers jours ? OUI / NON") )
gorge_ou_courbatures = bool(input("Avez-vous un mal de gorge ou des douleurs musculaires ou des courbatures inhabituelles ces derniers jours ? OUI / NON"))
diarrhee = bool(input("Avez-vous de la diarrhée ces dernières 24 heures (au moins 3 selles molles) ? OUI / NON"))
fatigue = bool(input("Avez-vous une fatigue inhabituelle ces derniers jours ? OUI / NONSi OUI : Cette fatigue vous oblige-t-elle à vous reposer plus de la moitié de la journée ? OUI / NON"))
impossibilite_de_vous_alimenter = bool(input("Êtes-vous dans l'impossibilité de vous alimenter ou de boire DEPUIS 24 HEURES OU PLUS ? OUI / NON"))
manque_de_souffle= bool(input("Dans les dernières 24 heures, avez-vous noté un manque de souffle INHABITUEL lorsque vous parlez ou faites un petit effort ? OUI / NON"))
age = (input("Quel est votre âge ?"))
poids = bool(input("Quel est votre poids ? "))
taille= bool(input("Quelle est votre taille ?"))
hypertension = bool(input("Avez-vous de l’hypertension artérielle mal équilibrée ? Ou avez-vous une maladie cardiaque ou vasculaire ? Ou prenez-vous un traitement à visée cardiologique ? OUI / NON / Je ne sais pas (OUI)"))
diabetique = bool(input("Êtes-vous diabétique ? OUI / NON") or "True")
cancer= bool(input("Avez-vous ou avez-vous eu un cancer dans les 3 dernières années ? OUI / NON") )
insuffisance_renale = bool(input("Avez-vous une insuffisance rénale chronique dialysée ? OUI / NON" ))
maladie_respiratoire = bool(input("Avez-vous une maladie chronique du foie ? OUI / NON"))
maladie_chronique_du_foie = bool(input("Avez-vous une maladie respiratoire ? Ou êtes-vous suivi par un pneumologue ? OUI / NON"))
enceinte = bool(input("Êtes-vous enceinte ? OUI / NON / Non applicable"))
maladie_diminuer_vos_défenses_immunitaires = bool(input("Avez-vous une maladie connue pour diminuer vos défenses immunitaires OUI / NON / Je ne sais pas (NON)"))
traitement_immunosuppresseur = bool(input("Prenez-vous un traitement immunosuppresseur ? C’est un traitement qui diminue vos défenses contre les infections. Voici quelques exemples : corticoïdes, méthotrexate, ciclosporine, tacrolimus, azathioprine, cyclophosphamide (liste non exhaustive). OUI / NON / Je ne sais pas (NON)"))
code_postal = (input("Quel est votre code postal ?") or "229" )
maladie_respiratoire = bool(input("Avez-vous une maladie respiratoire ? Ou êtes-vous suivi par un pneumologue ? OUI / NON"))

donnees=[fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
         cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
         traitement_immunosuppresseur,code_postal]
#imc =poids/(taille**2)
imc=40

"""



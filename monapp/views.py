from django.shortcuts import render , redirect, HttpResponseRedirect, HttpResponse

from . forms import DonneesUser

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . forms import recevoir_valeurs_code_postal
from . forms import recevoir_valeurs_courbatures
from . forms import recevoir_valeurs_fatigue_moitiee_journee
from . forms import recevoir_valeurs_diabetique
from . forms import recevoir_valeurs_diarrhee
from . forms import recevoir_valeurs_enceinte
from . forms import recevoir_valeurs_fatigue
from . forms import recevoir_valeurs_gout
from . forms import recevoir_valeurs_hypertension
from . forms import recevoir_valeurs_imc
from . forms import recevoir_valeurs_impossibilite_de_vous_alimenter
from . forms import indeex_maladie_chronique_du_foie
from . forms import recevoir_valeurs_insuffisance_renale
from . forms import recevoir_valeurs_maladi_respiratoire

from . forms import recevoir_valeurs_poids
from . forms import recevoir_valeurs_temperature
from . forms import recevoir_valeurs_toux
from . forms import recevoir_valeurs_traitement_immuinosuppresseur
from . forms import recevoir_valeurs_fatigue_moitiee_journee
from . forms import recevoir_valeurs_age
from . forms import recevoir_valeurs_cancer
from . forms import indeex_maladie_diminuer_ummunitaire
from . forms import recevoir_valeurs_diabetiquee
from . forms import resultat
from . forms import recevoir_valeurs_fiever
from . forms import manque_de_souffle
from . forms import recevoir_valeurs_taille
from . forms import choix_du_pays
from . Covid_class import Post as Posta

import ast

#from . import Covid_class

class ChoixDePays: 
    CHOIX={'Benin':'95 36 11 07, ou 51 02 00 00, ou 51 04 00 00 | Numéro vert CDC  - 95 36 1104 or 95 36 11 02 partout au Bénin',
    'Burkina Faso ':'35 35 | Numéro vert CDC - 61 63 63 99 ou 52 19 53 94 partout au Burkina Faso ',
    'Cameroun ':'1510 | Numéro vert CDC - 677 899 369 ou 677 894 364 ou 677 897 644 ou 677 900 157 partout au Cameroun',
    'Cap_Vert':'800 11 12 partout au Cap Vert',
    'Republique_Centrafricaine':'1212 | Numéro vert CDC - 72 28 71 53 ou 75 23 33 90 partout en République Centrafricaine',
    'Republique_du_Congo ':'1414  ou 1400 partout au Congo',
    'Republique_Democratique_du_Congo':' Numéro vert CDC - 854 463 582 ou 841 363 267 partout en RDC',
    'Cote_d_Ivoire':'144 ou 143 ou 101 ou envoyez << CORONA >> au 1366 partout en Cote d Ivoire',
    'Guinee_Bissau':'1919 (MTN) ou 2020 (Orange) ou 966 050 002 (COES) partout en Guinee Bissau',
    'Guinee_Equatoriale':'1111 partout en  Guinée Equatoriale',
    'Gabon':'1410 partout  au Gabon','Gambie':'1025 partout  en Gambie','Ghana':'Numéro vert CDC - 509 497 700 ou 552 222 004 ou 552 222 005 ou 558 439 868 partout au Ghana',
    'Guinee':'Numéro vert CDC - 629 995 656 partout en Guinée',
    'Liberia':'4455 partout au Libéria ',
    'Mali':'36061 partout au Mali',
    'Mauritanie':'1155 partout en Mauritanie',
    'Niger':'15 partout au Niger',
    'Nigeria':'Numéro vert CDC - 800 9700 0010 partout  au Nigeria',
    'Senegal':'1515 | Numéro vert CDC - 800 00 50 50 partout  au Senegal',
    'Sierra_Leone':'117  partout  en Sierra Leone',
    'Tchad':'1313 partout  au Tchad','Togo':'Numéro vert CDC - 22 222 073 ou 91 674 242 au partout Togo'}


Donnees= {}

class Yes2Truee:
    def Yes2True(self,val):
        if val=='Yes':
            val=True
        elif val =='No':
            val=False
        return val


class DonneesDuProblem():
    def index(request):
        form_temp=recevoir_valeurs_fiever()
        form_toux=recevoir_valeurs_toux()
        form_gout =  recevoir_valeurs_gout()
        form_gorge=recevoir_valeurs_courbatures()
        form_diarrhee = recevoir_valeurs_diarrhee()
        form_fatigue =  recevoir_valeurs_fatigue()
        form_fatigue_mo = recevoir_valeurs_fatigue_moitiee_journee()   
        form_alimenter =  recevoir_valeurs_impossibilite_de_vous_alimenter()
        form_souffle =  manque_de_souffle()
        form_age = recevoir_valeurs_age()    
        form_taille =  recevoir_valeurs_taille()
        form_poids =  recevoir_valeurs_poids()
        form_hypertension =  recevoir_valeurs_hypertension()
        form_diabetique =  recevoir_valeurs_diabetique()
        form_cancer = recevoir_valeurs_cancer()  
        form_respiratoire = recevoir_valeurs_maladi_respiratoire()
        form_renale =  recevoir_valeurs_insuffisance_renale() 
        form_foie = indeex_maladie_chronique_du_foie()  
        form_enceinte =  recevoir_valeurs_enceinte() 
        form_ummunitaire = indeex_maladie_diminuer_ummunitaire()  
        form_immuinosuppresseur =  recevoir_valeurs_traitement_immuinosuppresseur()    
        form_code_postal = recevoir_valeurs_code_postal()
        form_choix_du_pays=choix_du_pays()  

        return render(request,'index.html',{'form_temp':form_temp,'form_toux':form_toux,'form_gout':form_gout,'form_gorge':form_gorge,
            'form_diarrhee':form_diarrhee,'form_fatigue':form_fatigue,'form_fatigue_mo':form_fatigue_mo,'form_alimenter':form_alimenter,
            'form_souffle':form_souffle,'form_age':form_age,'form_taille':form_taille,
            'form_poids':form_poids,'form_hypertension':form_hypertension,'form_diabetique':form_diabetique,
            'form_cancer':form_cancer,'form_respiratoire':form_respiratoire,'form_renale':form_renale,
           'form_foie':form_foie,'form_enceinte':form_enceinte,'form_ummunitaire':form_ummunitaire,
           'form_immuinosuppresseur':form_immuinosuppresseur,'form_code_postal':form_code_postal,'form_choix_du_pays':form_choix_du_pays} )

    


    
    def handler500(request):
        return render(request, 'index.html', status=500)


    def Reprendre(request):



        return redirect('https://testercovid.herokuapp.com/')



    def recevoir_index(request):





        form_age = recevoir_valeurs_age(request.POST)    
        form_taille =  recevoir_valeurs_taille(request.POST)
        form_poids =  recevoir_valeurs_poids(request.POST)
        form_temp=recevoir_valeurs_fiever(request.POST)

        if request.method=='POST':
            toux=request.POST['question_2'] 
            fievre=request.POST['question_f'] #toux
            gout=request.POST['question_3'] #gout
            fatigue=request.POST['question_4'] #gout
            gorge=request.POST['question_5'] #gout
            diarrhee=request.POST['question_6'] #gout
            fatigue_inhabituelle=request.POST['question_7'] #gout
            alimenter=request.POST['question_8'] #gout
            souffle=request.POST['question_9'] #gout
            hypertension=request.POST['question_10'] #gout
            diabetique=request.POST['question_11'] 
            cancer=request.POST['question_12'] 
            respiratoire=request.POST['question_13'] #gout
            renale=request.POST['question_14'] 
            foie=request.POST['question_15'] 
            enceinte=request.POST['question_16'] 
            immunitaires=request.POST['question_17'] 
            immuinosuppresseur=request.POST['question_18']
          
            if form_age.is_valid():
                age=form_age.cleaned_data['age']
                if form_taille.is_valid():
                    taille=form_taille.cleaned_data['taille']
                    if form_poids.is_valid():
                        poids=form_poids.cleaned_data['poids']
                        if form_temp.is_valid():
                            temperature=form_temp.cleaned_data['temp']


           


          

                            return HttpResponse('''<h2> c est OK <h2/>''')

                





    def resultat2( request): 
        if request.method== 'POST':


            Yes=Yes2Truee()


            form_age = recevoir_valeurs_age(request.POST)    
            form_taille =  recevoir_valeurs_taille(request.POST)
            form_poids =  recevoir_valeurs_poids(request.POST)
            form_temp=recevoir_valeurs_fiever(request.POST)
            form_choix_du_pays=choix_du_pays(request.POST)


            if request.method=='POST':
                toux=request.POST['question_2'] #toux
                fievre=request.POST['question_f']
                gout=request.POST['question_3'] #gout
                fatigue=request.POST['question_4'] #gout
                gorge=request.POST['question_5'] #gout
                diarrhee=request.POST['question_6'] #gout
                fatigue_inhabituelle=request.POST['question_7'] #gout
                alimenter=request.POST['question_8'] #gout
                souffle=request.POST['question_9'] #gout
                hypertension=request.POST['question_10'] #gout
                diabetique=request.POST['question_11'] 
                cancer=request.POST['question_12'] 
                respiratoire=request.POST['question_13'] #gout
                renale=request.POST['question_14'] 
                foie=request.POST['question_15'] 
                enceinte=request.POST['question_16'] 
                immunitaires=request.POST['question_17'] 
                immuinosuppresseur=request.POST['question_18']
                temperature=request.POST['temp']
            
                if form_age.is_valid():
                    age=form_age.cleaned_data['age']
                    if form_taille.is_valid():
                        taille=form_taille.cleaned_data['taille']
                        if form_poids.is_valid():
                            poids=form_poids.cleaned_data['poids']
               
                            if form_choix_du_pays.is_valid():
                                    le_choix_du_pays=form_choix_du_pays.cleaned_data['choix_du_pays']



        
            gorge_ou_courbatures = Yes.Yes2True(gorge)
            manque_de_souffle= Yes.Yes2True(souffle)
            age =int(age)
            taille=float(taille)
            poids=int(poids)
            temperature=float(temperature)


            fievre_temp =temperature


            gout = Yes.Yes2True(gout)
            toux = Yes.Yes2True(toux)
            fievre = Yes.Yes2True(fievre)
            diarrhee = Yes.Yes2True(diarrhee)
            fatigue = Yes.Yes2True( fatigue)
            impossibilite_de_vous_alimenter =Yes.Yes2True(alimenter)
            poids = (poids)
            taille=taille
            hypertension =Yes.Yes2True(hypertension)
            diabetique = Yes.Yes2True(diabetique)
            cancer=Yes.Yes2True( cancer)
            insuffisance_renale =Yes.Yes2True( renale)
            maladie_respiratoire = Yes.Yes2True(respiratoire)
            maladie_chronique_du_foie =Yes.Yes2True( foie)
            enceinte =Yes.Yes2True(enceinte)
            maladie_diminuer_vos_défenses_immunitaires = Yes.Yes2True( immunitaires)
            recevoir_valeurs_traitement_immuinosuppresseurent_immunosuppresseur = Yes.Yes2True(immuinosuppresseur)
            code_postal=229
            
            imc=poids/taille**2
            imc=int(imc)

            





            Post=Posta(fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
                     cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
                     recevoir_valeurs_traitement_immuinosuppresseurent_immunosuppresseur,code_postal)
            Post.fonction_facteur_pronostique_defavorable()
            Post.fonction_facteur_de_gravite_majeur()
            Post.fonction_facteur_de_gravite_mineur()

            facteur_pronostique_defavorable=Post.facteur_pronostique_defavorable
            facteur_de_gravite_majeur=Post.facteur_de_gravite_majeur
            facteur_de_gravite_mineur=Post.facteur_de_gravite_mineur


            num_de_pays=ChoixDePays()
            CHOIX_DE_PAYS=num_de_pays.CHOIX[le_choix_du_pays]

            if imc<=18.5 :
                imc_message= f""" vous etes donc en sous poids il est normal pour une valeur comprise entre 18.5 et 24.9 """
            elif (18.5 <= imc) and (imc<=24.9):
                imc_message= f""" votre poids est donc  normal par rapport à votre taille ,il est normal pour une valeur comprise entre 18.5 et 24.9"""
            elif (24.9<= imc) and (imc<=29.9):
                imc_message= f""" vous etes donc en surpoids à moins que vous soyez  pratiquant de la musculation ,il est normal pour une valeur comprise entre 18.5 et 24.9 """
            elif (29.9<= imc) and (imc<=40):
                imc_message= f""" vous souffrez donc d'obésité, il est normal pour une valeur comprise entre 18.5 et 24.9 """
            elif  (imc>=40):
                imc_message= f""" vous souffrez donc d'obésité massive ,il est normal pour une valeur comprise entre 18.5 et 24.9"""



            resultats ="""Aucune reposnse"""
            if int(Post.age)<= 15 :
                resultats = f"""     Prenez contact avec votre médecin généraliste au moindre doute.
            Cette application n’est pour l’instant pas adaptée aux personnes de moins de 15 ans.
            En cas d’urgence, appeler le :{CHOIX_DE_PAYS} """
            elif Post.facteur_de_gravite_majeur >=1:
                resultats = f""" Vous devriez appeler le: {CHOIX_DE_PAYS}  pour une prise en charge"""
            elif (Post.fievre==True and Post.toux== True):
                if(Post.facteur_pronostique_defavorable==0):
                    resultats =f"""    3.  Votre situation peut relever d’un COVID 19.
            Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""

                elif Post.facteur_pronostique_defavorable >= 1:
                    if Post.facteur_de_gravite_mineur ==(1 or 2):
                        resultats = """    Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""


                    elif Post.facteur_de_gravite_mineur >=2:
                        resultats = f"""     Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
                Si vous n'arrivez pas à obtenir de consultation, appelez :{CHOIX_DE_PAYS} """
            elif Post.fievre or(not Post.fievre and(Post.diarrhee or (Post.toux and Post.gorge_ou_courbatures) or (Post.toux and Post.impossibilite_de_vous_alimenter ))):
                if Post.facteur_pronostique_defavorable==0:
                    if Post.facteur_de_gravite_mineur!=0:
                        resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
            Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
            Nous vous conseillons de rester à votre domicile."""
                    elif Post.facteur_de_gravite_mineur == 0:

                        if Post.age <= 50 :
                            resultats = """    Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
                Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
                Nous vous conseillons de rester à votre domicile."""
                        elif Post.age > 50:
                            resultats = f""" Votre situation peut relever d’un COVID 19.
            Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
            Appelez les Numeros d'Urgences :
    {CHOIX_DE_PAYS} si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
                    elif  Post.facteur_de_gravite_mineur!=0:
                        resultats = f"""      Votre situation peut relever d’un COVID 19.
            Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
            Appelez les Numeros d'Urgences :
    {CHOIX_DE_PAYS} si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""

                if Post.facteur_pronostique_defavorable != 0:
                    if Post.facteur_de_gravite_mineur <=1:
                        resultats = f"""    Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
                Appelez les Numeros d'Urgences :
    {CHOIX_DE_PAYS} si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
                    elif Post.facteur_de_gravite_mineur >1:
                        resultats = f"""    Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
                Si vous n'arrivez pas à obtenir de consultation, appelez les Numeros d'Urgences :
    {CHOIX_DE_PAYS} .."""
            elif ( not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter)):
                A=( not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter))
                print(f" not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter){A},Post.fievre  {Post.fievre},Post.toux  {Post.toux}")
                if Post.facteur_pronostique_defavorable >=1:
                    resultats = f"""  Votre situation peut relever d’un COVID 19. Un avis médical est recommandé.
            Au moindre doute, appelez le les Numeros d'Urgences :
    {CHOIX_DE_PAYS} . Nous vous conseillons de rester à votre domicile."""
                elif Post.facteur_pronostique_defavorable==0:
                    resultats = """    Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
            Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
            Nous vous conseillons de rester à votre domicile."""
            elif  (Post.fievre and Post.gout and Post.gorge_ou_courbatures and  Post.diarrhee and Post.fatigue and Post.impossibilite_de_vous_alimenter and Post.manque_de_souffle)== False:
                resultats = f"""   Votre situation ne relève probablement pas du COVID 19.
            N’hésitez pas à contacter votre médecin en cas de doute.
            Vous pouvez refaire le test en cas de nouveau symptôme pour réévaluer la situation.
            Pour toute information concernant le COVID 19, les Numeros d'Urgences :
   {CHOIX_DE_PAYS} .."""





           
     
           
            return render(request,'resultat2.html' ,{'imc_message':imc_message,'resultats': resultats,'imc': imc,'facteur_de_gravite_majeur': facteur_de_gravite_majeur,'facteur_de_gravite_mineur': facteur_de_gravite_mineur,'facteur_pronostique_defavorable': facteur_pronostique_defavorable})

        else :
            return redirect('https://testercovid.herokuapp.com/')






    def resultat3( request): 
        if request.method== 'POST':


            Yes=Yes2Truee()


            form_age = recevoir_valeurs_age(request.POST)    
            form_taille =  recevoir_valeurs_taille(request.POST)
            form_poids =  recevoir_valeurs_poids(request.POST)
            form_temp=recevoir_valeurs_fiever(request.POST)
            form_choix_du_pays=choix_du_pays(request.POST)


            if request.method=='POST':
                toux=request.POST['question_2'] #toux
                fievre=request.POST['question_f']
                gout=request.POST['question_3'] #gout
                fatigue=request.POST['question_4'] #gout
                gorge=request.POST['question_5'] #gout
                diarrhee=request.POST['question_6'] #gout
                fatigue_inhabituelle=request.POST['question_7'] #gout
                alimenter=request.POST['question_8'] #gout
                souffle=request.POST['question_9'] #gout
                hypertension=request.POST['question_10'] #gout
                diabetique=request.POST['question_11'] 
                cancer=request.POST['question_12'] 
                respiratoire=request.POST['question_13'] #gout
                renale=request.POST['question_14'] 
                foie=request.POST['question_15'] 
                enceinte=request.POST['question_16'] 
                immunitaires=request.POST['question_17'] 
                immuinosuppresseur=request.POST['question_18']
   
                if form_age.is_valid():
                    age=form_age.cleaned_data['age']
                    if form_taille.is_valid():
                        taille=form_taille.cleaned_data['taille']
                        if form_poids.is_valid():
                            poids=form_poids.cleaned_data['poids']
                            if form_temp.is_valid():
                                temperature=form_temp.cleaned_data['temp']
                                if form_choix_du_pays.is_valid():
                                    le_choix_du_pays=form_choix_du_pays.cleaned_data['choix_du_pays']



        
            gorge_ou_courbatures = Yes.Yes2True(gorge)
            manque_de_souffle= Yes.Yes2True(souffle)
            age =age


            fievre_temp =temperature


            gout = Yes.Yes2True(gout)
            fievre = Yes.Yes2True(fievre)
            diarrhee = Yes.Yes2True(diarrhee)
            fatigue = Yes.Yes2True( fatigue)
            impossibilite_de_vous_alimenter =Yes.Yes2True(alimenter)
            poids = (poids)
            taille=(taille)
            hypertension =Yes.Yes2True(hypertension)
            diabetique = Yes.Yes2True(diabetique)
            cancer=Yes.Yes2True( cancer)
            insuffisance_renale =Yes.Yes2True( renale)
            maladie_respiratoire = Yes.Yes2True(respiratoire)
            maladie_chronique_du_foie =Yes.Yes2True( foie)
            enceinte =Yes.Yes2True(enceinte)
            maladie_diminuer_vos_défenses_immunitaires = Yes.Yes2True( immunitaires)
            traitement_immunosuppresseur = Yes.         Yes2True(immuinosuppresseur)
            code_postal=229
            
            imc=poids/taille**2

            





            Post=Posta(fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
                     cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
                     traitement_immunosuppresseur,code_postal)
            Post.fonction_facteur_pronostique_defavorable()
            Post.fonction_facteur_de_gravite_majeur()
            Post.fonction_facteur_de_gravite_mineur()
            facteur_pronostique_defavorable=Post.facteur_pronostique_defavorable

            facteur_de_gravite_majeur=Post.facteur_de_gravite_mineur_gravite_majeur
            facteur_de_gravite_mineur=Post.facteur_de_gravite_mineur



            return render(request,'resultat3.html' ,{'imc': imc,'facteur_de_gravite_majeur': facteur_de_gravite_majeur,'facteur_de_gravite_mineur': facteur_de_gravite_mineur,'facteur_pronostique_defavorable': facteur_pronostique_defavorable})

        # else :
        #     return redirect('http://localhost:8000/')
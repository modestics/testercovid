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
from . Covid_class import Post as Posta

import ast

#from . import Covid_class





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

        return render(request,'index.html',{'form_temp':form_temp,'form_toux':form_toux,'form_gout':form_gout,'form_gorge':form_gorge,
            'form_diarrhee':form_diarrhee,'form_fatigue':form_fatigue,'form_fatigue_mo':form_fatigue_mo,'form_alimenter':form_alimenter,
            'form_souffle':form_souffle,'form_age':form_age,'form_taille':form_taille,
            'form_poids':form_poids,'form_hypertension':form_hypertension,'form_diabetique':form_diabetique,
            'form_cancer':form_cancer,'form_respiratoire':form_respiratoire,'form_renale':form_renale,
           'form_foie':form_foie,'form_enceinte':form_enceinte,'form_ummunitaire':form_ummunitaire,
           'form_immuinosuppresseur':form_immuinosuppresseur,'form_code_postal':form_code_postal} )

    


    
    def handler500(request):
        return render(request, 'index.html', status=500)


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
            print(type(form_age))
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
                print(type(form_age))
                if form_age.is_valid():
                    age=form_age.cleaned_data['age']
                    if form_taille.is_valid():
                        taille=form_taille.cleaned_data['taille']
                        if form_poids.is_valid():
                            poids=form_poids.cleaned_data['poids']
                            if form_temp.is_valid():
                                temperature=form_temp.cleaned_data['temp']


        
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
            taille=(taille)/100 
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

            resultats ="""Aucune reposnse"""
            if int(Post.age)<= 15 :
                resultats = """     Prenez contact avec votre médecin généraliste au moindre doute.
            Cette application n’est pour l’instant pas adaptée aux personnes de moins de 15 ans.
            En cas d’urgence, appeler les Numeros d'Urgences :
    101 - 144."""
            elif Post.facteur_de_gravite_majeur >=1:
                resultats = """Vous devriez appeler  les Numeros d'Urgences :
    101 - 144 pour une prise en charge"""
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
                Si vous n'arrivez pas à obtenir de consultation, appelezles Numeros d'Urgences :
    101 - 144."""
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
            Appelez les Numeros d'Urgences :
    101 - 144 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
                    elif  Post.facteur_de_gravite_mineur!=0:
                        resultats = """     Votre situation peut relever d’un COVID 19.
            Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
            Appelez les Numeros d'Urgences :
    101 - 144 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""

                if Post.facteur_pronostique_defavorable != 0:
                    if Post.facteur_de_gravite_mineur <=1:
                        resultats = """     Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
                Appelez les Numeros d'Urgences :
    101 - 144 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
                    elif Post.facteur_de_gravite_mineur >1:
                        resultats = """     Votre situation peut relever d’un COVID 19.
                Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
                Si vous n'arrivez pas à obtenir de consultation, appelez les Numeros d'Urgences :
    101 - 144.."""
            elif not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter):
                if Post.facteur_pronostique_defavorable >=1:
                    resultats = """Votre situation peut relever d’un COVID 19. Un avis médical est recommandé.
            Au moindre doute, appelez le les Numeros d'Urgences :
    101 - 144. Nous vous conseillons de rester à votre domicile."""
                elif Post.facteur_pronostique_defavorable==0:
                    resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
            Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
            Nous vous conseillons de rester à votre domicile."""
            elif not (Post.fievre and Post.gout and Post.gorge_ou_courbatures and  Post.diarrhee and Post.fatigue and Post.impossibilite_de_vous_alimenter and Post.manque_de_souffle)== True:
                resultats = """     Votre situation ne relève probablement pas du COVID 19.
            N’hésitez pas à contacter votre médecin en cas de doute.
            Vous pouvez refaire le test en cas de nouveau symptôme pour réévaluer la situation.
            Pour toute information concernant le COVID 19, les Numeros d'Urgences :
    101 - 144.."""





           
     
           
            return render(request,'resultat2.html' ,{'resultats': resultats})

        else :
            return redirect('http://localhost:8000/')







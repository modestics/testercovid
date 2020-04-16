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



 

    def recevoir_valeurs_fiever(request):
        form=recevoir_valeurs_fiever()

        return render(request,'indeex.html',{'form': form } )





    def accueil(request):
        if request.method == 'POST':
            return redirect('/demarrertest/')



        #je_demarre_le_test


        return render(request,'accueil.html' )



    def je_demarre_le_test(request):
        if request.method == 'POST':
            return redirect('/recevoir_valeurs_fiever/')

       

        return render(request,'je_demarre_le_test.html' )

        






    def indeex_maladie_chronique_du_foie(request):

        if request.method=='POST':
            form =  recevoir_valeurs_insuffisance_renale(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_insuffisance_renale']=Reponse
                Donnees['recevoir_valeurs_insuffisance_renale']=ast.literal_eval(Donnees['recevoir_valeurs_insuffisance_renale'])
                form = indeex_maladie_chronique_du_foie()         
        return render(request,'indeex_maladie_chronique_du_foie.html' ,{'form': form})



    def recevoir_valeurs_fatigue_moitiee_journee(request):

        if request.method=='POST':
            form =  recevoir_valeurs_fatigue(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_fatigue']=Reponse
                Donnees['recevoir_valeurs_fatigue']=ast.literal_eval(Donnees['recevoir_valeurs_fatigue'])
                form = recevoir_valeurs_fatigue_moitiee_journee()         
        return render(request,'indeex_fatigue_moitiee_journee.html' ,{'form': form})



    def recevoir_valeurs_age(request):
        if request.method=='POST':
            form =  manque_de_souffle(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['manque_de_souffle']=Reponse
                Donnees['manque_de_souffle']=ast.literal_eval(Donnees['manque_de_souffle'])
                form = recevoir_valeurs_age()         
        return render(request,'indeex_age.html' ,{'form': form})


    def recevoir_valeurs_cancer(request):
        if request.method=='POST':
            form =  recevoir_valeurs_diabetique(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_diabetique']=Reponse
                Donnees['recevoir_valeurs_diabetique']=ast.literal_eval(Donnees['recevoir_valeurs_diabetique'])
                form = recevoir_valeurs_cancer()         
        return render(request,'indeex_cancer.html' ,{'form': form})


    def recevoir_valeurs_code_postal(request):
        if request.method=='POST':
            form =  recevoir_valeurs_traitement_immuinosuppresseur(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_traitement_immuinosuppresseur']=Reponse
                Donnees['recevoir_valeurs_traitement_immuinosuppresseur']=ast.literal_eval(Donnees['recevoir_valeurs_traitement_immuinosuppresseur'])
                form = recevoir_valeurs_code_postal()         
                
        return render(request,'indeex_code_postal.html' ,{'form': form})

    def indeex_maladie_diminuer_ummunitaire(request):
        if request.method=='POST':
            form =  recevoir_valeurs_enceinte(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_enceinte']=Reponse
                Donnees['recevoir_valeurs_enceinte']=ast.literal_eval(Donnees['recevoir_valeurs_enceinte'])
                form = indeex_maladie_diminuer_ummunitaire()         
                
        return render(request,'indeex_maladie_diminuer_ummunitaire.html' ,{'form': form,'Reponse': Reponse})



    def recevoir_valeurs_courbatures(request):
        if request.method=='POST':
            form =  recevoir_valeurs_gout(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_gout']=Reponse
                Donnees['recevoir_valeurs_gout']=ast.literal_eval(Donnees['recevoir_valeurs_gout'])
                form = recevoir_valeurs_courbatures()         
        return render(request,'indeex_courbatures.html' ,{'form': form,'Reponse': Reponse})

    def recevoir_valeurs_diabetique(request):
        if request.method=='POST':
            form =  recevoir_valeurs_hypertension(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_hypertension']=Reponse
                Donnees['recevoir_valeurs_hypertension']=ast.literal_eval(Donnees['recevoir_valeurs_hypertension'])
                form = recevoir_valeurs_diabetique()         
                
                return render(request,'indeex_diabetique.html' ,{'form': form,'Reponse': Reponse})

    def recevoir_valeurs_diarrhee(request):
        if request.method=='POST':
            form =  recevoir_valeurs_courbatures(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_courbatures']=Reponse
                Donnees['recevoir_valeurs_courbatures']=ast.literal_eval(Donnees['recevoir_valeurs_courbatures'])
                form = recevoir_valeurs_diarrhee()         
        return render(request,'indeex_diarhee.html' ,{'form': form})




    def recevoir_valeurs_enceinte(request):
        if request.method=='POST':
            form =  indeex_maladie_chronique_du_foie(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['indeex_maladie_chronique_du_foie']=Reponse
                Donnees['indeex_maladie_chronique_du_foie']=ast.literal_eval(Donnees['indeex_maladie_chronique_du_foie'])
                form = recevoir_valeurs_enceinte()         
        return render(request,'indeex_enceinte.html' ,{'form': form})



    def recevoir_valeurs_fatigue(request):
        if request.method=='POST':
            form =  recevoir_valeurs_diarrhee(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_diarrhee']=Reponse
                Donnees['recevoir_valeurs_diarrhee']=ast.literal_eval(Donnees['recevoir_valeurs_diarrhee'])
                form = recevoir_valeurs_fatigue()         
        return render(request,'indeex_fatigue.html' ,{'form': form})



    def recevoir_valeurs_gout(request):
        if request.method=='POST':
            form =  recevoir_valeurs_toux(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_toux']=Reponse
                Donnees['recevoir_valeurs_toux']=ast.literal_eval(Donnees['recevoir_valeurs_toux'])
    
                form = recevoir_valeurs_gout()         
        return render(request,'indeex_gout.html' ,{'form': form})




    def manque_de_souffle(request):
        
        if request.method=='POST':
            form =  recevoir_valeurs_impossibilite_de_vous_alimenter(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_impossibilite_de_vous_alimenter']=Reponse
                Donnees['recevoir_valeurs_impossibilite_de_vous_alimenter']=ast.literal_eval(Donnees['recevoir_valeurs_impossibilite_de_vous_alimenter'])
                form = manque_de_souffle()         
        return render(request,'manque_de_souffle.html' ,{'form': form})


    def recevoir_valeurs_hypertension(request):
        
        if request.method=='POST':
            form =  recevoir_valeurs_poids(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_poids']=Reponse

                form = recevoir_valeurs_hypertension()         
        return render(request,'indeex_hypertension.html' ,{'form': form})

    def recevoir_valeurs_imc(request):
        if request.method=='POST':
            form =  recevoir_valeurs_fiever(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_fiever']=Reponse
                Donnees['recevoir_valeurs_fiever']=ast.literal_eval(Donnees['recevoir_valeurs_fiever'])
                form = recevoir_valeurs_toux()         
        return render(request,'indeex_toux.html' ,{'form': form})            
        return render(request,'indeex_imc.html' ,{'form': form,'Reponse': Reponse})

    def recevoir_valeurs_impossibilite_de_vous_alimenter(request):
        if request.method=='POST':
            form =  recevoir_valeurs_fatigue_moitiee_journee(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_fatigue_moitiee_journee']=Reponse
                Donnees['recevoir_valeurs_fatigue_moitiee_journee']=ast.literal_eval(Donnees['recevoir_valeurs_fatigue_moitiee_journee'])
                form = recevoir_valeurs_impossibilite_de_vous_alimenter()           
                
        return render(request,'indeex_impossibilite_de_vous_alimenter.html' ,{'form': form})





    def recevoir_valeurs_maladi_respiratoire(request):
        if request.method=='POST':
            form =  recevoir_valeurs_cancer(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_cancer']=Reponse
                Donnees['recevoir_valeurs_cancer']=ast.literal_eval(Donnees['recevoir_valeurs_cancer'])
                form = recevoir_valeurs_maladi_respiratoire()        
                
        return render(request,'indeex_maladi_respiratoire.html' ,{'form': form})

    def recevoir_valeurs_insuffisance_renale(request):
        if request.method=='POST':
            form =  recevoir_valeurs_maladi_respiratoire(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_maladi_respiratoire']=Reponse
                Donnees['recevoir_valeurs_maladi_respiratoire']=ast.literal_eval(Donnees['recevoir_valeurs_maladi_respiratoire'])
                form = recevoir_valeurs_insuffisance_renale()         
                
        return render(request,'indeex_insuffisance_renale.html' ,{'form': form})







    def recevoir_valeurs_poids(request):
        if request.method=='POST':
            form =  recevoir_valeurs_taille(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_taille']=Reponse

                form = recevoir_valeurs_poids()         
                
        return render(request,'indeex_poids.html' ,{'form': form,'Reponse': Reponse})


    def recevoir_valeurs_taille(request):

        if request.method=='POST':
            form =  recevoir_valeurs_age(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_age']=Reponse

                form = recevoir_valeurs_taille()         
                
        return render(request,'indeex_taille.html' ,{'form': form,'Reponse': Reponse})

    def recevoir_valeurs_temperature(request):
        if request.method=='POST':
            form =  recevoir_valeurs_fiever(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_fiever']=Reponse
                Donnees['recevoir_valeurs_fiever']=ast.literal_eval(Donnees['recevoir_valeurs_fiever'])
                form = recevoir_valeurs_toux()         
        return render(request,'indeex_toux.html' ,{'form': form})
                
        return render(request,'indeex_temperature.html' ,{'form': form})#,'Reponse': Reponse})


    def recevoir_valeurs_toux(request):
       
        if request.method=='POST':
            form =  recevoir_valeurs_fiever(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['recevoir_valeurs_fiever']=Reponse
                Donnees['recevoir_valeurs_fiever']=ast.literal_eval(Donnees['recevoir_valeurs_fiever'])
                form = recevoir_valeurs_toux()  



        return render(request,'indeex_toux.html' ,{'form': form})


    def recevoir_valeurs_traitement_immuinosuppresseur(request):
        if request.method=='POST':
            form = indeex_maladie_diminuer_ummunitaire(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['Reponse']
                Donnees['indeex_maladie_diminuer_ummunitaire']=Reponse
                Donnees['indeex_maladie_diminuer_ummunitaire']=ast.literal_eval(Donnees['indeex_maladie_diminuer_ummunitaire'])
                form = recevoir_valeurs_traitement_immuinosuppresseur()         

        return render(request,'indeex_traitement_immuinosuppresseur.html' ,{'form': form})



    def resultat2(request):

        fievre =True
        toux = Donnees['recevoir_valeurs_toux']
        gorge_ou_courbatures = Donnees['recevoir_valeurs_courbatures']
        manque_de_souffle= Donnees['manque_de_souffle']
        age = Donnees['recevoir_valeurs_age']


        fievre_temp = Donnees['recevoir_valeurs_fiever']


        gout = Donnees['recevoir_valeurs_gout']
        diarrhee = Donnees['recevoir_valeurs_diarrhee']
        fatigue = Donnees['recevoir_valeurs_fatigue']
        impossibilite_de_vous_alimenter = Donnees['recevoir_valeurs_impossibilite_de_vous_alimenter']
        poids = Donnees['recevoir_valeurs_poids']
        taille= Donnees['recevoir_valeurs_taille']
        hypertension = Donnees['recevoir_valeurs_hypertension']
        diabetique = Donnees['recevoir_valeurs_diabetique']
        cancer= Donnees['recevoir_valeurs_cancer']
        insuffisance_renale = Donnees['recevoir_valeurs_insuffisance_renale']
        maladie_respiratoire = Donnees['recevoir_valeurs_maladi_respiratoire']
        maladie_chronique_du_foie = Donnees['indeex_maladie_chronique_du_foie']
        enceinte = Donnees['recevoir_valeurs_enceinte']
        maladie_diminuer_vos_défenses_immunitaires =  Donnees['indeex_maladie_diminuer_ummunitaire']
        traitement_immunosuppresseur = Donnees['recevoir_valeurs_traitement_immuinosuppresseur']
        code_postal = Donnees['E_mail']
        imc=Donnees['recevoir_valeurs_poids']/(Donnees['recevoir_valeurs_taille'])**2

        





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





       
 
       
        return render(request,'resultat2.html' ,{'resultats': resultats})



    def resultat(request):
        if request.method=='POST':
            form =  recevoir_valeurs_code_postal(request.POST)
            if form.is_valid():
                Reponse=form.cleaned_data['E_mail']
                Donnees['E_mail']=Reponse
                Reponse=form.cleaned_data['Ville']
                Donnees['Ville']=Reponse
          
                return render(request,'resultat.html' ,{'form': form})
            






















def poster(request):
    form = DonneesUser()
    return render(request,'indeex.html',{'form': form})


def register(request):

	context={'forms': DonneesUser}

	return render(request,'registration.html',context)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            text=form.cleaned_data['your_name']
            return render(request, 'name.html', {'text': text})
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def next_2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DonneesUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            text=form.cleaned_data['your_name']
            return render(request, 'name.html', {'text': text})
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def choice_field(request):
    # if this is a POST request we need to process the form data
   
        # create a form instance and populate it with data from the request:
    form = DonneesUser()


      

    return render(request, 'indeex.html', {'form': form})
            #return HttpResponseRedirect('/thanks/')
""""""

# Create your views here.

# # Create your views here.
# Post=Post(fievre,fievre_temp,toux,gout,gorge_ou_courbatures,diarrhee,fatigue,impossibilite_de_vous_alimenter,manque_de_souffle,age, poids,taille,hypertension ,diabetique,
#          cancer,maladie_respiratoire,insuffisance_renale,maladie_chronique_du_foie,enceinte,maladie_diminuer_vos_défenses_immunitaires,
#          traitement_immunosuppresseur,code_postal)
# Post.fonction_facteur_pronostique_defavorable()
# Post.fonction_facteur_de_gravite_majeur()
# Post.fonction_facteur_de_gravite_mineur()

# resultats ="""Aucune reposnse"""
# if int(Post.age)<= 15 :
#     resultats = """     Prenez contact avec votre médecin généraliste au moindre doute.
# Cette application n’est pour l’instant pas adaptée aux personnes de moins de 15 ans.
# En cas d’urgence, appeler le 15."""
# elif Post.facteur_de_gravite_majeur >=1:
#     resultats = """Appelez le 15."""
# elif (Post.fievre==True and Post.toux== True):
#     if(Post.facteur_pronostique_defavorable==0):
#         resultats ="""      Votre situation peut relever d’un COVID 19.
# Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""

#     elif Post.facteur_pronostique_defavorable >= 1:
#         if Post.facteur_de_gravite_mineur ==(1 or 2):
#             resultats = """     Votre situation peut relever d’un COVID 19.
#     Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile (SOS médecins, etc.)"""


#         elif Post.facteur_de_gravite_mineur >=2:
#             resultats = """     Votre situation peut relever d’un COVID 19.
#     Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
#     Si vous n'arrivez pas à obtenir de consultation, appelez le 15."""
# elif Post.fievre or(not Post.fievre and(Post.diarrhee or (Post.toux and Post.gorge_ou_courbatures) or (Post.toux and Post.impossibilite_de_vous_alimenter ))):
#     if Post.facteur_pronostique_defavorable==0:
#         if Post.facteur_de_gravite_mineur!=0:
#             resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
# Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
# Nous vous conseillons de rester à votre domicile."""
#         elif Post.facteur_de_gravite_mineur == 0:

#             if Post.age <= 50 :
#                 resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
#     Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
#     Nous vous conseillons de rester à votre domicile."""
#             elif Post.age > 50:
#                 resultats = """Votre situation peut relever d’un COVID 19.
# Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
# Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
#         elif  Post.facteur_de_gravite_mineur!=0:
#             resultats = """     Votre situation peut relever d’un COVID 19.
# Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
# Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""

#     if Post.facteur_pronostique_defavorable != 0:
#         if Post.facteur_de_gravite_mineur <=1:
#             resultats = """     Votre situation peut relever d’un COVID 19.
#     Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
#     Appelez le 15 si une gêne respiratoire ou des difficultés importantes pour vous alimenter ou boire apparaissent pendant plus de 24 heures."""
#         elif Post.facteur_de_gravite_mineur >1:
#             resultats = """     Votre situation peut relever d’un COVID 19.
#     Demandez une téléconsultation ou un médecin généraliste ou une visite à domicile.
#     Si vous n'arrivez pas à obtenir de consultation, appelez le 15.."""
# elif not Post.fievre  and(Post.toux or Post.gorge_ou_courbatures or Post.impossibilite_de_vous_alimenter):
#     if Post.facteur_pronostique_defavorable >=1:
#         resultats = """Votre situation peut relever d’un COVID 19. Un avis médical est recommandé.
# Au moindre doute, appelez le 15. Nous vous conseillons de rester à votre domicile."""
#     elif Post.facteur_pronostique_defavorable==0:
#         resultats = """     Votre situation peut relever d’un COVID 19 qu’il faut surveiller.
# Si de nouveaux symptômes apparaissent, refaites le test ou consultez votre médecin.
# Nous vous conseillons de rester à votre domicile."""
# elif not (Post.fievre and Post.gout and Post.gorge_ou_courbatures and  Post.diarrhee and Post.fatigue and Post.impossibilite_de_vous_alimenter and Post.manque_de_souffle)== True:
#     resultats = """     Votre situation ne relève probablement pas du COVID 19.
# N’hésitez pas à contacter votre médecin en cas de doute.
# Vous pouvez refaire le test en cas de nouveau symptôme pour réévaluer la situation.
# Pour toute information concernant le COVID 19, composer le 0 800 130 000.."""


# print("Post.facteur_de_gravite_mineur     {}".format(Post.facteur_de_gravite_mineur))
# print("Post.facteur_pronostique_defavorable    {}".format(Post.facteur_pronostique_defavorable))
# print("Post.facteur_de_gravite_majeur      {}".format(Post.facteur_de_gravite_majeur))

# print("Post.facteur_de_gravite_majeur     \n\n\n {}".format(resultats))
# print("Post.facteur_de_gravite_majeur     \n\n\n {}".format(fievre))
# """"""
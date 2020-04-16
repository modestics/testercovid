from django import forms
from django.forms import MultiWidget




 
   
   
class resultat(forms.Form):
	CHOIX=[('True','Chine'),
         ('True','Italie'),('True','Corée '), ('True','France '),('False','Autre pays à risque '),('False','Non ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)




class recevoir_valeurs_fiever(forms.Form):
	CHOIX=[(31,'31'),(32,'32'),
         (33,'33'),(34,'34'),(35,'35'),(36,'36'),(37,'37'), (38,'38'),(39,'39'),(40,'40'),(41,'41'),(42,'42')]
	temp=forms.ChoiceField(choices=CHOIX, widget=forms.Select)






class recevoir_valeurs_traitement_immuinosuppresseur(forms.Form):
	CHOIX=[(True,'Oui'), (False,'Non'),(False,'Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)



class recevoir_valeurs_temperature(forms.Form):
	
	temp=forms.IntegerField(label='Degre Celsius' )
  
class recevoir_valeurs_poids(forms.Form):
	poids=forms.IntegerField(label='KG' )

class recevoir_valeurs_diarrhee(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	# CHOIX=[('21', '21'),(' 22' ,'22'),('23' , '23 '),('24' , '24 '),('25 ','25 '),('26' , '26'),('27' ,' 27 '),('28', '28'),('29', '29 '),(' 30' , '30 '),('31' ,'31 '),('32', '32'),('33' ,'33'),('34', '34'),('35 ,35'),('  36', '36'),(' 37' ,'37'),
	# (' 38'  ,'38 '),('39', '39'),('40' , '40')]
	Reponse=forms.ChoiceField(choices=CHOIX , widget=forms.RadioSelect)




class recevoir_valeurs_maladi_respiratoire(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)


class recevoir_valeurs_insuffisance_renale(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)



class indeex_maladie_chronique_du_foie(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_diabetiquee(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)


	


class DonneesUser(forms.Form):
	CHOIX=[('True','hffhfhffjfjf'),
         ('False','Non'),('True','Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_toux(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect(attrs={"class":"container_radio version_2"}))

class recevoir_valeurs_imc(forms.Form):
	CHOIX=[('Trueimc','hffhfhffjfjf'),
         ('Falseimc','Non'),('True','Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)




class recevoir_valeurs_impossibilite_de_vous_alimenter(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class indeex_maladie_diminuer_ummunitaire(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non'),('False','Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_cancer(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_taille(forms.Form):
	
	taille=forms.IntegerField(label='Centimetre' )

class recevoir_valeurs_age(forms.Form):
	
	age=forms.IntegerField(label='Ans' )

class recevoir_valeurs_fatigue_moitiee_journee(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_hypertension(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non'),('True','Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_gout(forms.Form):
	CHOIX=[('True','Oui'),
         ('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect(attrs={"class":"checkmark"}))

class manque_de_souffle(forms.Form):
	CHOIX=[('True','Oui'),('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_fatigue(forms.Form):
	CHOIX=[('True','Oui'),('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_enceinte(forms.Form):
	CHOIX=[('True','Oui'),('False','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)


class recevoir_valeurs_diabetique(forms.Form):
	CHOIX=[('True','Oui'),
         ('True','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_courbatures(forms.Form):
	CHOIX=[('False','Oui'),('True','Non')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

class recevoir_valeurs_code_postal(forms.Form):
	CHOIX=[('False','Oui'),('True','Non')]
	
	E_mail=forms.EmailField(label='E-mail')
	CHOIX=[('ABENGOUROU','ABENGOUROU'),('SAN_PEDRO','SAN PEDRO'),
         ('ABIDJAN','ABIDJAN'),('BOUAKE','BOUAKE'),('KATIOLA','KATIOLA'),('ADZOPE','ADZOPE'),('KORHOGO','KORHOGO')]
	Ville=forms.ChoiceField(choices=CHOIX, widget=forms.Select, )
	


    
from django import forms
from django.forms import MultiWidget




 
   
   
class resultat(forms.Form):
	CHOIX=[('True','Chine'),
         ('True','Italie'),('True','Corée '), ('True','France '),('False','Autre pays à risque '),('False','Non ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)




class recevoir_valeurs_fiever(forms.Form):
	CHOIX=[(37.0, 'Je ne sais pas'),(35.0, '35.0'), (35.1, '35.1'), (35.2, '35.2'), (35.3, '35.3'), 
	(35.4, '35.4'), (35.5, '35.5'), (35.6, '35.6'), (35.7, '35.7'), (35.8, '35.8'),
	 (35.9, '35.9'), (36.0, '36.0'), (36.1, '36.1'), (36.2, '36.2'), (36.3, '36.3'), (36.4, '36.4'),
	  (36.5, '36.5'), (36.6, '36.6'), (36.7, '36.7'), (36.8, '36.8'), (36.9, '36.9'), (37.0, '37.0'),
	   (37.1, '37.1'), (37.2, '37.2'), (37.3, '37.3'), (37.4, '37.4'), (37.5, '37.5'), (37.6, '37.6'), 
	   (37.7, '37.7'), (37.8, '37.8'), (37.9, '37.9'), (38.0, '38.0'), (38.1, '38.1'), (38.2, '38.2'),
	    (38.3, '38.3'), (38.4, '38.4'), (38.5, '38.5'), (38.6, '38.6'), (38.7, '38.7'), (38.8, '38.8'), 
	    (38.9, '38.9'), (39.0, '39.0'), (39.1, '39.1'), (39.2, '39.2'), (39.3, '39.3'), (39.4, '39.4'), 
	    (39.5, '39.5'), (39.6, '39.6'), (39.7, '39.7'), (39.8, '39.8'), (39.9, '39.9'), (40.0, '40.0'),
	     (40.1, '40.1'), (40.2, '40.2'), (40.3, '40.3'), (40.4, '40.4'), (40.5, '40.5'), (40.6, '40.6'), 
	     (40.7, '40.7'), (40.8, '40.8'), (40.9, '40.9'), (41.0, '41.0'), (41.1, '41.1'), (41.2, '41.2'),
	      (41.3, '41.3'), (41.4, '41.4'), (41.5, '41.5'), (41.6, '41.6'), (41.7, '41.7'), (41.8, '41.8'), 
	      (41.9, '41.9')]
	temp=forms.ChoiceField(choices=CHOIX, widget=forms.Select)


class choix_du_pays(forms.Form):
	CHOIX=[('Benin','Bénin'),('Burkina Faso ' ,'Burkina Faso '),
         ('Cameroun ','Cameroun '),('Cap_Vert','Cap Vert'),('Republique_Centrafricaine','République Centrafricaine'),
         ('Republique_du_Congo ','République du Congo'),('Republique_Democratique_du_Congo','République Démocratique du Congo'),
          ('Cote_d_Ivoire','Cote dIvoire'),('Guinee_Bissau','Guinée-Bissau'),('Guinee_Equatoriale','Guinée Equatoriale'),
          ('Gabon','Gabon'),('Gambie','Gambie'),('Ghana','Ghana'),('Guinee','Guinée'),
          ('Liberia','Liberia '),('Mali','Mali'),('Mauritanie','Mauritanie'),('Niger','Niger'),
          ('Nigeria','Nigeria'),('Senegal','Sénégal'),('Sierra_Leone','Sierra Leone'),('Tchad','Tchad'),('Togo','Togo')]
	choix_du_pays=forms.ChoiceField(choices=CHOIX, widget=forms.Select)






class recevoir_valeurs_traitement_immuinosuppresseur(forms.Form):
	CHOIX=[(True,'Oui'), (False,'Non'),(False,'Je ne sais pas ')]
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)



class recevoir_valeurs_temperature(forms.Form):
	
	temp=forms.IntegerField(label='Degre Celsius' )
  
class recevoir_valeurs_poids(forms.Form):
	CHOIX=[(40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), 
(45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), 
(50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'),
 (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), 
 (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'),
  (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), 
  (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'),
   (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'),
    (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), 
    (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), 
    (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), 
    (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), 
    (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), 
    (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), 
    (110, '110'), (111, '111'), (112, '112'), (113, '113'), (114, '114'), 
    (115, '115'), (116, '116'), (117, '117'), (118, '118'), (119, '119'), 
    (120, '120'), (121, '121'), (122, '122'), (123, '123'), (124, '124'),
     (125, '125'), (126, '126'), (127, '127'), (128, '128'), (129, '129'),
      (130, '130'), (131, '131'), (132, '132'), (133, '133'), (134, '134'), 
      (135, '135'), (136, '136'), (137, '137'), (138, '138'), (139, '139'),
      (140, '140'), (141, '141'), (142, '142'), (143, '143'), (144, '144'), 
      (145, '145'), (146, '146'), (147, '147'), (148, '148'), (149, '149'), 
      (150, '150'), (151, '151'), (152, '152'), (153, '153'), (154, '154'), 
      (155, '155'), 
(156, '156'), (157, '157'), (158, '158'), (159, '159'), (160, '160')]
	poids=forms.ChoiceField(choices=CHOIX, widget=forms.Select)

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
	Reponse=forms.ChoiceField(choices=CHOIX, widget=forms.RadioSelect)

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
	CHOIX=[(1.0, '1.0'), (1.01, '1.01'), (1.02, '1.02'), 
	(1.03, '1.03'), (1.04, '1.04'), (1.05, '1.05'), (1.06, '1.06'),
	 (1.07, '1.07'), (1.08, '1.08'), (1.09, '1.09'), (1.1, '1.1'), 
	 (1.11, '1.11'), (1.12, '1.12'), (1.13, '1.13'), (1.14, '1.14'), 
	 (1.15, '1.15'), (1.16, '1.16'), (1.17, '1.17'), (1.18, '1.18'), 
	 (1.19, '1.19'), (1.2, '1.2'), (1.21, '1.21'), (1.22, '1.22'), 
	 (1.23, '1.23'), (1.24, '1.24'), (1.25, '1.25'), (1.26, '1.26'), 
	 (1.27, '1.27'), (1.28, '1.28'), (1.29, '1.29'), (1.3, '1.3'), 
	 (1.31, '1.31'), (1.32, '1.32'), (1.33, '1.33'), (1.34, '1.34'),
	  (1.35, '1.35'), (1.36, '1.36'), (1.37, '1.37'), (1.38, '1.38'), 
	  (1.39, '1.39'), (1.4, '1.4'), (1.41, '1.41'), (1.42, '1.42'), 
	  (1.43, '1.43'), (1.44, '1.44'), (1.45, '1.45'), (1.46, '1.46'), 
	  (1.47, '1.47'), (1.48, '1.48'), (1.49, '1.49'), (1.5, '1.5'),
	   (1.51, '1.51'), (1.52, '1.52'), (1.53, '1.53'), (1.54, '1.54'),
	    (1.55, '1.55'), (1.56, '1.56'), (1.57, '1.57'), (1.58, '1.58'), 
	    (1.59, '1.59'), (1.6, '1.6'), (1.61, '1.61'), (1.62, '1.62'), 
	    (1.63, '1.63'), (1.64, '1.64'), (1.65, '1.65'), (1.66, '1.66'), 
	    (1.67, '1.67'), (1.68, '1.68'), (1.69, '1.69'), (1.7, '1.7'),
	     (1.71, '1.71'), (1.72, '1.72'), (1.73, '1.73'), (1.74, '1.74'),
	      (1.75, '1.75'), (1.76, '1.76'), (1.77, '1.77'), (1.78, '1.78'), 
	      (1.79, '1.79'), (1.8, '1.8'), (1.81, '1.81'), (1.82, '1.82'), 
	      (1.83, '1.83'), (1.84, '1.84'), (1.85, '1.85'), (1.86, '1.86'),
	       (1.87, '1.87'), (1.88, '1.88'), (1.89, '1.89'), (1.9, '1.9'),
	        (1.91, '1.91'), (1.92, '1.92'), (1.93, '1.93'), (1.94, '1.94'),
	         (1.95, '1.95'), (1.96, '1.96'), (1.97, '1.97'), (1.98, '1.98'),
	          (1.99, '1.99'), (2.0, '2.0'), (2.01, '2.01'), (2.02, '2.02'), 
	          (2.03, '2.03'), (2.04, '2.04'), (2.05, '2.05'), (2.06, '2.06'), 
	          (2.07, '2.07'), (2.08, '2.08'), (2.09, '2.09'), (2.1, '2.1'), 
	          (2.11, '2.11'), (2.12, '2.12'),
	 (2.13, '2.13'), (2.14, '2.14'), (2.15, '2.15'), (2.16, '2.16'), (2.17, '2.17'), 
	 (2.18, '2.18'), (2.19, '2.19'), (2.2, '2.2')]
	
	taille=forms.ChoiceField(choices=CHOIX, widget=forms.Select)

class recevoir_valeurs_age(forms.Form):
	CHOIX=[(11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), 
	(17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'),
	 (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), 
	 (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), 
	 (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), 
	 (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'),
	  (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), 
	  (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), 
	  (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), 
	  (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'),
	   (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'),
	    (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), 
	    (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), 
	(100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), 
	(106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110'), (111, '111'),
	 (112, '112'), (113, '113'), (114, '114'), (115, '115'), (116, '116'), (117, '117'), 
	 (118, '118'), (119, '119'), (120, '120')]
	age=forms.ChoiceField( choices=CHOIX, label='Ans',widget=forms.Select(attrs={"class":"form-control form-control-lg" }))

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
	


    
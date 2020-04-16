from django.db import models

class RegistrationData(models.Model):
	recevoir_valeurs_fiever= models.CharField(max_length=100)
	recevoir_valeurs_traitement_immuinosuppresseur = models.CharField(max_length=100)
	recevoir_valeurs_touxt= models.CharField(max_length=100)
	recevoir_valeurs_temperature = models.CharField(max_length=100)
	recevoir_valeurs_poids = models.CharField(max_length=100)
	recevoir_valeurs_diarrhee = models.CharField(max_length=100)
	recevoir_valeurs_maladi_respiratoire = models.CharField(max_length=100)
	recevoir_valeurs_insuffisance_renale = models.CharField(max_length=100)
	indeex_maladie_chronique_du_foie = models.CharField(max_length=100)
	DonneesUser = models.CharField(max_length=100)
	recevoir_valeurs_toux = models.CharField(max_length=100)
	recevoir_valeurs_imc = models.CharField(max_length=100)
	ecevoir_valeurs_impossibilite_de_vous_alimenter = models.CharField(max_length=100)
	indeex_maladie_diminuer_ummunitaire = models.CharField(max_length=100)
	recevoir_valeurs_age = models.CharField(max_length=100)
	recevoir_valeurs_taille = models.CharField(max_length=100)
	recevoir_valeurs_fatigue_moitiee_journee = models.CharField(max_length=100)
	recevoir_valeurs_hypertension = models.CharField(max_length=100)
	recevoir_valeurs_gout = models.CharField(max_length=100)
	recevoir_valeurs_fatigue = models.CharField(max_length=100)
	recevoir_valeurs_enceinte = models.CharField(max_length=100)
	recevoir_valeurs_diabetique = models.CharField(max_length=100)
	recevoir_valeurs_courbatures = models.CharField(max_length=100)
	recevoir_valeurs_code_postal = models.CharField(max_length=100)



# Create your models here.

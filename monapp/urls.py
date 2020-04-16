
from django.urls import path
from. import views

urlpatterns = [
    path('index/resultat/',views.DonneesDuProblem.resultat2,name='ad24'),
	# path('accueil/',views.DonneesDuProblem.accueil,name='reponse'),
	# path('',views.DonneesDuProblem.accueil,name='reponse'),
 #    path('demarrertest/',views.DonneesDuProblem.je_demarre_le_test,name='test'),
 #    #path('',views.DonneesDuProblem.recevoir_valeurs_fiever	,name='reponse'),
 #    #path('fievree/',views.DonneesDuProblem.recevoir_valeurs_fiever_1	,name='reponse2'),
 #    path('form/',views.register,name='add'),
 #    path('form/reponse',views.get_name,name='home'),
      path('index/',views.DonneesDuProblem.index,name='index'),
   
 #    path('choisir/',views.choice_field,name='choix'),
 #    path('recevoir_valeurs_code_postal/',views.DonneesDuProblem.recevoir_valeurs_code_postal,name='ad1'),
 #    path('manque_de_souffle/',views.DonneesDuProblem.manque_de_souffle,name='ad111'),
 #    path('recevoir_valeurs_courbatures/',views.DonneesDuProblem.recevoir_valeurs_courbatures,name='ad2'),
 #    path('recevoir_valeurs_diabetique/',views.DonneesDuProblem.recevoir_valeurs_diabetique,name='ad3'),
 #    path('recevoir_valeurs_diarrhee/',views.DonneesDuProblem.recevoir_valeurs_diarrhee,name='ad3'),
 #    path('recevoir_valeurs_enceinte/',views.DonneesDuProblem.recevoir_valeurs_enceinte,name='ad4'),
 #    path('recevoir_valeurs_fatigue/',views.DonneesDuProblem.recevoir_valeurs_fatigue,name='ad5'),
 #    path('recevoir_valeurs_gout/',views.DonneesDuProblem.recevoir_valeurs_gout,name='ad6'),
 #    path('recevoir_valeurs_hypertension/',views.DonneesDuProblem.recevoir_valeurs_hypertension,name='ad7'),
 #    path('recevoir_valeurs_imc/',views.DonneesDuProblem.recevoir_valeurs_imc,name='ad8'),
 #    path('recevoir_valeurs_impossibilite_de_vous_alimenter/',views.DonneesDuProblem.recevoir_valeurs_impossibilite_de_vous_alimenter,name='ad9'),
 #    path('indeex_maladie_chronique_du_foie/',views.DonneesDuProblem.indeex_maladie_chronique_du_foie,name='ad10'),
 #    path('recevoir_valeurs_insuffisance_renale/',views.DonneesDuProblem.recevoir_valeurs_insuffisance_renale,name='ad11'),
 #    path('recevoir_valeurs_maladi_respiratoire/',views.DonneesDuProblem.recevoir_valeurs_maladi_respiratoire,name='ad12'),
 #    path('recevoir_valeurs_diarrhee/',views.DonneesDuProblem.recevoir_valeurs_diarrhee,name='ad13'),
 #    path('recevoir_valeurs_poids/',views.DonneesDuProblem.recevoir_valeurs_poids,name='ad14'),
 #    path('recevoir_valeurs_temperature/',views.DonneesDuProblem.recevoir_valeurs_temperature,name='ad15'),
 #    path('recevoir_valeurs_toux/',views.DonneesDuProblem.recevoir_valeurs_toux,name='ad16'),
 #    path('recevoir_valeurs_traitement_immuinosuppresseur/',views.DonneesDuProblem.recevoir_valeurs_traitement_immuinosuppresseur,name='ad17'),
 #    path('recevoir_valeurs_fiever/',views.DonneesDuProblem.recevoir_valeurs_fiever,name='ad18'),
 #    path('recevoir_valeurs_fatigue_moitiee_journee/',views.DonneesDuProblem.recevoir_valeurs_fatigue_moitiee_journee,name='ad19'),
 #    path('recevoir_valeurs_age/',views.DonneesDuProblem.recevoir_valeurs_age,name='ad20'),
 #    path('recevoir_valeurs_taille/',views.DonneesDuProblem.recevoir_valeurs_taille,name='ad21'),
 #    path('recevoir_valeurs_cancer/',views.DonneesDuProblem.recevoir_valeurs_cancer,name='ad22'),
 #    path('indeex_maladie_diminuer_ummunitaire/',views.DonneesDuProblem.indeex_maladie_diminuer_ummunitaire,name='ad23'),
 #    path('index/resultat/',views.DonneesDuProblem.recevoir_index,name='ad24'),
    path('resultat2/',views.DonneesDuProblem.resultat2,name='ad24'),






    ]

  

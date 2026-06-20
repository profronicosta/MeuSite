from django.urls import path
from MeuApp import views

# registrar as urls do APP

# Qual url corresponde a cada view '' = home do site
urlpatterns = [
    path('', views.home, name='home'), 
    path('contato/', views.contato, name='contato'),
    path('produtos/', views.exibir_produtos, name='produtos')
]
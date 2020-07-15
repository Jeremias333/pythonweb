from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$', views.home),
	url(r'^lista/', views.lista),
	url(r'^adicionar/', views.adicionar),
	url(r'^enviar/', views.send_funcionario)
]

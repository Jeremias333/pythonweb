from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$', views.home),
	url(r'^lista/', views.lista),
	url(r'^adicionar/', views.adicionar),
	url(r'^enviar/', views.send_funcionario),
	url(r'^deletar/', views.deletar),
	url(r'^delete/', views.delete),
	url(r'^editar/', views.editar),
	url(r'^edite/', views.edite),
	url(r'^editando/', views.edite_funcionario)
]

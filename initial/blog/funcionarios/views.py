from django.shortcuts import render, HttpResponse
# Create your views here.
from .back.dao.dao_funcionario import DaoFuncionario

def home(req):
	desc = "Aqui irá conseguir manipular os dados dos usuários da empresa chatos."
	#return HttpResponse("Bem vindo a seção de funcionarios.")
	return render(req, "funcionarios/index.html", {"desc": desc})

def lista(req):
	dao = DaoFuncionario()
	lista = dao.select_all()

	#return HttpResponse("Lista de funcionarios")
	return render(req, "funcionarios/lista.html", {"lista": lista})
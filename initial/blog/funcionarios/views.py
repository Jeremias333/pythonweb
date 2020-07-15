from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# Create your views here.
from .back.dao.dao_funcionario import DaoFuncionario
from .back.models.funcionario import Funcionario
from django.views.decorators.csrf import csrf_protect


funcionario = Funcionario()
dao = DaoFuncionario()

def home(req):
	desc = "Aqui irá conseguir manipular os dados dos usuários da empresa chatos."
	#return HttpResponse("Bem vindo a seção de funcionarios.")
	return render(req, "funcionarios/index.html", {"desc": desc})

def lista(req):
	lista = dao.select_all()

	#return HttpResponse("Lista de funcionarios")
	return render(req, "funcionarios/lista.html", {"lista": lista, "funcionario": funcionario})

def adicionar(req):
	return render(req, "funcionarios/adicionar.html")

@csrf_protect
def send_funcionario(req):
	if req.method == "POST":
		funcionario.set_name(req.POST['name'])
		funcionario.set_function(req.POST['function'])
		funcionario.set_salary(float(req.POST['salary']))

		dao.add(funcionario)
		lista(req)
	return HttpResponseRedirect("http://127.0.0.1:8000/funcionarios/lista/")

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
	return HttpResponseRedirect("/funcionarios/lista/")

def deletar(req):
	lista = dao.select_all()
	return render(req, "funcionarios/deletar.html", {"lista": lista, "funcionario": funcionario})

def delete(req):
	if req.method == "GET":
		dao.delete_by_id(req.GET['id'])
	return HttpResponseRedirect("/funcionarios/deletar/")

def editar(req):
	lista = dao.select_all()
	return render(req, "funcionarios/editar.html", {"lista": lista, "funcionario": funcionario})

def edite(req):
	if req.method == "GET":
		_id = req.GET["id"];
		lista = dao.select_id(_id)
		funcionario.set_id(lista[0])
		funcionario.set_name(lista[1])
		funcionario.set_function(lista[2])
		funcionario.set_salary(lista[3])

		return render(req, "funcionarios/edite.html", {"funcionario":funcionario})
	

def edite_funcionario(req):
	if req.method == "POST":
		funcionario.set_id(req.POST['id'])
		funcionario.set_name(req.POST['name'])
		funcionario.set_function(req.POST['function'])
		funcionario.set_salary(float(req.POST['salary']))

		dao.update(funcionario, funcionario.get_id())
	return HttpResponseRedirect("/funcionarios/lista/")
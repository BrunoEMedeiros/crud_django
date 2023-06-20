from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from fabricantes.models import Fabricante
from estados.models import Estado
import datetime

def fabricantes(request):
    fabricantes = Fabricante.objects.all().values()
    template = loader.get_template('all_fabricantes.html')
    context = {
        'all_fabricantes': fabricantes
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    fabricantes = Fabricante.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'all_fabricantes': fabricantes
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    estados = Estado.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'myestados' : estados
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    nome = request.POST['nome']
    rs = request.POST['rs']
    ph = request.POST['phone']
    CNPJ = request.POST['CNPJ']
    uf = Estado.objects.filter(id=request.POST['estado']).first()
    fabri = Fabricante(name=nome, razao_social=rs, phone=ph, cnpj=CNPJ, joined_date=datetime.date.today(), estado=uf)
    fabri.save()
    return HttpResponseRedirect(reverse('fabricantes'))

def delete(request, id):
    fabricantes = Fabricante.objects.get(id=id)
    fabricantes.delete()
    return HttpResponseRedirect(reverse('fabricantes'))

def update(request, id):
    fabricantes = Fabricante.objects.get(id=id)
    estados = Estado.objects.all().values()
    template = loader.get_template('update.html')
    context = {
        'all_fabricantes': fabricantes,
        'myestados' : estados
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    nome = request.POST['nome']
    rs = request.POST['rs']
    ph = request.POST['phone']
    CNPJ = request.POST['CNPJ']
    uf = request.POST['estado']
    fabricantes = Fabricante.objects.get(id=id)
    fabricantes.name = nome
    fabricantes.razao_social = rs
    fabricantes.phone = ph
    fabricantes.cnpj = CNPJ
    fabricantes.estado = Estado.objects.get(id=uf)
    fabricantes.save()
    return HttpResponseRedirect(reverse('fabricantes'))
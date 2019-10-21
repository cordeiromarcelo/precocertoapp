from django.shortcuts import render
import openpyxl
from django.utils import timezone
import django_tables2 as tables
from celery import task

from .filters import ProductFilter, ImportsFilter
from .tables import VendasTable, ImportsTable
from .models import Importacao, Vendas
from principal.tasks import upsheet

@task
def index(request):
    if "GET" == request.method:
        importacoes = Importacao.objects.all()

        if not importacoes:
            context = {'importacoes': importacoes}
            return render(request, 'principal/index.html', context)

        importacoes = Importacao.objects.all().order_by("-id")[0]
        context = {'importacoes': importacoes}
        return render(request, 'principal/index.html', context)
    else:
        excel_file = request.FILES["excel_file"]

        i = Importacao(nome=excel_file.name, uploads=excel_file, pub_date=timezone.now())
        i.save()

        upsheet.delay(i.uploads.path, i.id)

        importacoes = Importacao.objects.all().order_by("-id")[0]
        context = {'importacoes': importacoes}
        return render(request, 'principal/index.html', context)

def dash(request):
    f = ProductFilter(request.GET, queryset=Vendas.objects.all())
    table = VendasTable(f.qs)
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request, 'principal/dash.html', {'table': table, 'filter': f})

def imports(request):
    f = ImportsFilter(request.GET, queryset=Importacao.objects.all())
    table = ImportsTable(f.qs)
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request, 'principal/imports.html', {'table': table, 'filter': f})
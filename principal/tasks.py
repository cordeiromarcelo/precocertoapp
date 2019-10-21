from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import task

from app1.celery import app
from .models import Importacao, Vendas
import openpyxl
from django.utils import timezone


@task
def upsheet(path, i):

    wb = openpyxl.load_workbook(path)
    objeto = Importacao.objects.get(id=i)

    worksheet = wb["Sheet1"]
    print(worksheet)

    for row in worksheet.iter_rows(min_row=2):
        objeto.vendas_set.create(produto=row[0].value, 
                            categoria=row[1].value,
                            unidades=int(row[2].value),
                            preco=float(row[3].value.replace("R$ ", "").replace(",", ".")),
                            total=float(row[4].value.replace("R$ ", "").replace(",", ".")),
                            pub_date=timezone.now())

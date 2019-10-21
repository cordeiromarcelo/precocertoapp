import django_tables2 as tables
from .models import Vendas, Importacao

class VendasTable(tables.Table):
    preco = tables.Column(attrs={"cell": {"class": "foo"}})
    total = tables.Column(attrs={"cell": {"class": "foo"}})

    class Meta:
        model = Vendas
        template_name = "django_tables2/bootstrap.html"
        fields = ("produto", "categoria", "unidades", "preco", "total")

class ImportsTable(tables.Table):

    class Meta:
        model = Importacao
        template_name = "django_tables2/bootstrap.html"
        fields = ("nome", "pub_date")
from django.db import models
from django.utils import timezone

class Importacao(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=200)
    uploads = models.FileField(upload_to='uploads/', default="")
    pub_date = models.DateTimeField('Data da Importação')


class Vendas(models.Model):
    def __str__(self):
        return self.produto
    importacao = models.ForeignKey(Importacao, on_delete=models.CASCADE)
    produto = models.CharField(max_length=200, db_column="Produto", verbose_name="Produto")
    categoria = models.CharField(max_length=200, db_column="Categoria", verbose_name="Categoria")
    unidades = models.IntegerField(db_column="Unidades Vendidas no Mês", verbose_name="Unidades Vendidas no Mês")
    preco = models.FloatField(db_column = "Preço de Custo", verbose_name="Preço de Custo")
    total = models.FloatField(db_column = "Total da venda", verbose_name="Total da Venda")
    pub_date = models.DateTimeField(db_column = "Data de Importação", verbose_name="Data de Importação", default=timezone.now())
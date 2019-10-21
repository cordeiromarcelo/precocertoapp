import django_filters
from .models import Vendas, Importacao
from django_filters import DateFilter
from django.db.models import Sum


class ProductFilter(django_filters.FilterSet):
    produto = django_filters.CharFilter(lookup_expr='contains', label='Produto contém:')
    categoria = django_filters.CharFilter(lookup_expr='contains', label='Categoria contém:')
    start_date = DateFilter(field_name='pub_date',lookup_expr=('lte'), label="Data de Importação menor que (mês/dia/ano):") 
    end_date = DateFilter(field_name='pub_date',lookup_expr=('gte'), label="Data de Importação maior que (mês/dia/ano):")

    class Meta:
        model = Vendas
        fields = ("produto", "categoria", "start_date", "end_date")

    @property
    def vendas_sum(self):
        qs = super(ProductFilter, self).qs
        return qs.aggregate(Sum('total'))['total__sum']
    
    def vendas_count(self):
        qs = super(ProductFilter, self).qs
        return qs.count()

    def soma(self):
        try:
            return self.vendas_sum/self.vendas_count()
        except:
            return 0


class ImportsFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='contains', label='Nome da importação contém:')
    start_date = DateFilter(field_name='pub_date',lookup_expr=('lte'), label="Data de Importação menor que (mês/dia/ano):") 
    end_date = DateFilter(field_name='pub_date',lookup_expr=('gte'), label="Data de Importação maior que (mês/dia/ano):")

    class Meta:
        model = Importacao
        fields = ("nome", "start_date", "end_date")
 
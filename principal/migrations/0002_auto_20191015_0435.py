# Generated by Django 2.2.6 on 2019-10-15 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Importacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(db_column='Produto', max_length=200)),
                ('categoria', models.CharField(db_column='Categoria', max_length=200)),
                ('unidades', models.IntegerField(db_column='Unidades Vendidas no Mês')),
                ('preco', models.FloatField(db_column='Preço de Custo')),
                ('total', models.FloatField(db_column='Total da venda')),
                ('importacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Importacao')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
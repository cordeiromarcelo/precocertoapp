# Generated by Django 2.2.6 on 2019-10-21 02:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20191020_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='pub_date',
            field=models.DateTimeField(db_column='Data de Importação', default=datetime.datetime(2019, 10, 21, 2, 1, 52, 50488, tzinfo=utc), verbose_name='Data de Importação'),
        ),
    ]
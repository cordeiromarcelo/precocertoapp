# Generated by Django 2.2.6 on 2019-10-21 07:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20191021_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='pub_date',
            field=models.DateTimeField(db_column='Data de Importação', default=datetime.datetime(2019, 10, 21, 7, 9, 20, 968299, tzinfo=utc), verbose_name='Data de Importação'),
        ),
    ]

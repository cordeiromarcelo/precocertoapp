# Generated by Django 2.2.6 on 2019-10-21 04:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20191021_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='pub_date',
            field=models.DateTimeField(db_column='Data de Importação', default=datetime.datetime(2019, 10, 21, 4, 40, 56, 20528, tzinfo=utc), verbose_name='Data de Importação'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-21 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0015_auto_20191021_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='pub_date',
            field=models.DateTimeField(db_column='Data de Importação', default=datetime.datetime(2019, 10, 21, 8, 26, 19, 882852, tzinfo=utc), verbose_name='Data de Importação'),
        ),
    ]

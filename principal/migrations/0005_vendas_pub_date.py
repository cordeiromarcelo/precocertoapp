# Generated by Django 2.2.6 on 2019-10-20 22:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20191018_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='pub_date',
            field=models.DateTimeField(db_column='Data de Importação', default=datetime.datetime(2019, 10, 20, 22, 50, 55, 633184, tzinfo=utc), verbose_name='Data de Importação'),
        ),
    ]

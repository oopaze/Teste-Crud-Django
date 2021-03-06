# Generated by Django 3.1.1 on 2020-09-22 23:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('quatidade_de_paginas', models.IntegerField(verbose_name='quantidade_de_paginas')),
                ('preco', models.FloatField(verbose_name='preco')),
                ('data_de_inclusao', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='data_de_inclusao')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
            ],
        ),
    ]

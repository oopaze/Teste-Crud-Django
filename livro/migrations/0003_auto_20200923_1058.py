# Generated by Django 3.1.1 on 2020-09-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_auto_20200923_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='quatidade_de_paginas',
            new_name='quantidade_de_paginas',
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-12 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='imagen',
            new_name='Imagen',
        ),
    ]

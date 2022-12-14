# Generated by Django 4.0.6 on 2022-08-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=40)),
                ('asunto', models.CharField(max_length=150)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]

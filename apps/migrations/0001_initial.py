# Generated by Django 4.0.5 on 2022-07-04 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('prenom', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sujet', models.TextField()),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pre_inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('prenom', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sujet', models.TextField()),
                ('ecole', models.TextField()),
                ('formation', models.TextField()),
                ('filiere', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
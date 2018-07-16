# Generated by Django 2.0.7 on 2018-07-16 20:22

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200, verbose_name='Rua')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('provincia', models.CharField(max_length=100, verbose_name='Provincia')),
                ('codigo_postal', models.CharField(max_length=5, verbose_name='Codigo Postal')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('image', models.ImageField(blank=True, upload_to='Media/Images/Evento', verbose_name='Imagem')),
                ('detalhes', models.TextField(verbose_name='Detalhes')),
                ('local', models.CharField(max_length=200, verbose_name='Local')),
                ('start_dia', models.DateTimeField(verbose_name='Inicio dia e hora')),
                ('end_dia', models.DateTimeField(verbose_name='Fim dia e hora')),
                ('pub_data', models.DateTimeField(auto_now_add=True, verbose_name='Publicado')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Endereco')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('start_dia',),
            },
        ),
    ]

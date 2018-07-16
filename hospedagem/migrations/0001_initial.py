# Generated by Django 2.0.7 on 2018-07-16 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='Media/Hospedagens/Imagens', verbose_name='Imagem')),
                ('image_2', models.ImageField(blank=True, upload_to='Media/Hospedagens/Imagens', verbose_name='Imagem')),
                ('image_3', models.ImageField(blank=True, upload_to='Media/Hospedagens/Imagens', verbose_name='Imagem')),
                ('detalhes', models.TextField(blank=True, verbose_name='Detalhes')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('alt_telefone', models.CharField(blank=True, max_length=15, verbose_name='Alternativo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('url', models.URLField(blank=True, verbose_name='Web Site')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospedagens', to='hospedagem.Categoria')),
            ],
            options={
                'ordering': ('-criado',),
            },
        ),
        migrations.AlterIndexTogether(
            name='hospedagem',
            index_together={('id', 'slug')},
        ),
    ]

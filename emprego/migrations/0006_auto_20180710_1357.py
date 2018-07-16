# Generated by Django 2.0.7 on 2018-07-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprego', '0005_auto_20180710_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='icon',
            field=models.CharField(choices=[('<i class="fas fa-laptop"></i>', 'Informática e Telecomunicações'), ('<i class="fas fa-futbol"></i>', 'Desporto e Fitness'), ('<i class="fas fa-medkit"></i>', 'Saúde e Beleza'), ('<i class="fas fa-wrench"></i>', 'Reparação e Manutenção'), ('<i class="fas fa-shopping-basket"></i>', 'Assistente de Loja e Caixa'), ('<i class="fas fa-leaf"></i>', 'Agricultura e Jardinagem'), ('<i class="far fa-chart-bar"></i>', 'Finanças e Contabilidade'), ('<i class="fas fa-lock"></i>', 'Segurança e Vigilância'), ('<i class="fas fa-user-graduate"></i>', 'Formação e Educação'), ('<i class="fas fa-hotel"></i>', 'Restauração, Hotelaria e Turismo'), ('<i class="fas fa-people-carry"></i>', 'Construção'), ('<i class="fas fa-store"></i>', 'Comercial'), ('<i class="far fa-calendar-alt"></i>', 'Publicidade e Eventos'), ('<i class="fas fa-broom"></i>', 'Domésticos e Limpezas'), ('<i class="fas fa-car"></i>', 'Transportes e Logística'), ('Outros', 'Outros')], default='Outros', max_length=35),
        ),
    ]

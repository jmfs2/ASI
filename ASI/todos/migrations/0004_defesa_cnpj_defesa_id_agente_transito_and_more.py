# Generated by Django 5.1.3 on 2024-12-03 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_defesa_options_remove_defesa_documentos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='defesa',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='defesa',
            name='id_agente_transito',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='ano_veiculo',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='modelo_veiculo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='nome_motorista',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='numero_infracao',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='placa_veiculo',
            field=models.CharField(default='', max_length=20),
        ),
    ]

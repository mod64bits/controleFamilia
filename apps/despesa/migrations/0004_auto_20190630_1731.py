# Generated by Django 2.2.2 on 2019-06-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0003_auto_20190630_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='estado',
            field=models.CharField(choices=[('Nao', 'Não Pago'), ('Pago', 'PAGO')], default='Pago', max_length=10, verbose_name='Estado'),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-05 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QRcodeStock', '0006_auto_20210104_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='id_usuario',
            field=models.ForeignKey(default='00', on_delete=django.db.models.deletion.SET_DEFAULT, to='QRcodeStock.usuario', verbose_name='Usuario criador'),
        ),
    ]
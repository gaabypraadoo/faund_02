# Generated by Django 5.1 on 2024-10-02 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faund_app', '0004_remove_ong_quant_pets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ong',
            name='senha_ong',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='senha_tutor',
        ),
    ]
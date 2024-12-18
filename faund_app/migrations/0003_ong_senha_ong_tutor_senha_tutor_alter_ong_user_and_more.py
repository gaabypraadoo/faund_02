# Generated by Django 5.1 on 2024-09-18 23:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faund_app', '0002_rename_email_ong_email_ong_rename_nome_ong_nome_ong_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ong',
            name='senha_ong',
            field=models.CharField(default='default_password', max_length=128),
        ),
        migrations.AddField(
            model_name='tutor',
            name='senha_tutor',
            field=models.CharField(default='default_password', max_length=128),
        ),
        migrations.AlterField(
            model_name='ong',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1 on 2024-10-10 22:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faund_app', '0005_remove_ong_senha_ong_remove_tutor_senha_tutor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to=settings.AUTH_USER_MODEL)),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_enviadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
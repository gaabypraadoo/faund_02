# Generated by Django 5.1 on 2024-11-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faund_app', '0012_pet_tipo_alter_pet_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='pet',
            name='tipo_pet',
            field=models.CharField(max_length=50),
        ),
    ]
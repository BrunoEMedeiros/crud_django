# Generated by Django 4.2.2 on 2023-06-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabricantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='cnpj',
            field=models.CharField(default=12345678910123, max_length=14),
            preserve_default=False,
        ),
    ]
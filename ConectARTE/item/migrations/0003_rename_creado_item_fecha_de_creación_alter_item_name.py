# Generated by Django 4.2.7 on 2023-11-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_item"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="creado",
            new_name="fecha_de_creación",
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=250),
        ),
    ]

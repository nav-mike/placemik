# Generated by Django 4.1 on 2022-12-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0014_remove_order_id_alter_order_temp_id"),
    ]

    operations = [
        migrations.RenameField(model_name="order", old_name="temp_id", new_name="id",),
    ]
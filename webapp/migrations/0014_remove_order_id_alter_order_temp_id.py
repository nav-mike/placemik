# Generated by Django 4.1 on 2022-12-09 14:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0013_order_temp_id_alter_orderitem_price"),
    ]

    operations = [
        migrations.RemoveField(model_name="order", name="id",),
        migrations.AlterField(
            model_name="order",
            name="temp_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
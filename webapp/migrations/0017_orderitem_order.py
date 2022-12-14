# Generated by Django 4.1 on 2022-12-09 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0016_remove_orderitem_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="webapp.order",
            ),
        ),
    ]

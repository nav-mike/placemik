# Generated by Django 4.1 on 2022-11-03 09:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0002_categorygroup_category_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="product", name="amount", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="webapp.categorygroup",
            ),
        ),
    ]

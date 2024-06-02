# Generated by Django 5.0.6 on 2024-05-24 06:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_productmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='if_published',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='is_draft',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_rating',
            field=models.DecimalField(decimal_places=1, default=4.5, max_digits=2, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_slug',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_variations',
            field=models.JSONField(default=list),
        ),
    ]
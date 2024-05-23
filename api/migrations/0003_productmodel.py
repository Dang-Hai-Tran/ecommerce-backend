# Generated by Django 5.0.6 on 2024-05-23 19:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tokenmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('product_thumbnail', models.CharField(max_length=255)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('product_category', models.CharField(choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing'), ('Books', 'Books'), ('Sports', 'Sports'), ('Other', 'Other')], max_length=255)),
                ('attributes', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
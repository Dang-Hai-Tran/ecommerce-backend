# Generated by Django 5.0.6 on 2024-06-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_discountmodel_discount_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountmodel',
            name='discount_uses_count',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-02 20:36

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_index=True, max_length=255)),
                ('product_description', models.CharField(db_index=True, max_length=255)),
                ('product_slug', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('product_thumbnail', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_quantity', models.IntegerField()),
                ('product_category', models.CharField(choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing'), ('Books', 'Books'), ('Sports', 'Sports'), ('Other', 'Other')], max_length=255)),
                ('attributes', models.JSONField(default=dict)),
                ('product_rating', models.DecimalField(decimal_places=1, default=4.5, max_digits=2, validators=[django.core.validators.MinValueValidator(Decimal('1.0')), django.core.validators.MaxValueValidator(Decimal('5.0'))])),
                ('product_variations', models.JSONField(default=list)),
                ('is_draft', models.BooleanField(db_index=True, default=True)),
                ('is_published', models.BooleanField(db_index=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inventory_location', models.CharField(default='unknown', max_length=255)),
                ('inventory_stock', models.IntegerField()),
                ('inventory_reservations', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inventory_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inventory_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('discount_name', models.CharField(max_length=255)),
                ('discount_description', models.CharField(max_length=255)),
                ('discount_code', models.CharField(max_length=255)),
                ('discount_type', models.CharField(choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')], default='Fixed', max_length=255)),
                ('discount_value', models.IntegerField()),
                ('discount_start_date', models.DateField()),
                ('discount_end_date', models.DateField()),
                ('discount_max_uses', models.IntegerField()),
                ('discount_uses_count', models.IntegerField()),
                ('discount_max_per_user', models.IntegerField(default=1)),
                ('discount_min_order_value', models.IntegerField(default=50)),
                ('discount_is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('discount_users', models.ManyToManyField(related_name='discount_users', to=settings.AUTH_USER_MODEL)),
                ('discount_products_applicable', models.ManyToManyField(related_name='discount_products', to='api.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TokenModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(unique=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isExpired', models.BooleanField(default=False)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.11 on 2024-10-02 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=80)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/')),
                ('phone', models.CharField(max_length=20)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_delivery_man', models.BooleanField(default=False)),
                ('is_restaurant', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('bill', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ORDERED', 'Ordered'), ('COOK_READY', 'Cooked Ready'), ('ACCEPT', 'Accept'), ('PICKED_UP', 'Picked Up'), ('DELIVERED', 'Delivered')], default='ORDERED', max_length=20)),
                ('otp', models.CharField(default=0, max_length=20)),
                ('cod', models.BooleanField(default=False)),
                ('delivery_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_product_user', to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(default=None, limit_choices_to={'is_restaurant': True}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_orders', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='package_images/')),
            ],
        ),
        migrations.CreateModel(
            name='PackageOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('bill', models.TextField(default='')),
                ('phone', models.CharField(max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ORDERED', 'Ordered'), ('COOK_READY', 'Cooked Ready'), ('ACCEPT', 'Accept'), ('PICKED_UP', 'Picked Up'), ('DELIVERED', 'Delivered')], default='ORDERED', max_length=20)),
                ('otp', models.CharField(default=0, max_length=20)),
                ('cod', models.BooleanField(default=False)),
                ('delivery_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_package_user', to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_orders', to='authentication.package')),
                ('restaurant', models.ForeignKey(default=None, limit_choices_to={'is_restaurant': True}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_package_orders', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_package_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('rating', models.FloatField(default=0.0)),
                ('product_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=20)),
                ('restaurant', models.ForeignKey(default=None, limit_choices_to={'is_restaurant': True}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_rating', to='authentication.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comments', to='authentication.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PackageOrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('package_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_order_products', to='authentication.packageorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.product')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='products',
            field=models.ManyToManyField(related_name='packages', to='authentication.product'),
        ),
        migrations.AddField(
            model_name='package',
            name='restaurant',
            field=models.ForeignKey(default=None, limit_choices_to={'is_restaurant': True}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_packages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='authentication.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.product')),
            ],
        ),
    ]

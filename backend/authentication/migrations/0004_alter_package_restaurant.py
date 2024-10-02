# Generated by Django 4.2.11 on 2024-10-02 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_order_restaurant_alter_package_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_packages', to=settings.AUTH_USER_MODEL),
        ),
    ]

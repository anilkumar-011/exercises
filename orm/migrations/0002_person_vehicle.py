# Generated by Django 4.2.5 on 2023-09-22 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_shop_owner_remove_vehicle_owner'),
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vehicle'),
        ),
    ]
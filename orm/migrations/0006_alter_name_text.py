# Generated by Django 4.2.5 on 2023-09-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_alter_name_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='text',
            field=models.CharField(max_length=20),
        ),
    ]

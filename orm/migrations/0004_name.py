# Generated by Django 4.2.5 on 2023-09-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_person_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
    ]

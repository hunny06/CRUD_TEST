# Generated by Django 4.0.4 on 2024-06-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teammodel_delete_accountmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodel',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]

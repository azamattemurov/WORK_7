# Generated by Django 5.0.6 on 2024-06-15 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_categorymodel_remove_productsmodels_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='category',
        ),
        migrations.CreateModel(
            name='ProductsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('retyting', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categorymodels')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
    ]

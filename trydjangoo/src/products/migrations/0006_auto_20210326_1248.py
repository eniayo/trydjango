# Generated by Django 3.1.7 on 2021-03-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]

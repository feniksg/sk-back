# Generated by Django 4.2.16 on 2024-09-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='orders', to='api.ordercategory', verbose_name='Категории'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20210924_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(),
        ),
    ]

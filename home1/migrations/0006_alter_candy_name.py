# Generated by Django 4.0.4 on 2022-05-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0005_alter_candy_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candy',
            name='name',
            field=models.CharField(max_length=2000),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp1', '0003_auto_20200831_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='screenshots'),
        ),
    ]
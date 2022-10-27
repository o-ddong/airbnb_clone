# Generated by Django 4.1.2 on 2022-10-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_pets_allowd_house_pets_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=140, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price_per_night',
            field=models.PositiveIntegerField(help_text='Positive Numbers Only', verbose_name='가격'),
        ),
    ]

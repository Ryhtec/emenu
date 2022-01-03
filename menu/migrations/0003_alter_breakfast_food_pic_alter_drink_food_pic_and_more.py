# Generated by Django 4.0 on 2022-01-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_breakfast_drink_lunchdinner_salad_starter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='drink',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='lunchdinner',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='salad',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='starter',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
# Generated by Django 4.0 on 2022-01-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealcategory', models.CharField(choices=[('BreakFast', 'BREAKFAST'), ('Starter', 'STARTER'), ('Lunch and Dinner', 'LUNCH AND DINNER'), ('Salad', 'SALAD'), ('Drinks', 'DRINKS')], max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.1 on 2018-09-10 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='N/A')),
                ('type', models.TextField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack'), ('Other', 'Other')], default='Snack')),
                ('calories', models.IntegerField(default=0)),
                ('carb', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.NutritionDay')),
            ],
        ),
    ]

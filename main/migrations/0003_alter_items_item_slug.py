# Generated by Django 4.2 on 2023-04-07 22:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_restaurants_options_remove_menu_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]

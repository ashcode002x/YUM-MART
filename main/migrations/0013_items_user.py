# Generated by Django 4.2 on 2023-04-14 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_shopkeeper'),
        ('main', '0012_remove_items_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.shopkeeper'),
        ),
    ]
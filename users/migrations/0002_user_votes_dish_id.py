# Generated by Django 4.1.3 on 2022-11-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_votes',
            name='dish_Id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

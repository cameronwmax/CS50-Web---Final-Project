# Generated by Django 4.2.7 on 2023-11-25 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdlist', '0005_alter_list_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]

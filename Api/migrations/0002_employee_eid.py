# Generated by Django 4.0.6 on 2022-07-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

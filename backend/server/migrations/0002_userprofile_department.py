# Generated by Django 4.2.2 on 2023-06-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(default='Sales', max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2022-06-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyurl', '0003_auto_20220628_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

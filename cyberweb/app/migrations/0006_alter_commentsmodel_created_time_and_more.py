# Generated by Django 5.1.3 on 2024-12-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_postmodel_created_time_commentsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]

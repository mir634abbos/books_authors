# Generated by Django 5.0.7 on 2024-07-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorsmodel',
            name='author',
        ),
        migrations.AddField(
            model_name='authorsmodel',
            name='age',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]

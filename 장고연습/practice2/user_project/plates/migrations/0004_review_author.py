# Generated by Django 3.2.13 on 2022-10-06 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0003_auto_20221007_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plates.user'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]

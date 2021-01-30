# Generated by Django 3.1.5 on 2021-01-30 08:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('death_user', '0005_deathuser_useremail'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'death 게시글', 'verbose_name_plural': 'death 게시글'},
        ),
        migrations.AddField(
            model_name='board',
            name='contents',
            field=models.TextField(default='some content', verbose_name='내용'),
        ),
        migrations.AddField(
            model_name='board',
            name='registered_dttm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='등록시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(default='some string', max_length=128, verbose_name='제목'),
        ),
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='death_user.deathuser', verbose_name='작성자'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='board',
            table='death_board',
        ),
    ]

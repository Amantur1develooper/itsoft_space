# Generated by Django 4.0.4 on 2022-05-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ludi',
            name='cource1',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='курс'),
        ),
        migrations.AddField(
            model_name='ludi',
            name='cource2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='курс'),
        ),
        migrations.AddField(
            model_name='ludi',
            name='cource3',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='курс'),
        ),
        migrations.AddField(
            model_name='ludi',
            name='cource4',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='курс'),
        ),
    ]

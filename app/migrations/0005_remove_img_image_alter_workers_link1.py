# Generated by Django 4.0.4 on 2022-05-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_create_link_alter_clients_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='image',
        ),
        migrations.AlterField(
            model_name='workers',
            name='link1',
            field=models.ManyToManyField(to='app.link', verbose_name='соц-сети'),
        ),
    ]
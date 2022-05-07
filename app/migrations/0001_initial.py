# Generated by Django 4.0.4 on 2022-05-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ludi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='фио')),
                ('phone', models.IntegerField(blank=True, max_length=150, null=True, verbose_name='номер телефона')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='почта')),
                ('letter', models.TextField(blank=True, null=True, verbose_name='письма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['created_at'],
            },
        ),
    ]
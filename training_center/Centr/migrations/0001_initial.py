# Generated by Django 3.2.25 on 2024-10-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuTrainingCent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('type', models.CharField(choices=[('PPD', 'Переподготовка'),
                                                   ('DPD', 'Доподготовка')],
                                          default='PPD', max_length=3, verbose_name='Тип')),
            ],
        ),
    ]

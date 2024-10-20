# Generated by Django 3.2.25 on 2024-10-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centr', '0004_alter_menuabout_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuabout',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menuabout',
            name='type',
            field=models.CharField(choices=[('OsS', 'Основные сведенения'),
                                            ('Dok', 'Документы'),
                                            ('Obr', 'Образование'),
                                            ('POU', 'Платные образовательные услуги')],
                                   default='OsS', max_length=3, verbose_name='Тип'),
        ),
    ]

# Generated by Django 3.2.25 on 2024-10-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Centr', '0008_auto_20241012_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True,
                                                 verbose_name='Отчество')),
                ('date_of_birth', models.DateField(blank=True, null=True,
                                                   verbose_name='Дата рождения')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('education', models.CharField(max_length=255, verbose_name='Образование')),
                ('education_level', models.CharField(max_length=255, verbose_name='Уровень образования')),
                ('qualification', models.CharField(max_length=255, verbose_name='Квалификация')),
                ('academic_degree', models.CharField(blank=True, max_length=255, null=True,
                                                     verbose_name='Ученое звание')),
                ('academic_title', models.CharField(blank=True, max_length=255, null=True,
                                                    verbose_name='Ученая степень')),
                ('pedagogical_experience', models.IntegerField(verbose_name='Стаж педагогической работы')),
                ('work_experience', models.IntegerField(verbose_name='Стаж работы в организации')),
                ('professional_development', models.TextField(blank=True, null=True, verbose_name=
                'Повышение квалификации')),
                ('taught_subjects', models.TextField(verbose_name='Преподаваемые дисциплины')),
            ],
        ),
    ]

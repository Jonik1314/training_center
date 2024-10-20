from django.db import models
from django import forms


# Create your models here.
class MenuTrainingCent(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    value_programs = models.IntegerField(default=1, verbose_name='количество программ обучения')
    TYPE = [
        ('PPD', 'Переподготовка'),
        ('DPD', 'Доподготовка'),

    ]

    type = models.CharField(choices=TYPE, max_length=3, default='PPD', verbose_name='Тип')

    def __str__(self):
        return self.title


class MenuAbout(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    TYPE = [
        ('OsS', 'Основные сведенения'),
        ('Dok', 'Документы'),
        ('Obr', 'Образование'),
        ('POU', 'Платные образовательные услуги'),
        ('RPN', 'Руководство. Педагогический (научно-педагогический) состав'),

    ]

    type = models.CharField(choices=TYPE, max_length=3, default='OsS', verbose_name='Тип')

    def __str__(self):
        return self.title


class more_detailed(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    position = models.CharField(max_length=255, verbose_name='Должность')
    education = models.CharField(max_length=255, verbose_name='Образование')
    education_level = models.CharField(max_length=255, verbose_name='Уровень образования')
    qualification = models.CharField(max_length=255, verbose_name='Квалификация')
    academic_degree = models.CharField(max_length=255, verbose_name='Ученое звание', blank=True, null=True)
    academic_title = models.CharField(max_length=255, verbose_name='Ученая степень', blank=True, null=True)
    pedagogical_experience = models.IntegerField(verbose_name='Стаж педагогической работы')
    work_experience = models.IntegerField(verbose_name='Стаж работы в организации')
    professional_development = models.TextField(verbose_name='Повышение квалификации', blank=True, null=True)
    taught_subjects = models.TextField(verbose_name='Преподаваемые дисциплины')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class RecordForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    mail = forms.EmailField(label="Почта")
    telephone = forms.CharField(label="Телефон", max_length=20)
    comment = forms.CharField(label="Коментарий", widget=forms.Textarea, required=False)


class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    phone = forms.CharField(max_length=20, label='Ваш телефон')
    message = forms.CharField(widget=forms.Textarea, label='Ваше сообщение')


class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, label='Номер карты')
    expiry_date = forms.CharField(max_length=5, label='Срок действия')
    cvv = forms.CharField(max_length=3, label='CVV')

from django.db import models
from django.urls import reverse

# Create your models here.
class Ludi(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name="фио" )
    phone = models.IntegerField( blank=True, null=True, verbose_name="номер телефона" )
    email = models.EmailField(max_length=150, blank=True, null=True, verbose_name="почта" )
    letter = models.TextField( blank=True, null=True, verbose_name="письма" )
    cource1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource2 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource3 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource4 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
   

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('about',kwargs={"id":self.pk})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']


class Clients(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name="фио" )
    phone = models.IntegerField( blank=True, null=True, verbose_name="номер телефона" )
    email = models.EmailField(max_length=150, blank=True, null=True, verbose_name="почта" )
    letter = models.TextField( blank=True, null=True, verbose_name="письма" )
    cource1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource2 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource3 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    cource4 = models.CharField(max_length=150, blank=True, null=True, verbose_name="курс" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
   

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('about',kwargs={"id":self.pk})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']

class Create(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновление')

    # def __str__(self):
    #         return self.created_at

class Img(Create):    
    title1 = models.CharField(null=True, blank=True, max_length=20, verbose_name='имя соц-сети')
    # image = models.ImageField( upload_to='сoц-сети',verbose_name='фото соц-сети')
    
    def __str__(self):
            return self.title1

    class Meta:
        verbose_name = 'Соц-сеть-img'
        verbose_name_plural = 'Соц-сети-img'
        ordering = ['-created_at']



class Link(models.Model):
    title = models.CharField(null=True, blank=True, max_length=30, verbose_name='имя акк')
    title1 = models.CharField(null=True, blank=True, max_length=20, verbose_name='имя соц-сети')
    image = models.ManyToManyField(Img, verbose_name='соц-сеть')
    link = models.URLField(null=True, blank=True, verbose_name='ссылки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновление')

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = 'Соц-сеть'
        verbose_name_plural = 'Соц-сети'
        ordering = ['-created_at']



class Workers(Create):
    clas = models.CharField(null=True, blank=True, max_length=150, verbose_name='не нужно')
    image = models.ImageField(upload_to='Сотрудник/', verbose_name='фото работника')
    f_name = models.CharField(null=True, blank=True, max_length=150, verbose_name='ФИО')
    post = models.CharField(null=True, blank=True, max_length=30, verbose_name='должность')
    discription = models.TextField(null=True, blank=True, verbose_name='описание')
    link1 = models.ManyToManyField(Link, verbose_name='соц-сети')
    contact = models.URLField(null=True, blank=True, max_length=200, verbose_name='контакт ссылка')

    def __str__(self):
            return self.f_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-created_at']
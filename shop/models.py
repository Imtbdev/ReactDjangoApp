import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe


class Colors(models.Model):
    color = models.CharField('Цвет', max_length=20)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Gender(models.Model):
    gender = models.CharField('Гендер', max_length=10)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Size(models.Model):
    size = models.CharField(max_length=20, verbose_name="Размер")

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=50, verbose_name="Производитель")

    def __str__(self):
        return self.manufacturer

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'


class SubCategory(models.Model):
    sub_name = models.CharField("Подкатегория", max_length=50)

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Category(models.Model):
    name = models.CharField("Название", max_length=50)
    content = models.ManyToManyField(SubCategory, max_length=50, verbose_name="Категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Производитель")
    name = models.CharField("Название", max_length=50)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    sub_category = models.ForeignKey('SubCategory', on_delete=models.PROTECT, verbose_name="Подкатегория")
    size = models.ManyToManyField(Size, max_length=10, verbose_name="Размер")
    color = models.ManyToManyField(Colors, max_length=100, verbose_name="Цвет")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.CharField(max_length=1000, verbose_name="Описание")
    gender = models.ManyToManyField(Gender, max_length=10, verbose_name="Пол")
    quantity = models.PositiveIntegerField(verbose_name="Кол-во на складе")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Фото")
    seen = models.BooleanField(default=False, blank=True, verbose_name="Просмотрено")
    date_published = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)
    counter = models.PositiveIntegerField(default=0, verbose_name="Костыль")
    popularity_counter = models.PositiveIntegerField(default=0, verbose_name="Заказы товара")
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "100" height=auto"/>')

    img_preview.fget.short_description = 'Миниатюра'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

from django.contrib.admin import display
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFill
from django.urls import reverse

from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT


class Category(MPTTModel, MetaTagMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    parent = TreeForeignKey(
        to='self',
        related_name='child',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='100'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='400'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' --> '.join(full_path[::-1])


    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


class Image(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True,

    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
    )

    product = models.ForeignKey(to='Product', verbose_name='Товар', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основное изображение', default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if self.is_main:
            Image.objects.filter(product=self.product).update(is_main=False)
        super(Image, self).save(force_insert, force_update, update_fields)


    @display(description='Текущее изображение')
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='100'>")

    @display(description='Текущее изображение')
    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='400'>")

    def __str__(self):
        return ''


class Product(MetaTagMixin):
    name = models.CharField(verbose_name='Продукт', max_length=255)
    description = models.TextField(verbose_name='Описание товара', null=True)
    quantity = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категории',
        through='ProductCategory',
        related_name='categories',
        blank=True
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.name


    def images(self):
        return Image.objects.filter(product=self.id)

    def main_image(self):
        image = Image.objects.filter(is_main=True, product=self.id).first()
        if image:
            return image
        return self.images().first()

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.id})

    def main_category(self):
        category = self.categories.filter(categories__productcategory__is_main=True)
        if category:
            return True
        return self.categories.first()






class ProductCategory(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, verbose_name='Категория', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная Категория', default=False)

    def __str__(self):
        return ''


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if self.is_main:
            ProductCategory.objects.filter(product=self.product).update(is_main=False)
        super(ProductCategory, self).save(force_insert, force_update, update_fields)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = "Категории товара"










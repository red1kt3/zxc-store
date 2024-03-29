from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from apps.main.mixins import MetaTagMixin
from apps.user.models import User
from config.settings import MEDIA_ROOT

class BlogCategory(MetaTagMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    # image = models.ImageField(verbose_name='Изображение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality':100},
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


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(MetaTagMixin):

    tags = models.CharField(verbose_name='Тэг', max_length=40)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.tags


    def __str__(self):
        return self.tags


    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(MetaTagMixin):
    category = models.ForeignKey(
        to=BlogCategory,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    tags = models.ManyToManyField(to=Tag, verbose_name='Тэг', blank=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.title


    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='100'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='400'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        format='JPEG',
        options={'quality':100},
        null=True,

    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

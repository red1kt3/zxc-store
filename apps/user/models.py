from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from config.settings import MEDIA_ROOT


class User(AbstractUser):
    phone = PhoneNumberField(verbose_name='Телефон', null=True, blank=True)
    about = models.CharField(verbose_name='О себе', null=True, blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='user/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True

    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100},
    )

    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='100'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='400'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True



# Generated by Django 4.2.6 on 2023-12-16 12:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='user/', verbose_name='Изображение'),
        ),
    ]

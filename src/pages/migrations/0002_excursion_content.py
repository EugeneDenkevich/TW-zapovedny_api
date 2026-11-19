import config.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backphoto',
            name='photo_excursion',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='photo_pages',
                validators=[config.validators.validate_image_size, config.validators.validate_name],
                verbose_name='Фон Экскурсии',
            ),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='excursion_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='excursion_title',
            field=models.CharField(default='Экскурсии', max_length=256, verbose_name='Экскурсии'),
        ),
    ]

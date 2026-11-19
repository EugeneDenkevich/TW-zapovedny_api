import config.validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0002_alter_entertainmentprice_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description_short', models.TextField(max_length=300, verbose_name='Короткое описание')),
                ('description_long', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсии',
            },
        ),
        migrations.CreateModel(
            name='ExcursionPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=256, verbose_name='Услуга')),
                ('price', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=6,
                    null=True,
                    validators=[
                        MaxValueValidator(9999.99),
                        MinValueValidator(0.0),
                    ],
                    verbose_name='Цена',
                )),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='entertainments.excursion')),
            ],
            options={
                'verbose_name': 'Цена экскурсии',
                'verbose_name_plural': 'Услуги и цены',
            },
        ),
        migrations.CreateModel(
            name='PhotoExcursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='photo_excursion', validators=[config.validators.validate_image_size], verbose_name='Фото')),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='entertainments.excursion')),
            ],
            options={
                'verbose_name': 'Фото экскурсии',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]

# Generated by Django 5.0 on 2024-02-26 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='название')),
                ('slug', models.TextField(verbose_name='slug')),
                ('content', models.TextField(verbose_name='контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('creation_date', models.DateField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(blank=True, default=True, null=True, verbose_name='статус публикации')),
                ('views_count', models.IntegerField(blank=True, null=True, verbose_name='кол-во просмотров')),
            ],
            options={
                'verbose_name': 'сообщение блога',
                'verbose_name_plural': 'сообщения блога',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price_per_unit', models.IntegerField(verbose_name='цена за единицу')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateField(verbose_name='дата последнего изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликован')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_name', models.CharField(max_length=200, verbose_name='version name')),
                ('version_number', models.CharField(default='1.0.0', max_length=100, verbose_name='version number')),
                ('current_version', models.CharField(default='1.0.0', max_length=100, verbose_name='version number')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]

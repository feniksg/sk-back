# Generated by Django 4.2.16 on 2024-09-25 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('payment', models.FloatField(verbose_name='Оплата')),
                ('payment_type', models.CharField(choices=[('Сдельная', 'Piecework'), ('Почасовая', 'Hourly')], max_length=32, verbose_name='Тип оплаты')),
                ('categories', models.ManyToManyField(blank=True, null=True, related_name='orders', to='api.ordercategory', verbose_name='Категории')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, default='', max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, default='', max_length=100, verbose_name='Отчество')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Последний вход')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'permissions': [],
            },
        ),
    ]
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    Permission,
    PermissionsMixin,
)

from django.utils import timezone


class PaymentTypeChoices(models.TextChoices):
    PIECEWORK = "Сдельная"
    HOURLY = "Почасовая"


class OrderStatusChoices(models.TextChoices):
    PENDING = "Открыт"
    IN_WORK = "В работе"
    CLOSED = "Закрыт"


class CreationTrackingMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract=True


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        st =  extra_fields.get('is_staff', None)
        if not st:
            user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin, CreationTrackingMixin):
    phone = models.CharField(max_length=15, blank=True, verbose_name = 'Телефон')
    email = models.EmailField(max_length=100, unique=True, verbose_name = 'Email')
    name = models.CharField(max_length=100, blank=True, default="", verbose_name = 'Имя')
    surname = models.CharField(max_length=100, blank=True, default="", verbose_name = 'Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, default="", verbose_name = 'Отчество')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField('Последний вход', blank=True, null=True)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        permissions = []
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    def __str__(self):
        return f'{self.email}'


class OrderCategory(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=128
    )

    def __str__(self) -> str:
        return self.title


class Order(CreationTrackingMixin):
    title = models.CharField(
        verbose_name="Заголовок", 
        max_length=255
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    payment = models.FloatField( 
        verbose_name="Оплата"
    )
    payment_type = models.CharField( 
        verbose_name="Тип оплаты",
        choices=PaymentTypeChoices.choices,
        max_length=32
    )
    categories = models.ManyToManyField(
        to=OrderCategory,
        verbose_name="Категории",
        blank=True,
        related_name="orders",
    )
    status = models.CharField(
        verbose_name="Статус заказа",
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
        max_length=32
    )
    customer = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Заказчик",
        null=True
    )
    performer = models.ForeignKey(
        to=CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Исполнитель",
        related_name="works"
    )
    
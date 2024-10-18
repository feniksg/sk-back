import django_filters
from .models import Order, OrderCategory, PaymentTypeChoices, CustomUser

class OrderFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=OrderCategory.objects.all(),
        to_field_name='id',  # Или другое поле, если нужно
        field_name='categories',
        label='Категории'
    )
    payment_type = django_filters.ChoiceFilter(
        choices=PaymentTypeChoices.choices,  # Предполагается, что это ваш класс выбора
        label='Тип оплаты'
    )
    customer = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        to_field_name='id',
        field_name='customer',
        label='Заказчик', 
    )
    performer = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        to_field_name='id',
        field_name='performer',
        label='Исполнитель', 
    )
    

    class Meta:
        model = Order
        fields = ['categories', 'payment_type', 'customer', 'performer']

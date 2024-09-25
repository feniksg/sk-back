import django_filters
from .models import Order, OrderCategory, PaymentTypeChoices

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

    class Meta:
        model = Order
        fields = ['categories']

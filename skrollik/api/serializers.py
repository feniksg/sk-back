from rest_framework import serializers


from .models import CustomUser, Order, OrderCategory
from django.contrib.auth import authenticate

from skrollik.settings import TZ_MOSCOW
     


class AuthorizationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        label="email",
        write_only=True,
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                if CustomUser.objects.filter(email=email).exists():
                    msg = 'Неверный пароль.'
                    raise serializers.ValidationError(msg, code=401)
                else:    
                    msg = 'Ошибка в номере телефона и/или в пароле.'
                    raise serializers.ValidationError(msg, code=400)
        else:
            msg = 'Оба поля обязательны к заполнению.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
    

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'phone', 'name', 'surname', 'patronymic']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phone=validated_data.get('phone', ''),
            name=validated_data.get('name', ''),
            surname=validated_data.get('surname', ''),
            patronymic=validated_data.get('patronymic', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk','name', 'surname', 'email']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'surname', 'patronymic', 'phone', 'email', 'orders', 'works', 'date_joined']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['orders'] = [OrderMinSerializer(x).data for x in instance.orders.all()]
        rep['works'] = [OrderMinSerializer(x).data for x in instance.works.all()]
        rep['fio'] = f'{instance.surname} {instance.name} {instance.patronymic}'
        rep['date_joined'] = instance.date_joined.strftime("%d.%m.%Y")
        return rep

class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'payment', 'status', 'payment_type', 'categories', 'created_at', 'customer', 'performer']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['categories'] = [OrderCategorySerializer(x).data for x in instance.categories.all()]
        rep['customer'] = CustomUserMinSerializer(instance.customer).data
        if instance.customer:
            rep['customer']['fio'] = f'{instance.customer.surname} {instance.customer.name}'
        else:
            rep['customer']['fio'] = ""
        rep['performer'] = CustomUserMinSerializer(instance.performer).data if instance.performer else None
        return rep

class OrderMinSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'title', 'payment', 'payment_type', 'created_at', 'categories', 'customer']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['categories'] = [OrderCategorySerializer(x).data for x in instance.categories.all()]
        rep['created_at'] = instance.created_at.astimezone(TZ_MOSCOW).strftime("%H:%M %d.%m.%Y")
        rep['customer'] = { "fio": f'{instance.customer.surname} {instance.customer.name}', 'id': instance.customer.pk}
        return rep

class OrderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCategory
        fields = ['id', 'title']



    
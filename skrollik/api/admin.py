from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from . import models


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.CustomUser
        fields = ('email', 'phone', 'name', 'surname', 'patronymic')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.CustomUser
        fields = ('email', 'phone', 'name', 'surname', 'patronymic')

    def __init__(self, *args, **kwargs):
        
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # form = CustomUserChangeForm
    # add_form = CustomUserCreationForm
    list_display = ('__str__', "surname", "name", "email")

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at", 'title')

@admin.register(models.OrderCategory)
class OrderCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email','username','first_name','last_name']
    # list_display_links = ['username']

    fieldsets = (
        (None,{'fields':('username','password','email','first_name','last_name',)}),
        ('Permissions',{
            'fields':(
                'is_active','is_staff','is_superuser',
                'is_admin','is_customer','groups'#'user_permissions'
            )
        }),
        ('Important dates',{'fields':('last_login','date_joined')}),
    )




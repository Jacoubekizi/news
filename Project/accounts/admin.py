from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display =['username', 'email', 'is_staff']
    add_fieldsets = (
        (None, {'classes':('wide',),
            'fields':(
                'email','username', 'password1', 'password2'
            )}
        ),
    )

admin.site.register(CustomUser, CustomAdmin)
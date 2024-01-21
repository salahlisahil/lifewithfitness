from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import TrainingClass, Post, CustomUser

admin.site.register(TrainingClass)
admin.site.register(Post)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'fullname', 'is_active', 'is_staff')
    search_fields = ('email', 'fullname')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fullname',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'fullname', 'is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

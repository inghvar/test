from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Company


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email', 'company')}), # NoQa
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'is_custom_role_1', 'is_custom_role_2')}), # NoQa
        ('Данные', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')} # NoQa
        ),
    )
    search_fields = ('username', 'email', 'first_name')
    ordering = ('email',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)

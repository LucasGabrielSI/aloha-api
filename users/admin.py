from users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    search_fields = ['name']
    list_display = ['name', 'email']
    fieldsets = (None, {'fields': ('name', 'email')}),


admin.site.register(User, UserAdmin)

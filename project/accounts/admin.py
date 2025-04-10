from django.contrib import admin
from .models import User
# Custom User Admin
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'email', 'name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name', 'last_name')
    ordering = ('id',)

admin.site.register(User, CustomUserAdmin)
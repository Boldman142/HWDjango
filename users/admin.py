from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'country')
    search_fields = ('name',)

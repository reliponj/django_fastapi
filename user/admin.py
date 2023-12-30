from django.contrib import admin
from django.contrib.auth.models import Group, User

from user.models import AppUser

admin.site.unregister(Group)  # Unregister default Django model
# admin.site.unregister(User)  # Unregister default Django model


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    exclude = ['password_hash']

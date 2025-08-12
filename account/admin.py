from django.contrib import admin
from .models import userProfile
# Register your models here.
@admin.register(userProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture', 'first_name', 'last_name', 'email')
    search_fields = ('user__username', 'email')
    list_filter = ('user__is_active', 'user__is_staff')
    ordering = ('user__username',)
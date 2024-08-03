

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class CustomUserAdmin(UserAdmin):
    model = Account
    list_display = ["id", "email", "username", "is_whitelisted", "is_active", "is_admin", "is_staff", "is_superuser"]
    list_display_links = ["email", "username"]
    search_fields = ["email", "username"]
    readonly_fields = ['id', 'date_joined', "last_login"]
    list_filter = ['is_admin', 'is_staff', 'is_whitelisted']
    ordering = ('email',)
  
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'profile_picture')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_whitelisted', 'is_active', 'is_superuser')}),
        ('login logout dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_admin', 'is_staff', 'is_whitelisted', 'is_active', 'is_superuser','profile_picture')}
        ),
    )



    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        search_term_lower = search_term.lower()

        if search_term_lower == 'find@admin':
            queryset |= self.model.objects.filter(is_admin=True)
        elif search_term_lower == 'find@staff':
            queryset |= self.model.objects.filter(is_staff=True)
        elif search_term_lower == 'find@whitelisted':
            queryset |= self.model.objects.filter(is_whitelisted=True)  # Ensure this field exists
        elif search_term_lower == 'find@superuser':
            queryset |= self.model.objects.filter(is_superuser=True)

        return queryset, use_distinct
    
admin.site.register(Account, CustomUserAdmin)

from django.contrib import admin
from .models import Snack


class SnackAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'is_accepted']


admin.site.register(Snack, SnackAdmin)

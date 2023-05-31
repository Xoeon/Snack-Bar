from django.contrib import admin
from .models import Snack


class SnackAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Snack, SnackAdmin)

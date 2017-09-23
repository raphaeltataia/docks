from django.contrib import admin
from .models import Company, Dock

# Register your models here.


class CompanynAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials')


class DockAdmin(admin.ModelAdmin):
    list_display = ('initials', 'value', 'date')


admin.site.register(Company)
admin.site.register(Dock)

from django.contrib import admin
from .models import Subsystem, System, SystemGroup


@admin.register(Subsystem)
class SubsystemAdmin(admin.ModelAdmin):
    list_display = ("name", 'system', 'parent', 'system_security_id')


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ("name", 'tenant',  'parent', 'system_security_id')


@admin.register(SystemGroup)
class SystemGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# from import_export.formats import base_formats

from user.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active')

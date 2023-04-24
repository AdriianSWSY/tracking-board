from django.contrib import admin

from apps.columns.models import Column


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    """
    Admin interface for Column model.

    This class is used to customize the admin interface for the Column model.
    """
    pass

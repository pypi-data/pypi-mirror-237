from django.apps import apps
from django.contrib import admin
from django.db import transaction
from tecdoc.utils import get_supplier

from manufacturers.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'new_name', 'has_supplier', 'logo']
    search_fields = ['name', 'new_name']
    list_per_page = 100

    def save_model(self, request, obj, form, change):
        obj.save()
        transaction.on_commit(
            lambda: self._handle_save(obj, form.changed_data))

    def _handle_save(self, obj, changed_data):

        try:
            supplier = get_supplier(obj.new_name or obj.name)
        except Exception:
            supplier = None

        obj.supplier_id = supplier.id if supplier else None
        obj.save()

        if 'new_name' in changed_data and apps.is_installed('celery'):
            from manufacturers.tasks import handle_adjustment_async
            handle_adjustment_async.delay(obj.pk)

from django.db import models
from django.utils.translation import gettext_lazy as _


class Manufacturer(models.Model):

    name = models.CharField(
        _('Manufacturer name'),
        max_length=255,
        unique=True,
        db_index=True)

    new_name = models.CharField(
        _('Destination name'),
        max_length=255,
        blank=True)

    logo = models.ImageField(
        _('Logo'),
        max_length=255,
        blank=True,
        null=True,
        upload_to='manufacturers')

    supplier_id = models.IntegerField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_new_name = self.new_name

    def __str__(self):
        return self.name

    def has_supplier(self):
        return bool(self.supplier_id)

    has_supplier.short_description = 'Tecdoc'
    has_supplier.boolean = True

    class Meta:
        ordering = ['name']
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class ManufacturerField(models.ForeignKey):

    def __init__(
            self,
            to=Manufacturer,
            on_delete=models.SET_NULL,
            verbose_name=_('Manufacturer'),
            blank=True,
            null=True,
            *args, **kwargs):
        super().__init__(
            to=to,
            on_delete=on_delete,
            verbose_name=verbose_name,
            blank=blank,
            null=null,
            *args, **kwargs)

from manufacturers.signals import manufacturer_replaced

from manufacturers.models import Manufacturer

from core import celery_app


@celery_app.task
def handle_adjustment_async(manufacturer_id):
    src = Manufacturer.objects.get(id=manufacturer_id)

    dst, created = Manufacturer.objects.get_or_create(name=src.new_name)

    manufacturer_replaced.send(Manufacturer, src_id=src.id, dst_id=dst.id)

from apps.order.models import Order


def order_created(data):
    Order.objects.create()


def payment_successfully(data):
    order = Order.objects.get(pk=data['id'])
    order.is_paid = True

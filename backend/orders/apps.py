from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.orders'
    def ready(self):
        import backend.orders.signals

from django.apps import AppConfig

class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services.profile'

    def ready(self):
        import services.profile.signals  # import signals.py

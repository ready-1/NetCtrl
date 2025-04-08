from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class CmsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cms"
    verbose_name = "Content Management System"
    
    def ready(self):
        """
        Initialize application-specific configurations when the app is ready.
        
        This method is called when the application is ready to receive requests.
        Use it to register signal handlers and perform other initialization tasks.
        """
        logger.info(f"CMS application {self.name} initialized")
        
        # Import signals module to register handlers
        try:
            import cms.signals
        except ImportError:
            # No signals module yet, this is fine
            pass

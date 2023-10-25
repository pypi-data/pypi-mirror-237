from netbox.search import SearchIndex
from .models import System
from django.conf import settings

# If we run NB 3.4+ register search indexes 
if settings.VERSION >= '3.4.0':
    class SystemIndex(SearchIndex):
        model = System
        fields = (
            ("name", 100),
            ("comments", 5000),
        )

    # Register indexes
    indexes = [SystemIndex]

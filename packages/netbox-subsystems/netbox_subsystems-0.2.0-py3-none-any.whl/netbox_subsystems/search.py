from netbox.search import SearchIndex
from .models import Subsystem, System, SystemGroup
from django.conf import settings

# If we run NB 3.4+ register search indexes 
if settings.VERSION >= '3.4.0':
    class SystemGroupIndex(SearchIndex):
        model = SystemGroup
        fields = (
            ('name', 100),
            ('slug', 110),
            ('description', 500),
        )

    class SystemIndex(SearchIndex):
        model = System
        fields = (
            ('name', 100),
            ('slug', 110),
            ('description', 500),
            ('comments', 5000),
        )

    class SubsystemIndex(SearchIndex):
        model = Subsystem
        fields = (
            ('name', 100),
            ('slug', 110),
            ('description', 500),
            ('comments', 5000),
        )

    # Register indexes
    indexes = [SystemGroupIndex, SystemIndex, SubsystemIndex]

from netbox.filtersets import NetBoxModelFilterSet
from .models import Subsystems
from django.db.models import Q


class SubsystemsFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Subsystems
        fields = ('id', 'name', 'type', 'tenant')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(type__icontains=value)
        )

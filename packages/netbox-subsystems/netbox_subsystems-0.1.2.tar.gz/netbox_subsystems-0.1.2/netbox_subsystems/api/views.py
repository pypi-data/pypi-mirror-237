from rest_framework.routers import APIRootView
from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import SubsystemSerializer


class SubsystemRootView(APIRootView):
    """
    Subsystems API root view
    """
    def get_view_name(self):
        return 'Subsystems'


class SubsystemsViewSet(NetBoxModelViewSet):
    queryset = models.Subsystems.objects.add_related_count(
        models.Subsystems,
        'parent',
        'subsystems_count',
        cumulative=True
    ).prefetch_related('tags')
    # queryset = models.Subsystems.objects.prefetch_related('tags')
    serializer_class = SubsystemSerializer
    filterset_class = filtersets.SubsystemsFilterSet

from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import SubsystemSerializer


class TenantDocumentViewSet(NetBoxModelViewSet):
    queryset = models.Subsystems.objects.prefetch_related('tags')
    serializer_class = SubsystemSerializer
    filterset_class = filtersets.SubsystemsFilterSet

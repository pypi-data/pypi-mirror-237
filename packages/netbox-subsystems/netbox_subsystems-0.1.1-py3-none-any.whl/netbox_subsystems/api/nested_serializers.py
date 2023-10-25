from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer
from ..models import *

__all__ = [
    'NestedSybsystemsSerializer',
]


@extend_schema_serializer(
    exclude_fields=('subsystems_count',),
)
class NestedSybsystemsSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:subsystems-detail')
    subsystems_count = serializers.IntegerField(read_only=True)
    _depth = serializers.IntegerField(source='level', read_only=True)

    class Meta:
        model = Subsystems
        fields = ['id', 'url', 'display', 'name', 'slug', 'subsystems_count', '_depth']

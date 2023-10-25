from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from .nested_serializers import NestedSybsystemsSerializer
from ..models import Subsystems


class SubsystemSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_subsystems-api:subsystems-detail'
    )

    tenant = NestedTenantSerializer()
    parent = NestedSybsystemsSerializer(required=False, allow_null=True)
    subsystems_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Subsystems
        fields = (
            'id', 'url', 'display', 'name', 'parent', 'type', 'tenant',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated', 'subsystems_count', '_depth'
        )



from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from ..models import Subsystems


class SubsystemSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_subsystems-api:subsystems-detail'
    )

    tenant = NestedTenantSerializer()

    class Meta:
        model = Subsystems
        fields = (
            'id', 'url', 'display', 'name', 'parent', 'type', 'tenant',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class NestedSubsystemSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_subsystems-api:subsystems-detail'
    )

    class Meta:
        model = Subsystems
        fields = (
            'id', 'url', 'display', 'name', 'type',
        )

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer, NestedGroupModelSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from .nested_serializers import NestedSystemSerializer, NestedSystemGroupSerializer, NestedSybsystemSerializer
from ..models import Subsystem, System, SystemGroup


class SystemGroupSerializer(NestedGroupModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_subsystems-api:systemgroup-detail')
    parent = NestedSystemGroupSerializer(required=False, allow_null=True)
    tenant_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = SystemGroup
        fields = [
            'id', 'url', 'display', 'name', 'slug', 'parent', 'description', 'tags', 'custom_fields', 'created',
            'last_updated', 'tenant_count', '_depth',
        ]


class SystemSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_subsystems-api:system-detail')
    group = NestedSystemGroupSerializer(required=False, allow_null=True)
    # device_count = serializers.IntegerField(read_only=True)
    # ipaddress_count = serializers.IntegerField(read_only=True)
    # prefix_count = serializers.IntegerField(read_only=True)
    # rack_count = serializers.IntegerField(read_only=True)
    # site_count = serializers.IntegerField(read_only=True)
    # virtualmachine_count = serializers.IntegerField(read_only=True)
    # vlan_count = serializers.IntegerField(read_only=True)
    # vrf_count = serializers.IntegerField(read_only=True)
    # cluster_count = serializers.IntegerField(read_only=True)
    tenant = NestedTenantSerializer(required=False)
    parent = NestedSystemSerializer(required=False, allow_null=True)

    class Meta:
        model = System
        fields = [
            'id', 'url', 'display', 'name', 'slug', 'group', 'tenant', 'parent', 'description', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated', 'security_id',
            # 'circuit_count', 'device_count', 'ipaddress_count', 'rack_count',
            # 'site_count', 'virtualmachine_count', 'vlan_count', 'vrf_count', 'cluster_count', 'prefix_count',
        ]


class SubsystemSerializer(NestedGroupModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_subsystems-api:subsystem-detail'
    )
    system = NestedSystemSerializer(required=False)
    parent = NestedSybsystemSerializer(required=False)

    class Meta:
        model = Subsystem
        fields = (
            'id', 'url', 'display', 'name', 'parent', 'security_id', 'system',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated'
        )



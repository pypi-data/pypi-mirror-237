from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from ..models import System


class SystemSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_systems-api:systems-detail'
    )

    tenant = NestedTenantSerializer()

    class Meta:
        model = System
        fields = (
            'id', 'url', 'display', 'name', 'parent', 'type', 'tenant',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class NestedSystemSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_systems-api:systems-detail'
    )

    class Meta:
        model = System
        fields = (
            'id', 'url', 'display', 'name', 'type',
        )

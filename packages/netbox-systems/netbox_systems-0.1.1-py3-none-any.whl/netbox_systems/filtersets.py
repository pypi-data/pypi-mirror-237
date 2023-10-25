from netbox.filtersets import NetBoxModelFilterSet
from .models import System
from django.db.models import Q


class SystemFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = System
        fields = ('id', 'name', 'type', 'tenant')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(type__icontains=value)
        )

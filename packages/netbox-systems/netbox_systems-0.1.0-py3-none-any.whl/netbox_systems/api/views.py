from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import SystemSerializer


class TenantDocumentViewSet(NetBoxModelViewSet):
    queryset = models.System.objects.prefetch_related('tags')
    serializer_class = SystemSerializer
    filterset_class = filtersets.SystemFilterSet

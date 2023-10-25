from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from . import forms, models, tables, filtersets


class SystemView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.System.objects.all()


class SystemListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.System.objects.all()
    table = tables.SystemTable
    filterset = filtersets.SystemFilterSet
    filterset_form = forms.SystemFilterForm


class SystemEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.System.objects.all()
    form = forms.SystemForm
    template_name = 'netbox_documents/pl_systems_edit.html'


class SystemDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.System.objects.all()

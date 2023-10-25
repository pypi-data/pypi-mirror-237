from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from tenancy.models import Tenant
from .models import System, SystemTypeChoices

from django.conf import settings
from packaging import version

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)
if NETBOX_CURRENT_VERSION >= version.parse("3.5"):
    from utilities.forms.fields import TagFilterField, CommentField, DynamicModelChoiceField
else:
    from utilities.forms import TagFilterField, CommentField, DynamicModelChoiceField


class SystemForm(NetBoxModelForm):
    comments = CommentField()

    tenant = DynamicModelChoiceField(
        label='Учреждение',
        queryset=Tenant.objects.all()
    )

    class Meta:
        model = System
        fields = ('name', 'parent', 'type', 'tenant', 'comments', 'tags')


class SystemFilterForm(NetBoxModelFilterSetForm):
    model = System

    name = forms.CharField(
        label='Название',
        required=False
    )

    tenant = forms.ModelMultipleChoiceField(
        label='Учреждение',
        queryset=Tenant.objects.all(),
        required=False
    )

    type = forms.MultipleChoiceField(
        label='document_type',
        choices=SystemTypeChoices,
        required=False
    )

    tag = TagFilterField(model)

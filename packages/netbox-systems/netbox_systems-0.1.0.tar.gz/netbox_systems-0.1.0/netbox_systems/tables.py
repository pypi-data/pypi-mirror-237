import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import System

TENANT_SYSTEM_LINK = """
{% if record %}
    <a href="{% url 'plugins:netbox_systems:system' pk=record.pk %}">{% firstof record.name record.type %}</a>
{% endif %}
"""


class SystemTable(NetBoxTable):
    name = tables.TemplateColumn(template_code=TENANT_SYSTEM_LINK)
    type = columns.ChoiceFieldColumn()
    tenant = tables.Column(
        linkify=True
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_systems:systems_list'
    )

    class Meta(NetBoxTable.Meta):
        model = System
        fields = ('pk', 'id', 'name', 'type',  'parent', 'tenant', 'comments', 'actions', 'created',
                  'last_updated', 'tags')
        default_columns = ('name', 'type', 'tenant', 'tags')

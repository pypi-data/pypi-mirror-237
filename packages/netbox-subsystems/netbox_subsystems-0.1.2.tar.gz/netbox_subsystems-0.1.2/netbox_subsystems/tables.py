import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import Subsystems

TENANT_SUBSYSTEM_LINK = """
{% if record %}
    <a href="{% url 'plugins:netbox_subsystems:subsystems' pk=record.pk %}">{% firstof record.name record.type %}</a>
{% endif %}
"""


class SubsystemsTable(NetBoxTable):
    name = tables.TemplateColumn(template_code=TENANT_SUBSYSTEM_LINK)
    type = columns.ChoiceFieldColumn()
    tenant = tables.Column(
        linkify=True
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_subsystems:subsystems_list'
    )

    class Meta(NetBoxTable.Meta):
        model = Subsystems
        fields = ('pk', 'id', 'name', 'type',  'parent', 'tenant', 'comments', 'actions', 'created',
                  'last_updated', 'tags')
        default_columns = ('name', 'type', 'tenant', 'tags')

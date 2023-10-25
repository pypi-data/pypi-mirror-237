from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from tenancy.models import Tenant
from .models import Subsystems, SubsystemsTypeChoices

from django.conf import settings
from packaging import version

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)
if NETBOX_CURRENT_VERSION >= version.parse("3.5"):
    from utilities.forms.fields import TagFilterField, CommentField, DynamicModelChoiceField
else:
    from utilities.forms import TagFilterField, CommentField, DynamicModelChoiceField


class SubsystemsForm(NetBoxModelForm):
    comments = CommentField()

    tenant = DynamicModelChoiceField(
        label='Учреждение',
        queryset=Tenant.objects.all()
    )

    class Meta:
        model = Subsystems
        fields = ('name', 'parent', 'type', 'tenant', 'comments', 'tags')


class SubsystemsFilterForm(NetBoxModelFilterSetForm):
    model = Subsystems

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
        label='Тип',
        choices=SubsystemsTypeChoices,
        required=False
    )

    tag = TagFilterField(model)

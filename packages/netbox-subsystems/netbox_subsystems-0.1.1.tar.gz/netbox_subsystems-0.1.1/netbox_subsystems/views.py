from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from . import forms, models, tables, filtersets


class SubsystemsView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Subsystems.objects.all()


class SubsystemsListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Subsystems.objects.all()
    table = tables.SubsystemsTable
    filterset = filtersets.SubsystemsFilterSet
    filterset_form = forms.SubsystemsFilterForm


class SubsystemsEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Subsystems.objects.all()
    form = forms.SubsystemsForm
    template_name = 'netbox_documents/subsystems_edit.html'


class SubsystemsDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = models.Subsystems.objects.all()

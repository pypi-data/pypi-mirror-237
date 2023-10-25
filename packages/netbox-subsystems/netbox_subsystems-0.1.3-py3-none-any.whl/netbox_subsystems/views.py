from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from .models import Subsystems
from .forms import SubsystemsForm, SubsystemsFilterForm
from .tables import SubsystemsTable
from .filtersets import SubsystemsFilterSet


class SubsystemsView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = Subsystems.objects.all()

    def get_extra_context(self, request, instance):
        parents = instance.get_descendants(include_self=True)
        related_models = (
            (Subsystems.objects.restrict(request.user, 'view').filter(patent__in=parents), 'group_id'),
        )

        return {
            'related_models': related_models,
        }


class SubsystemsListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = Subsystems.objects.all()
    # queryset = Subsystems.objects.add_related_count(
        # Subsystems,
        # 'parent',
        # 'subsystems_count',
        # cumulative=True
    # )
    table = SubsystemsTable
    filterset = SubsystemsFilterSet
    filterset_form = SubsystemsFilterForm


class SubsystemsEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = Subsystems.objects.all()
    form = SubsystemsForm
    template_name = 'netbox_subsystems/subsystems_edit.html'


class SubsystemsDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('dcim.view_site', 'dcim.view_device')
    queryset = Subsystems.objects.all()

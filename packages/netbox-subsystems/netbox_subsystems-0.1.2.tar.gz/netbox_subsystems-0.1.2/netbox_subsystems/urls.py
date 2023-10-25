from django.urls import path
from .models import Subsystems
from .views import SubsystemsView, SubsystemsListView, SubsystemsEditView, SubsystemsDeleteView
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('subsystems/', SubsystemsListView.as_view(), name='subsystems_list'),
    path('subsystems/add/', SubsystemsEditView.as_view(), name='subsystems_add'),
    path('subsystems/<int:pk>/', SubsystemsView.as_view(), name='subsystems'),
    path('subsystems/<int:pk>/edit/', SubsystemsEditView.as_view(), name='subsystems_edit'),
    path('subsystems/<int:pk>/delete/', SubsystemsDeleteView.as_view(), name='subsystems_delete'),
    path('subsystems/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='subsystems_changelog', kwargs={
        'model': Subsystems
    }),
)

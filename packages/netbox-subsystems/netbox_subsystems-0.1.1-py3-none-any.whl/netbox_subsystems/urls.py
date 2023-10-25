from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    path('subsystems/', views.SubsystemsListView.as_view(), name='subsystems_list'),
    path('subsystems/add/', views.SubsystemsEditView.as_view(), name='subsystems_add'),
    path('subsystems/<int:pk>/', views.SubsystemsView.as_view(), name='subsystems'),
    path('subsystems/<int:pk>/edit/', views.SystemEditView.as_view(), name='subsystems_edit'),
    path('subsystems/<int:pk>/delete/', views.SystemDeleteView.as_view(), name='subsystems_delete'),
    path('subsystems/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='subsystems_changelog', kwargs={
        'model': models.System
    }),

)

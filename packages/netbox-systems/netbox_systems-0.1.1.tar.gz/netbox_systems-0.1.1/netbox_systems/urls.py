from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    path('tenant-document/', views.SystemListView.as_view(), name='pl_systems_list'),
    path('tenant-document/add/', views.SystemEditView.as_view(), name='pl_systems_add'),
    path('tenant-document/<int:pk>/', views.SystemView.as_view(), name='pl_systems'),
    path('tenant-document/<int:pk>/edit/', views.SystemEditView.as_view(), name='pl_systems_edit'),
    path('tenant-document/<int:pk>/delete/', views.SystemDeleteView.as_view(), name='pl_systems_delete'),
    path('tenant-document/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='pl_systems_changelog', kwargs={
        'model': models.System
    }),

)

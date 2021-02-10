from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('list-company/', login_required(ListCompany.as_view()), name='list-company'),
    path('create-company/', login_required(CreateCompany.as_view()), name='create-company'),
    path('update-company/<int:pk>', login_required(UpdateCompany.as_view()), name='edit-company'),
    path('delete-company/<int:pk>', login_required(DeleteCompany.as_view()), name='delete-company'),

    path('list_activity/', login_required(ListActivityType.as_view()), name='list-activity'),
    path('create-activity/', login_required(CreateActivityType.as_view()), name='create-activity'),
    path('update-activity/<int:pk>', login_required(UpdateActivityType.as_view()), name='edit-activity'),
    path('delete-activity/<int:pk>', login_required(DeleteActivityType.as_view()), name='delete-activity'),

    path('kanban/', login_required(KanbanSupplier.as_view()), name='kanban-supplier'),
    path('list-supplier/', login_required(ListSupplier.as_view()), name='list-supplier'),
    path('create-supplier/', login_required(CreateSupplier.as_view()), name='create-supplier'),
    path('update-supplier/<int:pk>', login_required(UpdateSupplier.as_view()), name='edit-supplier'),
    path('delete-supplier/<int:pk>', login_required(DeleteActivityType.as_view()), name='delete-supplier'),

    path('list-classification/', login_required(ListClassification.as_view()), name='list-classification'),
    path('create-classification/', login_required(CreateClassifications.as_view()), name='create-classification'),
    path('update-classification/<int:pk>', login_required(UpdateClassifications.as_view()), name='edit-classification'),
    path('delete-classification/<int:pk>', login_required(DeleteClassifications.as_view()), name='delete-classification'),
]

urlpatterns += [
    path('companies/', login_required(TemplateView.as_view(template_name='settings/company.html')), name='companies'),
    path('activity_type/', login_required(TemplateView.as_view(template_name='settings/activity.html')), name='activity-type'),
    path('classification/', login_required(TemplateView.as_view(template_name='settings/classification.html')), name='classification'),
    path('supplier/', login_required(TemplateView.as_view(template_name='settings/supplier/list.html')), name='supplier'),
]

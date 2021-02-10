from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.views.generic import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import *


#Company
class ListCompany(ListView):
    model = Company
    context_object_name = 'company'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:companies')


class CreateCompany(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'settings/company/create.html'
    success_url = reverse_lazy('settings:companies')


class UpdateCompany(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'settings/company/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:companies')


class DeleteCompany(DeleteView):
    model = Company
    template_name = 'settings/company/delete.html'
    success_url = reverse_lazy('settings:companies')


# Activity Types
class ListActivityType(ListView):
    model = ActivityType
    context_object_name = 'activity'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:activity-type')


class CreateActivityType(CreateView):
    model = ActivityType
    form_class = ActivityTypeForm
    template_name = 'settings/activity/create.html'
    success_message = 'Success: Activity type was created.'
    success_url = reverse_lazy('settings:activity-type')


class UpdateActivityType(UpdateView):
    model = ActivityType
    form_class = ActivityTypeForm
    template_name = 'settings/activity/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:activity-type')


class DeleteActivityType(DeleteView):
    model = ActivityType
    template_name = 'settings/activity/delete.html'
    success_url = reverse_lazy('settings:activity-type')


# Classifications
class ListClassification(ListView):
    model = Classification
    context_object_name = 'classification'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:classification')


class CreateClassifications(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'settings/classification/create.html'
    success_message = 'Success: Classification was created.'
    success_url = reverse_lazy('settings:classification')


class UpdateClassifications(UpdateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'settings/classification/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:classification')


class DeleteClassifications(DeleteView):
    model = Classification
    template_name = 'settings/classification/delete.html'
    success_url = reverse_lazy('settings:classification')


class KanbanSupplier(ListView):
    model = Supplier
    template_name = 'settings/supplier.html'
    context_object_name = 'supplier'
    paginate_by = 24


class ListSupplier(ListView):
    model = Supplier
    context_object_name = 'supplier'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('settings:supplier')


class CreateSupplier(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'settings/supplier/create.html'
    success_message = 'Success: Supplier was created.'
    success_url = reverse_lazy('settings:kanban-supplier')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class UpdateSupplier(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'settings/supplier/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} edited successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not edited !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('settings:supplier')


class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'settings/supplier/delete.html'
    success_url = reverse_lazy('settings:supplier')

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.views.generic import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from .models import *
from .forms import *


class Home(TemplateView):
    template_name = 'dashboard.html'


class ListBuilding(ListView):
    model = Building
    context_object_name = 'buildings'
    queryset = model.objects.filter(state=True)
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.queryset), 'application/json')
        else:
            return redirect('nerlax:building')


class CreateBuilding(CreateView):
    model = Building
    form_class = buildingForm
    template_name = 'buildings/building/create.html'
    success_message = 'Success: Building was created.'
    success_url = reverse_lazy('nerlax:building')


class UpdateBuilding(UpdateView):
    model = Building
    form_class = buildingForm
    template_name = 'buildings/building/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
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
            return redirect('nerlax:building')


class DeleteBuilding(DeleteView):
    model = Building
    template_name = 'buildings/building/delete.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('nerlax:building')


class ListSupplier(ListView):
    model = Supplier
    context_object_name = 'supplier'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.queryset), 'application/json')
        else:
            return redirect('nerlax:create-building')


class ListUnit(ListView):
    model = Unit
    context_object_name = 'units'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('nerlax:unit')


class CreateUnit(CreateView):
    model = Unit
    form_class = unitForm
    template_name = 'buildings/units/create.html'
    success_message = 'Success: Unit was created.'
    success_url = reverse_lazy('nerlax:unit')


class UpdateUnit(UpdateView):
    model = Unit
    form_class = unitForm
    template_name = 'buildings/units/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
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
            return redirect('nerlax:unit')


class DeleteUnit(DeleteView):
    model = Unit
    template_name = 'buildings/units/delete.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('nerlax:unit')


class ListCommonExpenses(ListView):
    model = CommonExpenses
    context_object_name = 'expenses'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('nerlax:common-expenses')


class CreateCommonExpenses(CreateView):
    model = CommonExpenses
    form_class = commonExpensesForm
    template_name = 'buildings/common_expenses/create.html'
    success_message = 'Success: Common Expenses was created.'
    success_url = reverse_lazy('nerlax:common-expenses')


class UpdateCommonExpenses(UpdateView):
    model = CommonExpenses
    form_class = commonExpensesForm
    template_name = 'buildings/common_expenses/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
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
            return redirect('nerlax:common-expensese')


class DeleteCommonExpenses(DeleteView):
    model = CommonExpenses
    template_name = 'buildings/common_expenses/delete.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('nerlax:common-expenses')


class ListCommonExpensesLines(ListView):
    model = CommonExpensesLines
    context_object_name = 'expenses_lines'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('nerlax:ce-lines')


class CreateCommonExpensesLines(CreateView):
    model = CommonExpensesLines
    form_class = commonExpensesLinesForm
    template_name = 'buildings/common_expenses/lines/create_lines.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                line = CommonExpensesLines(
                    concept=form.cleaned_data.get('concept'),
                    amount=form.cleaned_data.get('amount'),
                    common_expenses=form.cleaned_data.get('common_expenses')
                )
                line.save()
                msj = f'{self.model.__name__} created successful!'
                error = "There isn't error"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} not created !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('nerlax:ce-lines')


class UpdateCommonExpensesLines(UpdateView):
    model = CommonExpenses
    form_class = commonExpensesLinesForm
    template_name = 'buildings/common_expenses/lines/edit_lines.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
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
            return redirect('nerlax:create-ce')


class DeleteCommonExpensesLines(DeleteView):
    model = CommonExpensesLines
    template_name = 'buildings/common_expenses/lines/delete_lines.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.state = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('nerlax:create-ce')
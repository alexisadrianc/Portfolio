from django.shortcuts import *
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import *
from ..web.models import *
from ..web.forms import *
# Create your views here.


def Home(request):
    return render(request, template_name='administration/home.html')


class AcademyList(ListView):
    model = AboutUs
    context_object_name = 'academy'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True),
                                'application/json')
        else:
            return redirect('administration:academy')


class AcademyCreate(CreateView):
    model = AboutUs
    form_class = AcademyForm
    template_name = 'administration/academy/create.html'
    success_message = 'Success: Building was created.'
    success_url = reverse_lazy('administration:academy')


class AcademyUpdate(UpdateView):
    model = AboutUs
    form_class = AcademyForm
    template_name = 'administration/academy/edit.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                msj = f'{self.model.__name__} fue editado satisfactoriamente !!!'
                error = "Hubo un error, Corrijalo !!!"
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 201
                return response
            else:
                msj = f'{self.model.__name__} no fue editado !'
                error = form.errors
                response = JsonResponse({'msj': msj, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('administration:academy')




import json
from django.shortcuts import *
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import *
from django.contrib.auth import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import *
from .models import *


# Create your views here.
class Index(FormView):
    template_name = 'index.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == '2':
                return HttpResponseRedirect('home_employee')
            elif request.user.user_type == '1':
                return HttpResponseRedirect('home_client')
        else:
            return super(Index, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Index, self).form_valid(form)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


class UsersRegister(CreateView):
    model = UserModel
    template_name = 'base/register.html'
    form_class = RegisterUserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = UserModel(
                email=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
            )
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


class ListUsers(ListView):
    model = UserModel
    context_object_name = 'users'

    def get_queryset(self):
        if self.request.user.is_active:
            return self.model.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            """ cuando en vez de objects.filter uso objects.get uso el de abajo pq devuelve un solo elemento"""
            # data = serialize('json', [self.get_queryset(),])
            """Cuando no uso serialize"""
            # list_user = []
            # for user in self.get_queryset():
            #     data_user = {}
            #     data_user['id'] = user.id
            #     data_user['first_name'] = user.first_name
            #     data_user['last_name'] = user.last_name
            #     data_user['username'] = user.username
            #     data_user['user_type'] = user.user_type
            #     data_user['is_active'] = user.is_active
            #     list_user.append(data_user)
            # data = json.dumps(list_user)
            # return HttpResponse(data, 'application/json')
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('base:users')


class CreateUsers(CreateView):
    model = UserModel
    template_name = 'base/user/create.html'
    form_class = UsersForm
    success_url = reverse_lazy('base:users')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                new_user = UserModel(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    user_type=form.cleaned_data.get('user_type'),
                )
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.save()
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
            return redirect('base:users')


class UpdateUsers(UpdateView):
    model = UserModel
    form_class = UsersForm
    template_name = 'base/user/edit.html'

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
            return redirect('base:users')


class DeleteUsers(DeleteView):
    model = UserModel
    template_name = 'base/user/delete.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            object = self.get_object()
            object.is_active = False
            object.save()
            msj = f'{self.model.__name__} delete successful!'
            error = "There isn't error"
            response = JsonResponse({'msj': msj, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('base:users')


class DetailUser(DetailView):
    model = UserModel
    template_name = 'base/profile.html'


#Company
class ListCompany(ListView):
    model = Company
    context_object_name = 'company'
    queryset = model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('base:companies')


class CreateCompany(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'base/company/create.html'
    success_url = reverse_lazy('base:companies')


class UpdateCompany(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'base/company/edit.html'

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
            return redirect('base:companies')


class DeleteCompany(DeleteView):
    model = Company
    template_name = 'base/company/delete.html'

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
            return redirect('base:companies')



import json
from django.shortcuts import *
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import *
from django.contrib.auth import *
from django.http import HttpResponseRedirect, HttpResponse
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
            return HttpResponseRedirect(self.get_success_url())
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
    template_name = 'users/register.html'
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
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_active:
            return UserModel.objects.filter(is_active=True)

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
            return redirect('login:users')


class CreateUsers(CreateView):
    model = UserModel
    template_name = 'users/create.html'
    form_class = UsersForm
    success_url = reverse_lazy('login:users')


class UpdateProfileUser(TemplateView):
    model = UserModel
    template_name = 'users/profile.html'


    # def get_context_data(self, **kwargs):
    #     context = super(ProfileUser, self).get_context_data(**kwargs)
    #
    #     print(context)
    #     return context

from django.shortcuts import *
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import *
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def Login(request):
    template_name = 'login/login.html'
    return render(request, template_name)


class LoginForm(FormView):
    template_name = 'login/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('administrator:home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginForm, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginForm, self).form_valid(form)


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')



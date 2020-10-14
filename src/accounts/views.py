from django.views.generic import TemplateView, CreateView
from .forms import SignupForm, LoginForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView





class LoginView(LoginView):
    form_class = LoginForm
    template_name = "./accounts/login.html"
    success_url = reverse_lazy('list')



class LogoutView(LogoutView):
    template_name = "./voting/list.html"
    success_url = reverse_lazy('list')

class SignupView(CreateView):
    form_class = SignupForm
    template_name = "./accounts/signup.html"
    success_url = reverse_lazy('list')

    # def form_valid(self, form):
    #     user = form.save() 
    #     login(self.request, user)
    #     self.object = user 
    #     return HttpResponseRedirect(self.get_success_url())

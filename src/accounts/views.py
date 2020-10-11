from django.views.generic import TemplateView, CreateView
from .forms import SignupForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login





class LogInView(TemplateView):
    template_name = "./accounts/login.html"

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "./accounts/signup.html"
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save() 
        login(self.request, user)
        self.object = user 
        return HttpResponseRedirect(self.get_success_url())

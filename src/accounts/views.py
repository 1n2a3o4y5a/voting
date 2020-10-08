from django.views.generic import TemplateView

class LogInView(TemplateView):
    template_name = "./accounts/login.html"

class SignUpView(TemplateView):
    template_name = "./accounts/signup.html"
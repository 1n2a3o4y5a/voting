from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignUpView.as_view(), name='login'),
]
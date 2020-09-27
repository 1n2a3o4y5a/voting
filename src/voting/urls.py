from django.urls import path, include
from .views import VotingList


urlpatterns = [
    path('list/', VotingList.as_view()),
]
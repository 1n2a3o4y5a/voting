from django.urls import path, include
from .views import VotingList, VotingDetail


urlpatterns = [
    path('list/', VotingList.as_view(), name='list'),
    path('detail/<int:pk>/', VotingDetail.as_view(), name='detail'),
]
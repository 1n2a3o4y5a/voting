from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comic, Character, Voting

class VotingList(ListView):
    template_name = 'list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = 'ranking.html'
    model = Voting
    queryset = Voting.objects.all() #.filter().order_by('-point')
    context_object_name = "items"

    # def get_queryset(self):
    #     # qs = Voting.objects.filter(name_id__comic_id__id=1).all().order_by('-point')
    #     return Voting.objects.filter(name_id__comic_id__id=1).order_by('-point')



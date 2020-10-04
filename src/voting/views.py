from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comic, Character, Voting

class VotingList(ListView):
    template_name = 'list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = 'ranking.html'
    # model = Comic
    # queryset = Voting.objects.filter(name_id__comic__id=1).all()

    def get_queryset(self):
        qs = Voting.objects.filter().order_by('-point')
        return qs


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comic, Character

class VotingList(ListView):
    template_name = 'list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = 'ranking.html'
    model = Comic
    # queryset = Comic.objects.select_rerated()


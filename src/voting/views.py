from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comic, Character, Voting

class VotingList(ListView):
    template_name = 'list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = 'ranking.html'
    model = Comic
    # queryset = Voting.objects.filter(name_id__comic__id=1).all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context["object_list"] = Comic.objects.all()

    #     return context


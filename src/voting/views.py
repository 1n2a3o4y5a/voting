from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comic, Character, Voting

class VotingList(ListView):
    template_name = 'list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = 'ranking.html'
    model = Comic
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voting"] = Voting.objects.filter(name_id__comic_id__id=self.kwargs['pk']).order_by('-point')
        return context



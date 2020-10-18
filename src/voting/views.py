from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from .models import Comic, Character, Voting
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



class VotingList(ListView):
    template_name = './voting/list.html'
    model = Comic


class VotingDetail(DetailView):
    template_name = './voting/ranking.html'
    model = Comic
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voting"] = Voting.objects.filter(name_id__comic_id__id=self.kwargs['pk']).order_by('-point')
        return context

@login_required
def vote_func(request, pk):
    vote = Voting.objects.get(pk=pk)
    comic_pk = vote.name.comic.pk
    vote.point += 1
    vote.save()
    return redirect('detail', pk=comic_pk)
    



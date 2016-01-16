from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
# Create your views here.
from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['time_now'] = timezone.now()
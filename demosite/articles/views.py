from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import ArticlePage


class ArticlePageListView(ListView):
    model = ArticlePage
    paginate_by = 2
    ordering = ["-first_published_at"]

    def get_context_data(self, **kwargs):
        context = super(ArticlePageListView, self).get_context_data(**kwargs)
        context['time_now'] = timezone.now()

        return context


class ArticlePageDetailView(DetailView):
    model = ArticlePage

    def get_context_data(self, **kwargs):
        context = super(ArticlePageDetailView, self).get_context_data(**kwargs)

        return context
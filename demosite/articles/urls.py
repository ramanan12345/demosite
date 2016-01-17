from django.conf.urls import url

from .views import ArticlePageListView, ArticlePageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)', ArticlePageDetailView.as_view(), name='article_detail'),
    url(r'^$', ArticlePageListView.as_view(), name='articles_list'),

]
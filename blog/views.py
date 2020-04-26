from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'

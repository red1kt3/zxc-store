from django.shortcuts import render
from apps.blog.models import BlogCategory, Article, Tag


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category/list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def tags_to_articles(request, tag_id):
    articles = Article.objects.filter(tags=tag_id)
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'blog/tag/list.html', {'articles': articles, 'tag': tag})



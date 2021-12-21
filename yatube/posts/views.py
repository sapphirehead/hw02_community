from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post, Group


def index(request):
    """Сохраняем в posts выборку из 10 объектов модели Post,
    отсортированных по полю pub_date по убыванию"""
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница с информацией о постах отфильтрованных по группам.
    view-функция принимает параметр slug из path()
    View-функция для страницы сообщества.
    """
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    # Метод .filter позволяет ограничить поиск по критериям.
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

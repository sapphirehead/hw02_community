from django.shortcuts import render, get_object_or_404
from .models import Post, Group


LIMIT = 10


def index(request):
    """Сохраняем в posts выборку из 10 объектов модели Post,
    отсортированных по полю pub_date по убыванию.
    """
    posts = Post.objects.order_by('-pub_date')[:LIMIT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """View-функция для страницы сообщества.
    Страница с информацией о постах отфильтрованных по группам.
    Принимает параметр slug из path()
    """
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

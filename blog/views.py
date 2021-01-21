from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):
    context = {'blogs': Blog.objects.all(), 'blogs_count': Blog.objects.all().count()}
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {'blog': get_object_or_404(Blog, pk=blog_pk)}
    return render(request, 'blog_detail.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def allblogs(request):
    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list,12)

    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        blogs = paginator.page(page)
    except(EmptyPage, InvalidPage):
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})

#def allblogs(request):
#    blogs = Blog.objects
#    return render(request, 'blog/allblogs.html', {'blogs':blogs})

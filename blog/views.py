from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
        return render(request, 'blog_detail.html', {'blog_id': blog_id})


def blog_list_view(request):
    if request.method == 'GET':
        query_blog = models.Blog.objects.all().order_by('-id')
        return render(request, 'blog_list.html', {'blog': query_blog})







# Create your views here.
def message(request):
    return HttpResponse('Это мой первый проект на DJANGO')

def emodji(request):
    return HttpResponse('😀😄🤬🫨🙃💩')
from django.shortcuts import render, HttpResponse
from . import models

def blog_list(request):
    posts = models.Post.objects.all().order_by('-date')
    return render(request, 'blog/bloglist.html', {'posts':posts} )


def post_detail(request, id):
    post = models.Post.objects.get(id=id)
    return render(request, 'blog/postDetail.html',{'post':post})

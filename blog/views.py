from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

def blog_list(request):
    posts = models.Post.objects.all().order_by('-date')
    return render(request, 'blog/bloglist.html', {'posts':posts} )


def post_detail(request, id):
    post = models.Post.objects.get(id=id)
    return render(request, 'blog/postDetail.html',{'post':post})

@login_required(login_url='/accounts/login')
def create_post(request):
    return render(request, 'blog/create_post.html')

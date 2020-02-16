from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Sample.models import Post


def get_jo_name(name):
    name = '조' + name
    return name


def hello(request):
    return render(request, 'hello.html', context={
        'name': get_jo_name('우석')
    })


def see_post(request):
    post_id = request.GET['post_id']

    post = Post.objects.get(id=post_id)

    return render(request, 'posts.html', context={
        'post': post
    })

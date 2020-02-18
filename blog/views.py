from django.shortcuts import render

posts = [
    {
        'author': 'Michael Scott',
        'title': 'Blog Post One',
        'content': 'Nice to meet me!',
        'date_posted': 'March 10, 1983',
    },
    {
        'author': 'Jim Halpert',
        'title': 'Blog Post Two',
        'content': 'Ding Dong!',
        'date_posted': 'March 11, 1983',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Me'})

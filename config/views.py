from django.shortcuts import render

from blog.models import BlogPost

def home(request):
    blog_posts = BlogPost.objects.all()
    context = {'posts': blog_posts}
    return render(request, 'home.html', context)
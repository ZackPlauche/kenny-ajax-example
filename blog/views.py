from django.shortcuts import render, get_object_or_404

from .models import BlogPost



def blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    next_post_id = blog_post.id + 1
    context = {'post': blog_post, 'next_post_id': next_post_id}
    return render(request, 'blog/post_detail.html', context)


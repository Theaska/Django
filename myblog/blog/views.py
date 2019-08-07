from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Blog
from django.shortcuts import render, get_object_or_404
from django.http import Http404

MONTH_ =   ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']

def index(request):
    latest_post_list = Post.objects.order_by('-date_publish')[:10]
    blogs_taglines = Blog.objects.values('tagline')
    return render(request, 'blog/index.html', {'post_list': latest_post_list,
                                             'tg_bl': blogs_taglines})

def post(request, post_id):
    post_ = get_object_or_404(Post, pk=post_id)
    blogs_taglines = Blog.objects.values('tagline')
    return render(request, 'blog/post.html', {'post': post_,
                                             'tg_bl': blogs_taglines})

def blog(request, blog_tag): 
    blog_ = get_object_or_404(Blog, tagline=blog_tag)
    blogs_taglines = Blog.objects.values('tagline')
    return render(request, 'blog/blog.html', {'blog': blog_, 
                                             'tg_bl': blogs_taglines})

def archive(request, month):
    if month in MONTH_:
        posts = Post.objects.filter(date_publish__month = (MONTH_.index(month)+1))
        blogs_taglines = Blog.objects.values('tagline')
        return render(request, 'blog/archive.html', {'posts': posts, 
                                                    'tg_bl': blogs_taglines})
    else:
        raise Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Blog
from django.shortcuts import render, get_object_or_404
from django.http import Http404

MONTH_ =   ['january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december']

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
    if month.lower() in MONTH_:
        posts = Post.objects.filter(date_publish__month = (MONTH_.index(month.lower())+1))
        blogs_taglines = Blog.objects.values('tagline')
        return render(request, 'blog/archive.html', {'posts': posts, 
                                                    'tg_bl': blogs_taglines})
    else:
        raise Http404
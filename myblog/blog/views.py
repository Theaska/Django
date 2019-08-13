from .models import Post, Blog, Author
from django.shortcuts import reverse, render, get_object_or_404, render_to_response, redirect
from django.views import generic
import datetime
from blog.forms import FormComment
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list' 
    def get_queryset(self):
        return Post.objects.order_by('-date_publish')[:10]

class PostView(generic.DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'blog/post.html'
    comment_form = FormComment

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        context = {}
        context.update(csrf(request))
        user = auth.get_user(request)
        context['comments'] = post.comment_set.all().order_by('-date_publish')
        context['post'] = post
        context['user'] = request.user
        if user.is_authenticated:
            context['form'] = self.comment_form
        return render_to_response(template_name=self.template_name, context=context)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_nickname = request.user
            comment.date_publish = datetime.datetime.now()
            post = Post.objects.get(pk=kwargs['post_id'])
            comment.in_post = post
            comment.save()
        return redirect(request.path)

class BlogView(generic.DetailView):
    model = Blog
    slug_field = 'tagline'
    slug_url_kwarg = 'tagline'
    template_name = 'blog/blog.html'

class MonthArchive(generic.MonthArchiveView):
    model = Post
    date_field = 'date_publish'
    template_name = 'blog/archive.html'
    make_object_list = True
    month_format = '%B'
    year = datetime.datetime.now().year
    def get_allow_empty(self):
        return True



=======
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
>>>>>>> 0e9f77b6729c82fdbf00e9cc44ebc3e3f0005958

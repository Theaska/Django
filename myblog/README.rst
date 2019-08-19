==========
MyBlog
==========

MyBlog is the simple Django app.

Quick start
-----------
1. Add 'blog' to your INSTALLED_APPS settings like this:
    INSTALLED_APPS = [
            ....
            'blog',
    ]
2. Add 'users' for google signup in your site: 
    INSTALLED_APPS = [
            ....
            'blog',
            'users',
    ]
3. Include the URLconf to your project urls.py like this:
    path('blog/', include('blog.urls'))
    path('users/', include('users.urls')), 
    path('accounts/', include('allauth.urls')),

4.Run 'python manage.py migrate' to create models:

5.Start the development server and visit https://128.0.0.1:8000 /blog/
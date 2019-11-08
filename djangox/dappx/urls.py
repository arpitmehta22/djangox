
from django.conf.urls import url
from django.urls import path

from dappx import views
app_name = 'dappx'
urlpatterns=[
path('',views.index,name='home'),



path('candidates.html',views.candidates,name='candidates'),

    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('blog.html',views.blog,name='blog'),
    path('new-post.html',views.new_post,name='new-post'),
    path('job-post.html',views.job_post,name='job-post'),
    path('blog-single.html',views.blog_single,name='blog-single'),

]

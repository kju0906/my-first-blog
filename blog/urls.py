from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.about, name='about'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.blog_sample, name='blog_single'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.blog, name='blog'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.features, name='features'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.portfolio, name='portfolio'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.project_sample, name='project_sample'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.home, name='home'),
]

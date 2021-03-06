from django.conf.urls import include, url
from blog import views
from blog import views_cbv

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # url(r'^(?P<pk>\w+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\w+)/$', views_cbv.post_detail, name='post_detail'),

    # url(r'^new/$', views.post_new, name='post_new'),
    url(r'^new/$', views_cbv.post_new, name='post_new'),

    # url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),

    # url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),

    url(r'^index2/$', views.index2, name='index2'),
    url(r'^(?P<category_pk>\d+)/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/20/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^api/v1/', include('blog.api.v1', namespace='api_v1')),
]

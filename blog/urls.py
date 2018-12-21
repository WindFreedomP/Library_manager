from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'(?P<a_id>\d)/$',views.blog_content,name="blog_content"),
]

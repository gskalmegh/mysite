
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.conf.urls import url,include

urlpatterns = [

    url(r'^(?P<pk>\d+)', DetailView.as_view(
        model=Post,
        template_name="blog/post.html")),

    url(r'^', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                  ]

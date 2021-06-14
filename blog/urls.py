from django.urls import path

from blog.views import BlogPostListView

urlpatterns = [
    path("", BlogPostListView.as_view(), name="post_list"),
]

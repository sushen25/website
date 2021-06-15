from django.shortcuts import render
from django.views.generic.list import ListView

from .models import BlogPost


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 50
    context_object_name = "post_list"
    template_name = "blog/post_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogPostListView, self).get_context_data()
        return context

    def get_queryset(self):
        queryset = super(BlogPostListView, self).get_queryset()
        return [
            post for post in queryset if post.can_be_viewed_by(user=self.request.user)
        ]


def index(request):
    return render(request, "blog/posts.html")

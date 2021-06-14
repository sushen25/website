from django.shortcuts import render
from django.views.generic.list import ListView

from .models import BlogPost


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 50
    context_object_name = "post_list"
    template_name = "blog/post_list.html"


def index(request):
    return render(request, "blog/posts.html")

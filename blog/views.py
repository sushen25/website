from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/posts.html")
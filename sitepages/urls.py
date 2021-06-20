from django.urls import path

from sitepages.views import home


urlpatterns = [
    path("", home, name="home"),
]

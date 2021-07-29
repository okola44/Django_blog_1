from .views import make_blog
from django.urls import path


urlpatterns=[
path("write/",make_blog, name="make_blog"),
]
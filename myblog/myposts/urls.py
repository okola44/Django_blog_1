from .views import make_blog
from django.urls import path


urlpatterns=[path("admin/",homepage, name="homepage"),]
from django.shortcuts import render

# Create your views here.
def make_blog(request):
    return render (request,"homepage.html")
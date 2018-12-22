from django.shortcuts import render
from .models import BlogArticle

# Create your views here.
def blog_title(request):
    blogs=BlogArticle.objects.all()
    return render(request,"blog/title.html",{"blogs":blogs})

def blog_content(request,a_id):
    article=BlogArticle.objects.get(id=a_id)
    return render(request,"blog/content.html",{"articles":article})

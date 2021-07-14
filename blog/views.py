from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(datum_objave__lte=timezone.now()).order_by('datum_objave')
    return render(request, 'blog/post_list.html', {'posts' : posts})

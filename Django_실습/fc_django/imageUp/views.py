from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import FormView
# Create your views here.


class PostView(FormView):
    template_name = 'imageUp/imageUp.html'
    form_class = PostForm
    success_url = '/'
from typing import Any
from django import http
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from .forms import PostForm,CommentForm
from .models import Post,Comment
from django.shortcuts import redirect

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object, active=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handles the comment form submission
        post = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        # If the form is invalid, reload the page with form errors
        return self.get(request, *args, **kwargs)  
    

class AddPostView(FormView):
    template_name= "new_post.html"
    form_class=PostForm
    success_url="/"

    def dispatch(self, request, *args, **kwargs) :
        self.request= request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object=Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image'],
            description = form.cleaned_data['description']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was succesful')
        return super().form_valid(form)

   
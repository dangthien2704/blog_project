from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


class PostListView(ListView):
    model = BlogPost
    ordering = ["-date_created"]
    # template_name = 'myapp/post_list.html'
    context_object_name = "posts"
    paginate_by = 3


class UserPostListView(ListView):
    model = BlogPost
    # ordering = ['-date_created']
    template_name = "myapp/user_posts.html"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return BlogPost.objects.filter(post_author=user).order_by("-date_created")


class PostDetailView(DetailView):
    model = BlogPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ["post_title", "post_content"]

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ["post_title", "post_content"]

    def test_func(self):  # First way to do test_func s
        post =  self.get_object()  #to get the current post we want to update
        if self.request.user == post.post_author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = "/myapp/"

    def test_func(self): # the second way, its a little shorter than the above
        if self.get_object().post_author == self.request.user:
            return True
        else:
            return False


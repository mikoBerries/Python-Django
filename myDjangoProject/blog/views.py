from datetime import date
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm


def starting_page(request):

    three_lastest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": three_lastest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-post.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


class StartingPageView(ListView):
    " View to handle index pages of blog"
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        " manipulate query to get only 3"
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    template_name = "blog/all-post.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    # template_name = "blog/post-detail.html"
    # model = Post
    # context_object_name = "post"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     # Post.objects.get.
    #     # request = self.request
    #     return context

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

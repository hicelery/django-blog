from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from requests import post
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """Display and individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    # Post request for comment forms
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form, }

    return render(
        request,
        "blog/post_detail.html",
        context,
    )


def comment_edit(request, slug, comment_id):
    """View to edit a comment.

    """
    if request.method == "POST":
        # Get the comment to edit
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        # check if the user is the author of the comment and form valid
        if comment.author == request.user and comment_form.is_valid():

            # If the user is the author, update the comment with the new content and save it
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated successfully'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'You are not authorized to edit this comment'
            )
        # Redirect the user back to the post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

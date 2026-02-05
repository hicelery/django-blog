from django.contrib import messages
from django.shortcuts import render
from .models import AboutPage, CollaborateRequest
from django.views import generic
from requests import post
from .forms import CollaborateRequestForm

# Create your views here.


def about_detail(request):
    """Display the first About Page.

    **Context**

    ``aboutpage``
        An instance of :model:`about.AboutPage`.

    **Template:**
    :template:`about/about.html`
    """

    about = AboutPage.objects.first()

    # Post request for comment forms
    if request.method == "POST":
        collaborate_request_form = CollaborateRequestForm(data=request.POST)
        if collaborate_request_form.is_valid():
            CollaborateRequest = collaborate_request_form.save(commit=False)
            CollaborateRequest.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request submitted successfully'
            )
    collaborate_request_form = CollaborateRequestForm()
    context = {"about": about,
               "collaborate_request_form": collaborate_request_form}
    return render(
        request,
        "about/about.html",
        context,
    )

from django.shortcuts import render
from .models import AboutPage
from django.views import generic

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

    context = {"about": about}

    return render(
        request,
        "about/about.html",
        context,
    )

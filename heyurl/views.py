from django.shortcuts import render
from django.http import HttpResponse
import validators

from .models import (
    Url,
    Click
)
from .utils import short_url_generator


def index(request):
    urls = Url.objects.order_by('-created_at')
    context = {'urls': urls}
    return render(request, 'heyurl/index.html', context)


def store(request):
    original_url = request.POST.get('original_url', None)

    if not original_url:
        return HttpResponse("No url provided")

    if not validators.url(original_url):
        return HttpResponse("Invalid url")

    Url.objects.create(
        original_url=original_url,
        short_url=short_url_generator()
    )

    return HttpResponse("Storing a new URL object into storage")


def short_url(request, short_url):
    # FIXME: Do the logging to the db of the click with the user agent and browser
    return HttpResponse("You're looking at url %s" % short_url)

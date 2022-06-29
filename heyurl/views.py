from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.db.models import Count
from datetime import datetime
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

    try:
        Url.objects.create(
            original_url=original_url,
            short_url=short_url_generator()
        )
    except IntegrityError:
        return HttpResponse("Url already exists in the database")

    return HttpResponse("Storing a new URL object into storage")


def get_url_object(short_url):
    try:
        return Url.objects.get(short_url=short_url)
    except Url.DoesNotExist:
        return None


def short_url(request, short_url):
    url_instance = get_url_object(short_url)
    if not url_instance:
        context = {'url': short_url}
        return render(request, 'heyurl/short_url_not_found.html', context)

    url_instance.clicks += 1
    url_instance.save()

    Click.objects.create(
        url=url_instance,
        browser=(request.user_agent.browser.family + ' ' + request.user_agent.browser.version_string).strip(),
        platform=(request.user_agent.os.family + ' ' + request.user_agent.os.version_string).strip()
    )

    return HttpResponse("You're looking at url %s" % short_url)


def metrics_panel(request, short_url):
    url_instance = get_url_object(short_url)
    if not url_instance:
        context = {'url': short_url}
        return render(request, 'heyurl/short_url_not_found.html', context)

    clicks = Click.objects.filter(url=url_instance, created_at__month=datetime.now().month)

    clicks_per_day = clicks.values('created_at__day').annotate(clicks=Count('created_at'))

    most_used_browser = clicks.values("browser").annotate(count=Count('browser')).order_by("-count").first()

    most_used_platform = clicks.values("platform").annotate(count=Count('platform')).order_by("-count").first()

    context = {
        'clicks_per_day': clicks_per_day,
        'url': url_instance,
        'clicks_count': len(clicks),
        'most_used_browser': most_used_browser,
        'most_used_platform': most_used_platform
    }
    return render(request, 'heyurl/metrics_panel.html', context)

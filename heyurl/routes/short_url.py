from django.urls import path

from heyurl import views

urlpatterns = [
    path('', views.short_url, name='short_url'),
    path('panel', views.metrics_panel, name='short_url_metrics_panel'),
]

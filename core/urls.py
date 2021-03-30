from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns=[
    path('home/', views.home),
    path("", RedirectView.as_view(url='/home/')),
]

urlpatterns += staticfiles_urlpatterns()
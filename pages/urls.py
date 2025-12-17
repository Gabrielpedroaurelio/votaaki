from django.urls import path
from .views import IndexView,PollView
urlpatterns=[
    path("",IndexView.as_view(),name="index-site"),
    path("enquete/",PollView.as_view(),name="index-poll"),
]
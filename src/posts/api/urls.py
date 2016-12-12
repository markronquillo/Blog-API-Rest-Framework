from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<abc>[\w-]+)$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<abc>[\w-]+)/edit$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<abc>[\w-]+)/delete$', PostDeleteAPIView.as_view(), name='delete'),
]
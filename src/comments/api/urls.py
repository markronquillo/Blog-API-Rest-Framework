from django.conf.urls import url
from django.contrib import admin

from .views import (
		CommentDetailAPIView,
		CommentListAPIView
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    # url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<abc>[\w-]+)$', CommentDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<abc>[\w-]+)/edit$', PostUpdateAPIView.as_view(), name='update'),
    # url(r'^(?P<abc>[\w-]+)/delete$', PostDeleteAPIView.as_view(), name='delete'),
]
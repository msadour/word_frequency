"""Urls."""

from django.urls import path

from word_frequency_api.views import WordFrequencyView

urlpatterns = [
    path("", WordFrequencyView.as_view()),
]

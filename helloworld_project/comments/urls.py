from django.urls import path

from .views import commentsView

urlpatterns = [
    path('', commentsView, name="comments"),
]
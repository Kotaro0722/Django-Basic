from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_line, name="post_list")
]

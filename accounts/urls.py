# could be remove in chapter 8, django-allauth
# from django.urls import path

from .views import SignupPageView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]

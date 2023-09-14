from django.urls import path

from prices.views import about, contact, home

urlpatterns = [
    path("", home),  # home
    path("about/", about),  # /about/
    path("contact/", contact),  # /contact/
]

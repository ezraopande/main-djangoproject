from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("mbote", views.mbote),
    path("john", views.james),
    path("emobilis", views.emobilis),
    path("home", views.home)

]
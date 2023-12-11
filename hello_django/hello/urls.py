from django.urls import path
from hello import views


urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>/", views.hello_there, name="hello")
]
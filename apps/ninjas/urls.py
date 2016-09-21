from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^ninjas/(?P<color>\w+)$', views.show_color),
    url(r'^ninjas/$', views.four)
]
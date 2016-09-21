from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^newuser$", views.newuser, name="newuser"),
    url(r"^login$", views.login, name="login"),
    url(r"^success$", views.success, name="success"),
    url(r"^usercourses$", views.usercourses, name="usercourses"),
    url(r'^delete/(?P<id>\d+)', views.delete, name="delete"),
    url(r'^addusertocourse$', views.addusertocourse, name="addusertocourse")
 
]
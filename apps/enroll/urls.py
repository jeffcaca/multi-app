from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^addcourse$', views.addcourse, name="addcourse"),
    url(r'^delete/(?P<id>\d+)', views.delete, name="delete")
   	

]
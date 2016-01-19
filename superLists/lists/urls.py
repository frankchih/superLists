from django.conf.urls import url
from lists import views


urlpatterns = [
    url(r'^the-only-list-in-the-world/$', views.viewLists, name='viewLists'),
    url(r'^$', views.homePage, name='homePage'),
]
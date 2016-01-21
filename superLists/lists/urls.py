from django.conf.urls import url
from lists import views


urlpatterns = [
    url(r'^the-only-list-in-the-world/$', views.viewList, name='viewList'),
    url(r'^new/$', views.newList, name='newList'),
    url(r'^$', views.homePage, name='homePage'),
]
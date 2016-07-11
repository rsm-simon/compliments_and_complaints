from django.conf.urls import url

from . import views

app_name = 'compliments'
urlpatterns = [
    url(r'^$', views.ComplimentView.as_view(), name='compliment'),
]

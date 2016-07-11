from django.conf.urls import url

from . import views

app_name = 'complaints'
urlpatterns = [
    url(r'^$', views.ComplaintView.as_view(), name='complaint'),
]

from django.conf.urls import url

from . import views

app_name = 'tracker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^(?P<todo_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]

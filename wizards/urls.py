from django.conf.urls import patterns, url
from wizards.views import TaskView


urlpatterns = patterns('',
    url(r'^$', TaskView.as_view(), name='task'),
)

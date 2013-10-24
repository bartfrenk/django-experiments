from django.conf.urls import patterns, url, include
from ubiqu import views

urlpatterns = patterns('',
    url(r'^dates$', views.DateTimeIntervalView.as_view(), name='datetime_form'),
    url(r'^wizard', include('wizards.urls'))
)

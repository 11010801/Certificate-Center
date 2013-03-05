from django.conf.urls import patterns, url

urlpatterns = patterns('verify.views',
    url(r'^$', 'detail'),
)
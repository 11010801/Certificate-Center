from django.conf.urls import patterns, url

urlpatterns = patterns('verify.views',
    url(r'^$', 'changeKey'),
    url(r'^registverify/', 'registVerify'),
    url(r'^verifyuser/', 'verifyUser'),
)

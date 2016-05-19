from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test, name='test'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<pk>\d+)/', test, name='question_detail'),
    url(r'^ask/', test, name='question_ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
]
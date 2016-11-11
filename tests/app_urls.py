from django.conf.urls import url


def index(request):
    pass


def sum(request):
    pass


urlpatterns = [
    url(r'^$', index, name='the-index-view'),
    url(r'^sum/(?P<left>\d+),(?P<right>\d+)$', sum, name='sum'),
]

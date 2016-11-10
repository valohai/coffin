from django.conf.urls import include, url

urlpatterns = [
    url(r'^url_test/', include('tests.app_urls')),

    # These two are used to test that our url-tag implementation can
    # deal with application namespaces / the 'current app'.
    url(r'^app/one/', include('tests.app_urls', app_name='testapp', namespace='testapp')),  # default instance
    url(r'^app/two/', include('tests.app_urls', app_name='testapp', namespace='two')),
]

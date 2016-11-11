from django.template.defaultfilters import upper, urlize
from jinja2 import Environment

from coffin.interop import django_filter_to_jinja2


def test_django_to_jinja():
    env = Environment()
    env.filters.update({
        'urlize': django_filter_to_jinja2(urlize),
        'upper': django_filter_to_jinja2(upper),
    })
    assert env.from_string(
        '{{ "foo"|upper }} {% filter urlize %}http://example.com{% endfilter %}'
    ).render() == 'FOO <a href="http://example.com" rel="nofollow">http://example.com</a>'

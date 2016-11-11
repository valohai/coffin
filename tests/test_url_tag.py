from __future__ import print_function, unicode_literals

import pytest
from django.core.urlresolvers import NoReverseMatch
from jinja2 import Environment, TemplateSyntaxError

from coffin import URLExtension


@pytest.mark.parametrize('template, context, expected_result', [
    # various ways to specify the view
    ('{% url the-index-view %}', {}, '/url_test/'),
    ('{% url "the-index-viewXX"[:-2] %}', {}, '/url_test/'),
    ('{% url the-index-view %}', {}, '/url_test/'),

    # various ways to specify the arguments
    ('{% url sum 1,2 %}', {}, '/url_test/sum/1,2'),
    ('{% url sum left=1,right=2 %}', {}, '/url_test/sum/1,2'),
    ('{% url sum l,2 %}', {'l': 1}, '/url_test/sum/1,2'),
    ('{% url sum left=l,right=2 %}', {'l': 1}, '/url_test/sum/1,2'),
    ('{% url sum left=2*3,right=z()|length %}',
     {'z': lambda: 'u'}, '/url_test/sum/6,1'),  # full expressive syntax

    # regression: string view followed by a string argument works
    ('{% url "sum" "1","2" %}', {}, '/url_test/sum/1,2'),

    # failures
    ('{% url %}', {}, TemplateSyntaxError),
    ('{% url 1,2,3 %}', {}, TemplateSyntaxError),
    ('{% url inexistant-view %}', {}, NoReverseMatch),

    # ValueError, not TemplateSyntaxError:
    # We actually support parsing a mixture of positional and keyword
    # arguments, but reverse() doesn't handle them.
    ('{% url sum left=1,2 %}', {'l': 1}, ValueError),

    # as-syntax
    ('{% url the-index-view as url %}', {}, ''),
    ('{% url the-index-view as url %}{{url}}', {}, '/url_test/'),
    ('{% url inexistent as url %}{{ url }}', {}, ''),  # no exception
])
def test_url(template, context, expected_result):
    env = Environment(extensions=[URLExtension])
    print(template, '==', expected_result)
    try:
        actual_result = env.from_string(template).render(context)
    except Exception as e:
        print('==> %s: (%s)' % (type(e), e))
        assert isinstance(e, expected_result)
    else:
        print('==> %s' % actual_result)
        assert actual_result == expected_result


def test_url_current_app():
    """Test that the url can deal with the current_app context setting."""
    from django.template import engines
    from django.http import HttpRequest
    t = engines['jinja2'].from_string('{% url testapp:the-index-view %}')
    assert t.render(request=HttpRequest()) == '/app/one/'
    request = HttpRequest()
    request.current_app = "two"
    assert t.render(request=request) == '/app/two/'

    request = HttpRequest()
    request.current_app = "three"  # nonexistent
    assert t.render(request=request) == '/app/one/'

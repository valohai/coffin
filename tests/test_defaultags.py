from __future__ import print_function, unicode_literals

from jinja2 import Environment

from coffin import LoadExtension, SpacelessExtension, WithExtension


def test_load():
    env = Environment(extensions=[LoadExtension])

    # the load tag is a no-op
    assert env.from_string('a{% load %}b').render() == 'ab'
    assert env.from_string('a{% load news.photos %}b').render() == 'ab'
    assert env.from_string('a{% load "news.photos" %}b').render() == 'ab'

    # [bug] invalid code was generated under certain circumstances
    assert env.from_string('{% set x=1 %}{% load "news.photos" %}').render() == ''


def test_spaceless():
    env = Environment(extensions=[SpacelessExtension])

    assert env.from_string("""{% spaceless %}
<p>
    <a href="foo/">Foo</a>
</p>
{% endspaceless %}""").render() == '<p><a href="foo/">Foo</a></p>'
    assert env.from_string("""{% spaceless %}
    <strong>
        Hello
    </strong>
{% endspaceless %}""").render() == '<strong>\n        Hello\n    </strong>'


def test_with():
    env = Environment(extensions=[WithExtension])
    assert env.from_string('{{ x }}{% with y as x %}{{ x }}{% endwith %}{{ x }}').render({'x': 'x', 'y': 'y'}) == 'xyx'

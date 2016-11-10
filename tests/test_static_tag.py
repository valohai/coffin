import pytest
from jinja2 import Environment

from coffin.static import StaticExtension, GetStaticPrefixExtension, GetMediaPrefixExtension
from coffin.staticfiles import StaticExtension as StaticFilesExtension


# The two extensions are almost similar -- one uses the staticfiles storage for url
# acquisition, the other uses the `STATIC_URL` configuration setting.
@pytest.mark.parametrize('extension', [
    StaticExtension,
    StaticFilesExtension,
])
@pytest.mark.parametrize('template', [
    '{% static "hello.txt" as foo %}{{ foo }}',
    '{% static "hello.txt" %}',
])
def test_static_tag(extension, template):
    env = Environment(extensions=[extension])
    assert env.from_string(template).render() == '/static/hello.txt'


@pytest.mark.parametrize('extension, expected_value', [
    (GetMediaPrefixExtension, '/media/'),
    (GetStaticPrefixExtension, '/static/'),
])
@pytest.mark.parametrize('with_assign', (False, True))
def test_prefix_tags(extension, expected_value, with_assign):
    env = Environment(extensions=[extension])
    tag = list(extension.tags)[0]
    if with_assign:
        template = '{%% %s as foo %%}{{ foo }}' % tag
    else:
        template = '{%% %s %%}' % tag
    assert env.from_string(template).render() == expected_value

import pytest
from jinja2 import Environment

from coffin.static import StaticExtension
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

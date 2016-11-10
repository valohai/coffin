__version__ = (2, 0, '0')

from coffin.common import (
    LoadExtension,
    URLExtension,
    WithExtension,
    SpacelessExtension,
    load,
    url,
    with_,
    spaceless,
)

from coffin.static import (
    StaticExtension,
    GetStaticPrefixExtension,
    GetMediaPrefixExtension,
)

COFFIN_EXTENSIONS = [
    'coffin.LoadExtension',
    'coffin.URLExtension',
    'coffin.WithExtension',
    'coffin.SpacelessExtension',
    'coffin.StaticExtension',
]
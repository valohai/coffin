__version__ = (2, 1, '0')

from coffin.common import (
    load,
    LoadExtension,
    spaceless,
    SpacelessExtension,
    url,
    URLExtension,
    with_,
    WithExtension
)
from coffin.static import (
    GetMediaPrefixExtension,
    GetStaticPrefixExtension,
    StaticExtension
)

COFFIN_EXTENSIONS = [
    'coffin.LoadExtension',
    'coffin.URLExtension',
    'coffin.WithExtension',
    'coffin.SpacelessExtension',
    'coffin.StaticExtension',
]

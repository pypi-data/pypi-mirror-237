import sys
import warnings

from matplotlib import font_manager

from h2o_autodoc.config.config import Config
from h2o_autodoc.h2o3.autodoc import render_autodoc
from h2o_autodoc.base.constants import (
    AUTODOC_DEFAULT_FONTS_DIR,
)

try:
    from . import build_info as bi

    __version__ = {n: getattr(bi, n) for n in dir(bi) if not n.startswith("__")}
except ImportError:
    __version__ = {}

warnings.filterwarnings("ignore", category=DeprecationWarning)

if sys.version_info[0] == 3 and sys.version_info[1] <= 6:
    print(
        "Warning! Support for Python 3.6 will be dropped from v1.0.10 onwards."
    )

# load default AutoDoc fonts
for f in font_manager.findSystemFonts(AUTODOC_DEFAULT_FONTS_DIR):
    font_manager.fontManager.addfont(f)

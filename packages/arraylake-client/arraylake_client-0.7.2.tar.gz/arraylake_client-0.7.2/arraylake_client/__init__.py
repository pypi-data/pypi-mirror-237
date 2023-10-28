import importlib
import warnings

from arraylake import *  # noqa

__version__ = importlib.metadata.version("arraylake")


warnings.warn(
    "`import arraylake_client` is deprecated. Use `import arraylake` instead to silence this warning",
    FutureWarning,
)

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.14.0"




from ._function import napari_experimental_provide_function
from ._dock_widget import napari_experimental_provide_dock_widget
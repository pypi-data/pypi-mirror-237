version = "0.1.5"


def hello():
    print('Hello from Dockme in Version:', version)


def get_version():
    print('Version:', version)



from .get_image import get_image
from .run_container import run_container
from .stop_container import stop_container
from .data.delet_container import delet_container
from .delet_image import delet_image
from .run_command_in_con import run_command
from .simple_funtion import show_images, show_all_container, show_running_container
from .start_stop_compose import stop_compose, run_compose



__all__ = [
    'get_image',
    'run_container',
    'stop_container',
    'delet_container',
    'delet_image',
    'run_command',
    'show_images',
    'show_all_container',
    'show_running_container',
    'run_compose',
    'stop_compose'
]
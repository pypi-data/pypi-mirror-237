version = "0.1.4"


def hello():
    print('Hello from Dockme in Version:', version)


def get_version():
    print('Version:', version)



from .data.get_image import get_image
from .data.run_container import run_container
from .data.stop_container import stop_container
from .data.delet_container import delet_container
from .data.delet_image import delet_image
from .data.run_command_in_con import run_command
from .data.simple_funtion import show_images, show_all_container, show_running_container
from .data.start_stop_compose import stop_compose, run_compose



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
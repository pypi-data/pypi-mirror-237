import os


def show_running_container():
    try:
        runnings = os.system('docker ps')
        return runnings
    except:
        print("Could not execute command")
        
def show_all_container():
    try:
        containers = os.system('docker ps -a')
        return containers
    except:
        print("Could not execute command")

def show_images():
    try:
        images = os.system('docker image list')
        return images
    except:
        print("Could not execute command")
# post_install_script.py
import atexit

def post_install_action():
    print("Post-installation script: Package is now installed!")

atexit.register(post_install_action)
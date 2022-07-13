import os
import subprocess

from os import getenv
from typing import List  # noqa: F401
from groups import *
from layouts import *
from screens import *
from shortcuts import *
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(f"~/.config/qtile/autostart/autostart.sh")
    subprocess.run([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "LG3D"

from config import *
from libqtile import bar, widget
from libqtile.config import Drag, Click, Screen
from libqtile.lazy import lazy
from shortcuts import mod
from utils import loadtheme

tema = loadtheme()

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.GroupBox(
                        font='Agave Nerd Font',
                        fontsize= 16,
                        # Spacing settings
                        margin_x = -1,
                        spacing = 2,

                        highlight_method='line',

                        # Color Settings
                        background = tema["bar"]["groupbox"]["background"],
                        active= tema["bar"]["groupbox"]["active"],
                        inactive= tema["bar"]["groupbox"]["inactive"],

                        this_current_screen_border = [tema["bar"]["groupbox"]["this_current_screen_border"]],
                        other_current_screen_border = [tema["bar"]["groupbox"]["line_active"]],
                        highlight_color = tema["bar"]["groupbox"]["line_hilight_color"],
                        other_screen_border = tema["bar"]["groupbox"]["other_screen_border"],

                        # Basic Settings
                        disable_drag = True,
                        rounded = False,
                        center_aligned = True
                    ),
                widget.WindowName(
                    fontsize=16,
                    padding = 500,
                    background= tema["widgets"]["background"], 
                    foreground= tema["widgets"]["window-name-font-color"],
                    format='{name}',
                    max_chars = 30,
                    ),
                widget.TextBox(
                    text="\ue0b2",
                    fontsize = 34,
                    background= tema["widgets"]["background"], 
                    foreground= tema["widgets"]["colors"]["four"], 
                    padding = -1
                    ),
                widget.TextBox(
                    text= ' ',
                    foreground= tema["widgets"]["font-color"], 
                    background = tema["widgets"]["colors"]["four"]
                ),
                widget.CurrentLayout(
                    foreground= tema["widgets"]["font-color"], 
                    background= tema["widgets"]["colors"]["four"]
                ),
                widget.TextBox(
                    text="\ue0b2",
                    fontsize = 34,
                    background = tema["widgets"]["colors"]["four"],
                    foreground = tema["widgets"]["colors"]["three"],
                    padding = -1
                ),
                widget.TextBox(
                    text='',
                    foreground = tema["widgets"]["font-color"],
                    background = tema["widgets"]["colors"]["three"]
                ),
                widget.Clock(
                    fromat = '%I:%M %p', 
                    foreground= tema["widgets"]["font-color"], 
                    background= tema["widgets"]["colors"]["three"]
                ),
                widget.TextBox(
                    text="\ue0b2",
                    fontsize = 34,
                    background = tema["widgets"]["colors"]["three"],
                    foreground = tema["widgets"]["colors"]["two"],
                    padding = -1
                ),
                widget.TextBox(
                    text='',
                    foreground = tema["widgets"]["font-color"],
                    background = tema["widgets"]["colors"]["two"]
                ),
                widget.Clock(
                    format= '%d/%m/%Y', 
                    foreground= tema["widgets"]["font-color"],  
                    background= tema["widgets"]["colors"]["two"]
                ),
                widget.TextBox(
                    text="\ue0b2",
                    fontsize = 34,
                    background = tema["widgets"]["colors"]["two"],
                    foreground = tema["widgets"]["colors"]["one"],
                    padding = -1
                ),
                widget.TextBox(
                    text= ' ',
                    mouse_callbacks={'Button1': lazy.spawn('eww open power')},
                    foreground= tema["widgets"]["font-color"], 
                    background = tema["widgets"]["colors"]["one"] 
                )
            ],
            32,
            margin = [10,5,10,5],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

from libqtile.config import Group, Key
from shortcuts import keys, mod 
from libqtile.command import lazy


groups = [Group(i) for i in [
    '  ',' ',' ',' ','響 '
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

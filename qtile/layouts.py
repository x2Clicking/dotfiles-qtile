from libqtile import layout
from libqtile.config import Match
from utils import loadtheme

tema = loadtheme()

layout_conf = {
    'border_focus': tema["screens"]["border"]["focus"],
    'border_normal' : tema["screens"]["border"]["normal"],
    'margin': 6
}
layouts = [
    layout.Columns(**layout_conf),
    layout.Max(**layout_conf),
    layout.MonadTall(**layout_conf),
]

widget_defaults = dict(
    font='Agave Nerd Font',
    fontsize=16,
    padding = 10
)
extension_defaults = widget_defaults.copy()

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
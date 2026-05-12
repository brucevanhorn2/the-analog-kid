## The Analog Kid — Configuration

define config.name = _("The Analog Kid")
define config.version = "0.1.0"
define build.name = "the_analog_kid"
define build.version = "0.1.0"

define gui.show_name = True
define gui.about = _("A story about a town, and the choices that shaped it.")

define config.window_title = "The Analog Kid"
define config.screen_width = 1920
define config.screen_height = 1080

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 40
default preferences.afm_time = 15

define config.save_directory = "the-analog-kid-0.1"

define config.window_icon = "gui/window_icon.png"

define config.console = True

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')

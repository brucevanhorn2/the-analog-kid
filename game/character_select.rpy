## The Analog Kid — Illustrated Character Select
##
## Replaces the plain text menu with a portrait roster. Each card returns the
## chosen protagonist id; `start` wires that into player_char.

image port_carver = "images/portraits/carver.png"
image port_geri   = "images/portraits/geri.png"
image port_ray    = "images/portraits/ray.png"
image port_frank  = "images/portraits/frank.png"
image port_june   = "images/portraits/june.png"
image port_samuel = "images/portraits/samuel.png"

init python:
    ## (id, name, role, side) — grid fills row-major, 3 across.
    CHARACTER_ROSTER = [
        ("samuel", "Dr. Samuel Beaumont", "Physician",            "South Side"),
        ("carver", "Rev. Thomas Carver",  "Pastor · First Baptist", "North Side"),
        ("geri",   "Dr. Geraldine Habicht", "Professor of Statistics", "North Side"),
        ("ray",    "Raymond Coldwater",   "County Social Worker",  "South Side"),
        ("frank",  "Frank DeLuca",        "Police Detective",      "North Side"),
        ("june",   "June Holloway",       "City Council",          "North Side"),
    ]


screen character_select_screen():

    tag menu
    modal True

    add "bg_main_street_1955"
    add Solid("#0a0a0fcc")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 18

        text "Whose story is this?":
            xalign 0.5
            size 40
            color "#e8c87a"
            font gui.text_font

        text "Middletown, 1955 — choose the eyes you'll see it through.":
            xalign 0.5
            size 18
            color "#b09060"

        null height 6

        grid 3 2:
            xalign 0.5
            xspacing 26
            yspacing 14

            for cid, name, role, side in CHARACTER_ROSTER:
                button:
                    xysize (270, 300)
                    background "#00000000"
                    hover_background "#cc660033"
                    action Return(cid)

                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5

                        add ("port_" + cid) zoom 0.128 xalign 0.5

                        text "[name]":
                            xalign 0.5
                            size 19
                            color "#f0e0c0"
                        text "[role]":
                            xalign 0.5
                            size 14
                            color "#cc9966"
                        text "[side]":
                            xalign 0.5
                            size 12
                            color "#8a8a8a"

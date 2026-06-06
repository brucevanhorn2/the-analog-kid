## The Analog Kid — Navigation System
##
## Room-based, Myst-style exploration. The player roams freely between
## connected locations (the hub loop, `explore_1955`) until they choose to
## proceed to their character's decision for the period.

init python:
    NAV_GRAPH = {
        "hospital_north":    ["first_baptist", "main_street"],
        "first_baptist":     ["hospital_north", "main_street"],
        "barbershop":        ["main_street"],
        "frank_office":      ["main_street"],
        "main_street":       ["hospital_north", "first_baptist", "earls_diner",
                              "mcswain_block", "town_square", "college_campus",
                              "library", "vfw_hall", "barbershop", "tracks_crossing",
                              "frank_office", "holloway_derrick", "high_school_road"],
        "earls_diner":       ["main_street"],
        "mcswain_block":     ["main_street"],
        "college_campus":    ["main_street", "library", "geri_office"],
        "geri_office":       ["college_campus", "library"],
        "library":           ["main_street", "college_campus", "geri_office"],
        "vfw_hall":          ["main_street"],
        "town_square":       ["main_street", "city_hall", "post_office"],
        "city_hall":         ["town_square"],
        "post_office":       ["town_square"],
        "tracks_crossing":   ["main_street", "south_side_entry",
                              "train_station", "bus_station"],
        "train_station":     ["tracks_crossing"],
        "bus_station":       ["tracks_crossing"],
        "south_side_entry":  ["tracks_crossing", "mount_zion", "tribal_office",
                              "beaumont_practice", "ihs_clinic", "blanton_factory"],
        "mount_zion":        ["south_side_entry"],
        "tribal_office":     ["south_side_entry"],
        "beaumont_practice": ["south_side_entry", "ihs_clinic"],
        "ihs_clinic":        ["south_side_entry", "beaumont_practice"],
        "blanton_factory":   ["south_side_entry"],
        "holloway_derrick":  ["main_street"],
        "high_school_road":  ["main_street"],
    }

    ## Nicer button captions than a naive title-case of the key.
    LOCATION_DISPLAY_NAMES = {
        "ihs_clinic":        "IHS Clinic",
        "mcswain_block":     "McSwain Block",
        "vfw_hall":          "VFW Hall",
        "geri_office":       "Science Hall",
        "frank_office":      "Police Station",
        "beaumont_practice": "Beaumont's Practice",
        "tribal_office":     "Tribal Office",
        "holloway_derrick":  "Holloway Derrick",
        "high_school_road":  "High School Road",
        "south_side_entry":  "South Side",
        "tracks_crossing":   "Railroad Crossing",
        "hospital_north":    "North Hospital",
        "first_baptist":     "First Baptist",
        "mount_zion":        "Mount Zion",
        "earls_diner":       "Earl's Diner",
    }

    ## Where the "proceed with your day" affordance sends each protagonist.
    ## Samuel/Ray flow into their nudge through the clinic scene that sets it up.
    ## The others have self-contained nudge scenes.
    PROCEED_LABELS = {
        "samuel": "location_ihs_clinic_1955_samuel",
        "ray":    "location_ihs_clinic_1955_ray",
        "carver": "carver_1955_nudge",
        "geri":   "geri_1955_nudge",
        "frank":  "frank_1955_nudge",
        "june":   "june_1955_nudge",
    }

    PROCEED_CAPTION = {
        "samuel": "▸  Walk to the IHS clinic",
        "ray":    "▸  Walk to the IHS clinic",
        "carver": "▸  It's nearly time for the board meeting",
        "geri":   "▸  The afternoon meeting is coming",
        "frank":  "▸  Back to the office to decide",
        "june":   "▸  To the council chamber",
    }

    ## 1967 decision routing (self-contained nudge scenes).
    PROCEED_LABELS_1967 = {
        "samuel": "samuel_1967_nudge",
        "carver": "carver_1967_nudge",
        "geri":   "geri_1967_nudge",
        "ray":    "ray_1967_nudge",
        "frank":  "frank_1967_nudge",
        "june":   "june_1967_nudge",
    }
    PROCEED_CAPTION_1967 = {
        "samuel": "▸  Decide what to do about Darnell",
        "carver": "▸  The march is Monday — decide",
        "geri":   "▸  Deliver the report",
        "ray":    "▸  Decide what to do with the list",
        "frank":  "▸  The list is on the desk — decide",
        "june":   "▸  Thursday's vote",
    }

    PROCEED_LABELS_1979 = {
        "samuel": "samuel_1979_nudge",
        "carver": "carver_1979_nudge",
        "geri":   "geri_1979_nudge",
        "ray":    "ray_1979_nudge",
        "frank":  "frank_1979_nudge",
        "june":   "june_1979_nudge",
    }
    PROCEED_CAPTION_1979 = {
        "samuel": "▸  Decide how the file enters the world",
        "carver": "▸  Harold is waiting in the study",
        "geri":   "▸  Answer Frank's question",
        "ray":    "▸  Decide about George's warning",
        "frank":  "▸  Resolve the Blanton case",
        "june":   "▸  Thursday's budget vote",
    }

    _PROCEED_BY_PERIOD = {
        1967: (PROCEED_LABELS_1967, PROCEED_CAPTION_1967),
        1979: (PROCEED_LABELS_1979, PROCEED_CAPTION_1979),
    }

    def proceed_label():
        labels = _PROCEED_BY_PERIOD.get(store.current_period, (PROCEED_LABELS, None))[0]
        return labels.get(store.player_char)

    def proceed_caption():
        caps = _PROCEED_BY_PERIOD.get(store.current_period, (None, PROCEED_CAPTION))[1]
        return caps.get(store.player_char, "▸  Continue")

    def get_exits(location):
        return NAV_GRAPH.get(location, [])

    def location_label(loc):
        return LOCATION_DISPLAY_NAMES.get(loc, loc.replace("_", " ").title())

    def can_visit(location):
        if location == "high_school_road":
            return store.keepsake_photo
        return True


## The navigation panel. Shown by the hub loop via `call screen`; each button
## returns the chosen destination (or the "__proceed__" sentinel).
screen nav_bar(loc):

    frame:
        style "nav_frame"
        xalign 0.5
        yalign 1.0
        yoffset -16

        vbox:
            spacing 10
            xalign 0.5

            text "Where would you like to go?":
                xalign 0.5
                size 22

            hbox:
                spacing 12
                xalign 0.5
                box_wrap True
                for dest in get_exits(loc):
                    if can_visit(dest):
                        textbutton location_label(dest):
                            action Return(dest)

            if proceed_label():
                textbutton proceed_caption():
                    xalign 0.5
                    action Return("__proceed__")


style nav_frame is frame:
    background "#0a0a0acc"
    padding (24, 16)


## Kept as a no-op so the many existing `call show_nav_bar` lines in the
## period scripts remain valid. Roaming is now driven by `explore_1955`.
label show_nav_bar:
    return


## The roam loop. Free exploration until the player chooses to proceed (or
## visits a location whose scene jumps straight into the decision).
label explore_1955:
    while True:
        call screen nav_bar(current_location)
        if _return == "__proceed__":
            jump expression proceed_label()
        $ current_location = _return
        $ mark_visited(_return)
        call expression "location_" + _return


## ---------------------------------------------------------------------------
## Dispatch labels — route a location to the right period/character version.
## Locations not yet authored for a period show a short placeholder.
## ---------------------------------------------------------------------------

label location_main_street:
    if current_period == 1955:
        jump location_main_street_1955
    else:
        "Main Street."
        return

label location_beaumont_practice:
    if current_period == 1955:
        jump location_beaumont_practice_1955
    elif current_period == 1967:
        jump location_beaumont_practice_1967
    else:
        "Dr. Beaumont's practice."
        return

label location_hospital_north:
    if current_period == 1955:
        jump location_hospital_north_1955
    elif current_period == 1967:
        jump location_hospital_north_1967
    elif current_period == 1979:
        jump location_hospital_north_1979
    else:
        "The north side hospital."
        return

label location_ihs_clinic:
    if current_period == 1955:
        if player_char == "ray":
            jump location_ihs_clinic_1955_ray
        elif player_char == "june":
            jump location_ihs_clinic_1955_june
        else:
            jump location_ihs_clinic_1955_samuel
    elif current_period == 1967:
        if player_char == "ray":
            jump location_ihs_clinic_1967_ray
        else:
            jump location_ihs_clinic_1967_samuel
    elif current_period == 1979:
        if player_char == "ray":
            jump location_ihs_clinic_1979_ray
        else:
            jump location_ihs_clinic_1979_samuel
    else:
        "The IHS clinic."
        return

label location_tracks_crossing:
    if current_period == 1955:
        if player_char == "ray":
            jump location_tracks_crossing_1955_ray
        else:
            jump location_tracks_crossing_1955_samuel
    elif current_period == 1967:
        jump location_tracks_crossing_1967
    else:
        "The tracks crossing."
        return

label location_mount_zion:
    if current_period == 1955:
        jump location_mount_zion_1955
    elif current_period == 1967:
        if player_char == "ray":
            jump location_mount_zion_1967_ray
        else:
            jump location_mount_zion_1967_carver
    elif current_period == 1979:
        jump location_mount_zion_1979
    else:
        "Mt. Zion Baptist Church."
        return

label location_earls_diner:
    if current_period == 1955:
        jump location_earls_diner_1955
    elif current_period == 1967:
        jump location_earls_diner_1967
    elif current_period == 1979:
        jump location_earls_diner_1979
    else:
        "Earl's Diner."
        return

label location_south_side_entry:
    if current_period == 1955:
        if player_char == "ray":
            jump location_south_side_street_1955
        else:
            jump location_south_side_entry_1955
    elif current_period == 1967:
        jump location_south_side_street_1967
    else:
        "The south side."
        return

label location_first_baptist:
    if current_period == 1955:
        jump location_first_baptist_1955
    elif current_period == 1967:
        jump location_first_baptist_1967
    elif current_period == 1979:
        jump location_first_baptist_1979
    else:
        "First Baptist Church."
        return

label location_barbershop:
    if current_period == 1955:
        jump location_barbershop_1955
    elif current_period == 1967:
        jump location_barbershop_1967
    elif current_period == 1979:
        jump location_barbershop_1979
    else:
        "The barbershop."
        return

label location_geri_office:
    if current_period == 1955:
        jump location_geri_office_1955
    elif current_period == 1967:
        jump location_geri_office_1967
    elif current_period == 1979:
        jump location_geri_office_1979
    else:
        "The science hall office."
        return

label location_frank_office:
    if current_period == 1955:
        jump location_frank_office_1955
    elif current_period == 1967:
        if player_char == "samuel":
            jump location_frank_office_1967_samuel
        elif player_char == "ray":
            jump location_frank_office_1967_ray
        else:
            jump location_frank_office_1967_frank
    elif current_period == 1979:
        if player_char == "samuel":
            jump location_frank_office_1979_samuel
        elif player_char == "ray":
            jump location_frank_office_1979_ray
        else:
            jump location_frank_office_1979_frank
    else:
        "The police station."
        return

label location_mcswain_block:
    "McSwain Block — the theater, Woolworth's, and the bank."
    return

label location_town_square:
    if current_period == 1955:
        scene bg_town_square_1955 with dissolve
    "The town square. City Hall's clock dome rises over the green."
    return

label location_city_hall:
    if current_period == 1955:
        jump location_city_hall_1955
    elif current_period == 1967:
        if player_char == "june":
            jump location_city_hall_1967_june
        else:
            jump location_city_hall_1967_carver
    elif current_period == 1979:
        jump location_city_hall_1979
    else:
        "City Hall."
        return

label location_post_office:
    "The Art Deco post office."
    return

label location_train_station:
    "The train station. A shimmer hangs over the far end of the platform."
    return

label location_bus_station:
    "The bus station. A chalkboard lists the day's departures."
    return

label location_tribal_office:
    if current_period == 1955:
        jump location_tribal_office_1955
    elif current_period == 1967:
        jump location_tribal_office_1967
    elif current_period == 1979:
        jump location_tribal_office_1979
    else:
        "The tribal community office."
        return

label location_blanton_factory:
    if current_period == 1979:
        if player_char == "ray":
            jump location_blanton_factory_1979_ray
        else:
            jump location_blanton_factory_1979_frank
    else:
        "Blanton Manufacturing. The smokestacks are running."
        return

label location_college_campus:
    "Middletown College. The quad, the admin building, the science hall."
    return

label location_library:
    if current_period == 1955:
        jump location_library_1955
    elif current_period == 1967:
        jump location_library_1967
    else:
        "The public library."
        return

label location_vfw_hall:
    if current_period == 1955:
        jump location_vfw_hall_1955
    elif current_period == 1967:
        jump location_vfw_hall_1967
    else:
        "The VFW Hall."
        return

label location_holloway_derrick:
    if current_period == 1955:
        jump location_holloway_derrick_1955
    elif current_period == 1967:
        jump location_holloway_derrick_1967
    elif current_period == 1979:
        jump location_holloway_derrick_1979
    else:
        "The Holloway oil derrick."
        return

label location_high_school_road:
    "The road past the high school. The building is visible but never open."
    return

## The Analog Kid — Navigation System

init python:
    NAV_GRAPH = {
        "hospital_north":    ["first_baptist", "main_street"],
        "first_baptist":     ["hospital_north", "main_street"],
        "barbershop":        ["main_street"],
        "main_street":       ["hospital_north", "first_baptist", "earls_diner",
                              "mcswain_block", "town_square", "college_campus",
                              "library", "vfw_hall", "barbershop", "tracks_crossing"],
        "earls_diner":       ["main_street"],
        "mcswain_block":     ["main_street"],
        "college_campus":    ["main_street", "library"],
        "library":           ["main_street", "college_campus"],
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

    def get_exits(location):
        return NAV_GRAPH.get(location, [])

    def can_visit(location):
        if location == "high_school_road":
            return store.keepsake_photo
        return True


screen nav_bar():
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -20
        hbox:
            spacing 16
            for dest in get_exits(store.current_location):
                if can_visit(dest):
                    textbutton dest.replace("_", " ").title():
                        action [
                            Function(mark_visited, dest),
                            SetVariable("current_location", dest),
                            Jump("location_" + dest)
                        ]


label show_nav_bar:
    show screen nav_bar
    return


## Dispatch labels — route to the right period version.
## Each period file defines location_X_PERIOD labels.
## Locations not yet written for a period show a placeholder.

label location_main_street:
    if current_period == 1955:
        jump location_main_street_1955
    else:
        "Main Street."
        return

label location_beaumont_practice:
    if current_period == 1955:
        jump location_beaumont_practice_1955
    else:
        "Dr. Beaumont's practice."
        return

label location_hospital_north:
    if current_period == 1955:
        jump location_hospital_north_1955
    else:
        "The north side hospital."
        return

label location_ihs_clinic:
    if current_period == 1955:
        jump location_ihs_clinic_1955
    else:
        "The IHS clinic."
        return

label location_tracks_crossing:
    if current_period == 1955:
        jump location_tracks_crossing_1955
    else:
        "The tracks crossing."
        return

label location_mount_zion:
    if current_period == 1955:
        jump location_mount_zion_1955
    else:
        "Mt. Zion Baptist Church."
        return

label location_earls_diner:
    if current_period == 1955:
        jump location_earls_diner_1955
    else:
        "Earl's Diner."
        return

label location_south_side_entry:
    if current_period == 1955:
        jump location_south_side_entry_1955
    else:
        "The south side."
        return

label location_first_baptist:
    if current_period == 1955:
        jump location_first_baptist_1955
    else:
        "First Baptist Church."
        return

label location_barbershop:
    if current_period == 1955:
        jump location_barbershop_1955
    else:
        "The barbershop."
        return

label location_mcswain_block:
    "McSwain Block."
    return

label location_town_square:
    "Town Square."
    return

label location_city_hall:
    if current_period == 1955:
        jump location_city_hall_1955
    else:
        "City Hall."
        return

label location_post_office:
    "The post office."
    return

label location_train_station:
    "The train station."
    return

label location_bus_station:
    "The bus station."
    return

label location_tribal_office:
    if current_period == 1955:
        jump location_tribal_office_1955
    else:
        "The tribal community office."
        return

label location_blanton_factory:
    "Blanton Manufacturing."
    return

label location_college_campus:
    "Middletown College."
    return

label location_library:
    if current_period == 1955:
        jump location_library_1955
    else:
        "The public library."
        return

label location_vfw_hall:
    if current_period == 1955:
        jump location_vfw_hall_1955
    else:
        "The VFW Hall."
        return

label location_holloway_derrick:
    if current_period == 1955:
        jump location_holloway_derrick_1955
    else:
        "The Holloway oil derrick."
        return

label location_high_school_road:
    "The road past the high school."
    return

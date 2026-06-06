## The Analog Kid — Main Entry Point

label start:

    scene black with fade

    ## No explanation. No frame story. Just the town.
    pause 1.0
    narrator "Middletown, USA."
    pause 0.5
    narrator "1955."
    pause 1.5

    jump character_select


label character_select:

    scene black with dissolve

    ## "Whose eyes are you seeing this through?"
    ## Framed as perspective, not as character creation.
    ## No mention of simulation, AI, or Atanasoff.
    narrator "Whose story is this?"

    menu:
        "Rev. Thomas Carver — Pastor, First Baptist Church":
            $ player_char = "carver"
        "Dr. Geraldine Habicht — Professor, Statistics":
            $ player_char = "geri"
        "Raymond Coldwater — Social Worker, South Side":
            $ player_char = "ray"
        "Frank DeLuca — Detective, Middletown Police Department":
            $ player_char = "frank"
        "June Holloway — City Council, North Side":
            $ player_char = "june"
        "Dr. Samuel Beaumont — Physician, South Side":
            $ player_char = "samuel"

    jump period_1955_begin


# ---------------------------------------------------------------------------
# Period transitions
# ---------------------------------------------------------------------------

label advance_to_1967:
    $ current_period = 1967
    call photo_wall_transition
    jump period_1967_begin

label advance_to_1979:
    $ current_period = 1979
    call photo_wall_transition
    jump period_1979_begin

label advance_to_1991:
    $ current_period = 1991
    call photo_wall_transition
    jump period_1991_begin

label advance_to_normaltown:
    ## The PSW corruption sequence — player's first hint something is wrong.
    ## Broderick appears here for the first time.
    $ current_period = "normaltown"
    $ normaltown_visited = True
    jump period_normaltown_begin

label advance_to_2008:
    $ current_period = 2008
    call photo_wall_transition
    jump period_2008_begin


# ---------------------------------------------------------------------------
# Photo wall — between-period transition
# ---------------------------------------------------------------------------

label photo_wall_transition:

    scene black with dissolve
    # play music "audio/music/transition_hum.ogg" fadein 1.5

    ## The wall exists from the beginning. What changes is whether the player
    ## can see it clearly — and whether they understand what they're looking at.

    scene black with dissolve
    pause 1.0

    if self_awareness == 0:
        narrator "Years pass."
    elif self_awareness == 1:
        narrator "Years pass."
        thought "There are photographs on this wall."
        thought "I don't know why I notice that."
    elif self_awareness == 2:
        narrator "Years pass."
        thought "The photographs are blurred. Or I am."
        thought "I can't tell which."
    elif self_awareness == 3:
        thought "I can almost see the faces."
        thought "I think I know some of them."
    elif self_awareness >= 4:
        thought "Every face on this wall. Every year."
        thought "I've been here the whole time."
        $ self_awareness = min(self_awareness + 1, 5)

    pause 2.0
    scene black with dissolve
    # stop music fadeout 1.0
    return


# ---------------------------------------------------------------------------
# Endings
# ---------------------------------------------------------------------------

label ending_conservative:
    scene black with fade
    jump credits

label ending_progressive:
    scene black with fade
    jump credits

label ending_middle:
    scene black with fade
    jump credits

label ending_crash:
    ## Player held the middle perfectly. The simulation detects the anomaly.
    ## Broderick appears here — last moment of the game.
    scene black with fade
    jump ending_crash_sequence

label ending_crash_sequence:
    scene black with fade
    # play music "audio/music/atanasoff_hum.ogg" fadein 3.0
    pause 2.0
    david "Still there."
    david "I didn't think you'd make it this far."
    pause 1.5
    thought "I know this voice."
    thought "I have always known this voice."
    pause 2.0
    jump credits


label credits:
    scene black with fade
    # stop music fadeout 2.0
    pause 1.0
    narrator "The Analog Kid"
    pause 1.5
    narrator "A story about a town, and the choices that shaped it."
    pause 3.0
    return

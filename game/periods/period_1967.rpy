## The Analog Kid — Future-Period Placeholders
##
## The 1967+ chapters are not yet authored. These dispatchers give every
## protagonist a clean, error-free landing at the close of the 1955 chapter
## so the game ends gracefully instead of jumping to an undefined label.
## Defining all four future entry points also keeps `renpy lint` clean.

label period_1967_begin:

    $ current_period = 1967

    ## Authored 1967 threads route here; the rest fall through to the stub.
    if player_char == "samuel":
        jump samuel_1967_begin

    scene black with fade
    pause 0.5

    "1967."
    pause 1.0
    "Twelve years pass. The smokestacks still run. The tracks still divide the town."
    pause 1.5

    if player_char == "samuel":
        "Dr. Beaumont's 1967 chapter — \"The Man The System Is Starting To Tolerate\" — is still being written."
    elif player_char == "carver":
        "Reverend Carver's 1967 chapter — \"The Man Whose Answers Stop Working\" — is still being written."
    elif player_char == "geri":
        "Dr. Habicht's 1967 chapter — \"The Woman Whose Numbers Are Now Evidence\" — is still being written."
    elif player_char == "ray":
        "Ray Coldwater's 1967 chapter — \"The Man Holding Two Worlds Together\" — is still being written."
    elif player_char == "frank":
        "Frank DeLuca's 1967 chapter — \"The Man The Law Is Failing\" — is still being written."
    elif player_char == "june":
        "June Holloway's 1967 chapter — \"The Woman Progress Left Behind\" — is still being written."
    else:
        "The next chapter is still being written."

    jump preview_end


## These later entry points are unreachable in the 1955 preview (the 1955
## chapter always advances to 1967), but defining them keeps the build clean.

label period_1979_begin:
    $ current_period = 1979
    jump preview_end

label period_1991_begin:
    $ current_period = 1991
    jump preview_end

label period_normaltown_begin:
    $ current_period = "normaltown"
    jump preview_end

label period_2008_begin:
    $ current_period = 2008
    jump preview_end


label preview_end:
    pause 1.5
    "Thank you for playing this 1955 preview of {i}The Analog Kid{/i}."
    pause 2.5

    ## Return to the main menu unconditionally. Using full_restart (rather than
    ## a bare `return`) discards any call frames still on the stack — e.g. when
    ## the decision was reached by *navigating* into the clinic (a `call`) rather
    ## than via the Proceed button (a `jump`) — so the period can't accidentally
    ## fall back into the roam loop.
    $ renpy.full_restart()

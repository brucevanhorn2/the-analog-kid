## The Analog Kid — Period 1967
## Dr. Geraldine Habicht — "The Woman Whose Numbers Are Now Evidence."
## The integration report; Diana Chambers; the math on patience.

label geri_1967_begin:

    $ current_period = 1967
    $ current_location = "geri_office"
    $ mark_visited("geri_office")

    scene bg_geri_office_1967 with fade

    thought "Forty-seven years old."
    thought "The tuberculosis data aged into vindication. Twelve more years of it now, all pointing the same direction."

    "On the desk: the Surgeon General's report. 1964. Annotated in her hand — three methodological critiques, precise and correct."
    "She wrote them with a Lucky Strike burning in the ashtray. She is aware of the shape of that. She has decided the data on the cigarettes is not yet conclusive enough to override the data on her own concentration."

    "The college has been asked to formally integrate. On paper it already has. In practice, the south-side students in her statistics courses face what she faced in 1943."

    thought "I have the numbers on that too. Enrollment by address. Completion by address. The pattern draws itself."

    "A seventeen-page report sits squared on the drafting table. One-paragraph conclusion. A specific policy recommendation."

    thought "I wrote the conclusion last. It took forty-five minutes. The data took twelve years."

    jump geri_1967_diana


label geri_1967_diana:

    "There is a student in her advanced course this term. Diana Chambers. Isaiah Chambers' daughter, pre-law."
    "Exceptional. Visibly isolated, in the particular way Geri remembers being isolated — alone in a room full of people who have decided in advance what you are."

    thought "Agnes has been quietly ordering the materials Diana needs that the south-side branch library doesn't carry."
    thought "Neither of them has ever discussed it. It simply happens. It has been happening since the first week."

    "Geri lights a Lucky Strike and looks at the report."

    thought "I want someone to read this before I deliver it. Not to fix it. The math is the math."
    thought "I want to know what a person feels reading it. I have been looking at the numbers so long I cannot tell whether the conclusion is obvious or devastating."

    $ mark_talked("geri", "geri_office", "report")

    jump geri_1967_explore


label geri_1967_explore:
    $ current_location = "geri_office"
    jump explore_1955


# --- 1967 LOCATIONS ---

label location_geri_office_1967:
    $ mark_visited("geri_office")
    scene bg_geri_office_1967 with dissolve
    "The office. South-facing window. The tracks in the middle distance. The Lucky Strikes at her right elbow."
    if talked("samuel", "geri_office", "joint_1967") or geri_samuel_connection:
        thought "Samuel Beaumont's health-outcome data and my enrollment data are two halves of one photograph."
    thought "The report is squared on the table. Seventeen pages. One conclusion. The decision is what I do with it, and who I let stand beside me when I do."
    return

label location_library_1967:
    $ mark_visited("library")
    scene bg_library_1967 with dissolve
    "The college library. Agnes Pruitt at her cataloguing station, as she has been since 1938."
    if not talked("agnes", "library", "diana_1967"):
        $ mark_talked("agnes", "library", "diana_1967")
        agnes "The Chambers girl returned the regression text. Two weeks early. Annotated."
        geri "Of course she did."
        agnes "I ordered her the next three. They're under interlibrary loan, miscellaneous."
        "Where I file the things the administration would prefer not to notice."
        geri "Agnes—"
        agnes "You don't need to say anything, Geraldine. You never have."
        thought "She protected my work for twelve years. Now she is quietly building a road for a girl who hasn't been told yet that there's a road."
    else:
        thought "You do not smoke in Agnes Pruitt's library. It has never been discussed."
    return

# --- NUDGE ---

label geri_1967_nudge:

    scene bg_geri_office_1967 with dissolve

    "The report is finished. The new Dean expects it Friday."

    thought "I've been doing the math on patience. The return on investment declines significantly over time."
    thought "Three ways to deliver twelve years of evidence."

    menu geri_1967_nudge_choice:

        "Soften it. Findings only. Let the administration draw its own conclusions.":
            jump geri_nudge_conservative_1967

        "Deliver it to Samuel first. Present jointly — statistician and physician." if geri_samuel_connection:
            jump geri_nudge_middle_1967

        "Deliver it as written. Request a response in thirty days. Copy the state board.":
            jump geri_nudge_progressive_1967


label geri_nudge_conservative_1967:
    $ nudge_1967 = "conservative"
    $ policy_score -= 1
    "She removes the conclusion. The recommendation. What remains is seventeen pages of numbers that imply everything and demand nothing."
    thought "A reader who wants to see it will see it. A reader who does not will not have to."
    thought "I have made the data deniable in order to keep myself employable. I know exactly what I traded and what I bought."
    "She stubs out a filtered cigarette half-finished."
    thought "I am aware of the particular irony of my own dataset."
    jump geri_1967_nudge_after


label geri_nudge_middle_1967:
    $ nudge_1967 = "middle"
    "She takes the report across town first, to a small office building on the edge of the south side."
    samuel "You want to present this together."
    geri "Two halves of the same picture are harder to ignore than either half alone. That is not sentiment. It's just true."
    samuel "It is just true."
    "They deliver it jointly. A statistician and a physician, the enrollment data and the mortality data, laid side by side on the Dean's desk."
    thought "Neither of us could be dismissed as easily with the other one in the room."
    thought "Samuel has been making this argument in bodies for years. I have been making it in columns. Today we made it in the same sentence."
    jump geri_1967_nudge_after


label geri_nudge_progressive_1967:
    $ nudge_1967 = "progressive"
    $ policy_score += 2
    "She delivers it exactly as written. One conclusion. One recommendation. A request for a formal response within thirty days, copied to the state board of education."
    thought "Thirty days is a clock. Clocks are harder to ignore than reports. Every follow-up will cite the date this was sent."
    thought "The Dean will not enjoy the next thirty days. I did not write this to be enjoyed."
    "She lights a fresh Lucky Strike and goes back to the next dataset. There is always a next dataset."
    jump geri_1967_nudge_after


label geri_1967_nudge_after:
    scene bg_geri_office_1967 with dissolve
    "Evening. The department has emptied. The factory lights are visible across the tracks."
    jump geri_1967_period_end


label geri_1967_period_end:
    scene bg_geri_office_1967 with dissolve
    "Evening. The office is quiet. The column ledgers are stacked where they have been stacked for two decades."

    thought "Forty-seven years old. A war behind me that nobody asks about and a war on the television that everyone argues about."
    thought "I calculated firing solutions once. The numbers did not care whether they were convenient. I learned that in the first week and never unlearned it."
    thought "Diana Chambers is going to be a lawyer. I have decided to consider that one of my outputs."

    scene black with dissolve
    pause 0.5
    "1967."

    if nudge_1967 == "conservative":
        "Dr. Habicht delivered the findings and withheld the conclusion."
        "The administration thanked her for her thoroughness and changed nothing."
        pause 1.0
        "The data sat in a drawer, correct and quiet, the way it had sat before."
    elif nudge_1967 == "middle":
        "Dr. Habicht and Dr. Beaumont delivered the report together."
        "The Dean could dismiss a statistician. He could dismiss a south-side physician. He could not as easily dismiss both at once."
        pause 1.0
        "A pilot program reached three south-side students that fall. Diana Chambers was not one of them. She was already ahead of it."
    elif nudge_1967 == "progressive":
        "Dr. Habicht delivered it as written and started a thirty-day clock."
        "The state board acknowledged receipt, which is a small thing that turned out to be a hinge."
        pause 1.0
        "The college changed three policies that year and credited none of them to her. She noted this with the expression she uses for everything."

    pause 1.5
    "The return on patience declines over time. She had the data to prove it."
    pause 2.0

    jump advance_to_1979
